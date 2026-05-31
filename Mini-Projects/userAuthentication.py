def userNameAuthentication(userName):
    if bool(userName):
        return 1
    else:
        print("Please Enter a UserName ...")
        return 0

def passwordAuthentication(password):
    if bool(password):
        if len(password)>=6 and password.isalnum():
            return 1
        else:
            print("Password Should have atleast 6 characters and should be a mix of alpha numeric.")
            return 0
    else:
        print("please Enter a Password")
        return 0

userName=input("UserName : ")
password=input("Password : ")
if userNameAuthentication(userName) and passwordAuthentication(password):
    print("Login Successfull...")
else:
    print("Login Failed")
