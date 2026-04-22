# EMail Validator
'''Author : Vijilee George Kurian 
   Description : A Simple Email Validator'''

emailAddress = input("Enter Your Email Address :")
if '@' in emailAddress:
    index=emailAddress.index('@')
    userName=emailAddress[:index]
    domainAddress=emailAddress[index+1:]
    print(f"Your User Name is :{userName} and \nDomain Name is :{domainAddress}")
else:
    print("Enter a Valid Email ID ")

  
