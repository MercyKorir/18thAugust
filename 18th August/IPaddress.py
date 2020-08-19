#Logic of the code
def getipAddress(ipAddress):
    return ipAddress
#Frontent 
def userInput():
#The exception is being handled
    try:
    #The user is required to input the ip address
        ipAddress = input("Enter IP Address")
        #the ip address input is validated to see if it matches the format required
        import re
        if(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ipAddress)):
            #After confirming that it does match the format the ip address is output with a message
            print("Valid IP Address")
            print(ipAddress)
            #if the format input is not correct the invalid error message is output
        else:
            print("Invalid IP Address")
            #incase an errror occurs in running this program an exception is allowed to prevent crashing of the program
    except:
        print("There is an error. Something went wrong")
#the function is called to be run
userInput()