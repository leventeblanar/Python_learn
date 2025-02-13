# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except 3. finally


# try:
#      try some code
# except Exception:
#      handle an exception
# finally:
#      do some clean up

try: 
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero Idiot!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("something went wrong!")
finally:
    print("Do some cleanup here")
