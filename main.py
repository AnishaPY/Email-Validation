email = input("Enter your email address. ")
k,j,d = 0,0,0
if len(email) >= 6: #a@b.co
    if email[0].isalpha():
        if("@" in email) and (email.count("@") == 1):
            if(email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@" :
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong email.")
                else:
                    print("Your email is valid.")
            else:
                print("Sorry, the email address is not valid. \t !Recheck your \". \" position.")
        else:
            print("Invalid email address. \t !Place @ in your email address atmost once." )

    else:
        print("Enter a valid email address. \t !First character should be alphabet.")
else:
    print("Enter a valid email address.")
