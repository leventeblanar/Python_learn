import pandas as pd
import sys
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="UTF-8")
sys.stdout.reconfigure(encoding="UTF-8")


def read_email():

    imap_host = '*****' 
    email_user = '*****'
    email_pass = '*****'

    # Kapcsolódás az IMAP szerverhez
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(email_user, email_pass)
    mail.select("inbox")

    # Keresés: utolsó levél adott feladótól
    status, messages = mail.search(None, '(FROM "sender_email")')
    email_ids = messages[0].split()

    if not email_ids:
        print("Nem található levél ettől a feladótól.")
    else:
        latest_id = email_ids[-1]
        status, data = mail.fetch(latest_id, "(RFC822)")
        raw_email = data[0][1]

        msg = email.message_from_bytes(raw_email)

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        print("Tárgy:", subject)

        # Email szöveg kinyerése
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_dispo = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_dispo:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")
            
        print("\nEmail törzs:\n")
        print(body)

    mail.logout()
    return body

def cikkek_levalogatas():

    html_text = read_email()
    soup = BeautifulSoup(html_text, "html.parser")
    
    target_groups = {
        "DAX": [],
        "HANSA": [],
        "PL": [],
        "KEREKES CK_KOD": []
    }

    for h3 in soup.find_all("h3"):
        group_name = h3.get_text(strip=True).upper()
        next_p = h3.find_next_sibling("p")

        if next_p and group_name in target_groups:
            raw_text = next_p.get_text(separator="\n")
            lines = raw_text.strip().split("\n")
            codes = [line.strip().strip("[]") for line in lines if line.strip()]
            target_groups[group_name] = codes

    dax_df = pd.DataFrame(target_groups["DAX"], columns=["Cikkszám"])
    hansa_df = pd.DataFrame(target_groups["HANSA"], columns=["CikkID"])
    pl_df = pd.DataFrame(target_groups["PL"], columns=["CikkID"])
    kerekes_df = pd.DataFrame(target_groups["KEREKES CK_KOD"], columns=["Cikkszám"])

    print(dax_df)
    print(hansa_df)
    print(pl_df)
    print(kerekes_df)

    return dax_df, hansa_df, pl_df, kerekes_df


if __name__ == '__main__':
    # csekk_kerekes_cikk()
    read_email()
    cikkek_levalogatas()