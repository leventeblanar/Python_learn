import pandas as pd
from db_config import get_connection
import psycopg2
from nio import AsyncClient, LoginResponse
import asyncio
import json

MATRIX_HOMESERVER = "****"
USERNAME = "****"
ROOM_ID = "****"
ACCESS_TOKEN = "****"

def setup_trigger():

    conn = get_connection()
    cur =conn.cursor()

    create_function = """
    CREATE OR REPLACE FUNCTION notify_new_entry() RETURNS TRIGGER AS $$
    BEGIN
        PERFORM pg_notify('new_entry', row_to_json(NEW)::text);
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """

    create_trigger = """
    DO $$
    BEGIN
        IF NOT EXISTS (
            SELECT 1 FROM pg_trigger WHERE tgname = 'new_entry_trigger'
        ) THEN
            CREATE TRIGGER new_entry_trigger
            AFTER INSERT ON invoice
            FOR EACH ROW EXECUTE FUNCTION notify_new_entry();
        END IF;
    END $$;
    """

    try:
        cur.execute(create_function)
        print("Notify function created.")

        cur.execute(create_trigger)
        print("Trigger created.")

        conn.commit()

    except Exception as e:
        print(f"Error during the setup of trigger: {e}")
    finally:
        cur.close()
        conn.close()

def get_new_entries():
    
    conn = get_connection()
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("Listen new_entry;")
    print("Waiting for new entry.")

    while True:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            data = json.loads(notify.payload)

            print(data)

            print(f"New entry detected: {data}")

            asyncio.run(send_matrix_message(data))

async def send_matrix_message(data):

    client = AsyncClient(MATRIX_HOMESERVER, USERNAME)

    client.access_token = ACCESS_TOKEN
    client.user_id = USERNAME

    try:
        message_text = (
            f"**New Entry Detected!**\n"
            f"---------------------------\n"
            f"Invoice ID: {data['invoice_id']}\n"
            f"Customer ID: {data['customer_id']}\n"
            f"invoice Date: {data['invoice_date']}\n"
            f"\n"
            f"**Billing Address**\n"
            f"Street, house: {data['billing_address']}\n"
            f"City: {data['billing_city']}\n"
            f"State: {data['billing_state']}\n"
            f"Country: {data['billing_country']}\n"
            f"Postal Code: {data['billing_postal_code']}\n"
            f"Total: ${data['total']}\n"
        )
        await client.room_send(
            room_id=ROOM_ID,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": message_text},
        )

        print("Message sent successfully!")

    finally:
        await client.close()
    

if __name__ == '__main__':
    setup_trigger()
    get_new_entries()
    # asyncio.run(send_matrix_message())