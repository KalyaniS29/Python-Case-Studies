import re

check_for = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w"
enter_email = input("Enter an email address to validate: ")

if re.search(check_for, enter_email):
    print("Email is valid.")

else:
  print("Email is invalid.")



