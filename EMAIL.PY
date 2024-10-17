                   ######## Simple Email Validation Project #########

                            ## checking criterion list #####

# 1. Check for exactly one '@' symbol
# 2. Ensure there are characters before and after the '@'
# 3. Check for at least one '.' in the domain part (after '@')
# 4. check for space
# 5. check for upper case
# 6. check for first STRING letter.
# 7. check for minimum length



                              #####  PROGRAM START ########
email = input("Enter an email address to validate: ")


if email.count('@') == 1:

     if (at_index := email.index('@')) and email.count('@') == 1:
         if '.' in email[at_index:]:
             if " " not in email:
                 if email[0].isalpha():
                     if email == email.lower():

                            if len(email) >= 6:
                                if email == "":
                                    print("The email address can not be empty")
                                else:
                                    print("email is valid")

                            else:
                                print("Minimum character must be more than 6")

                     else:
                         print("character must not be in uppercase")

                 else:
                     print("first letter must be alphabet")
             else:
                 print("remove the space")


         else:
             print("The domain part must contain at least one '.' symbol.")


     else:
         print("There must be characters before and after the '@'")



else:
    print("The email address must contain exactly one '@' symbol.")

















