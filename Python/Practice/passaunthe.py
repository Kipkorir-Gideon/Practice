import getpass
database = {"gideon.ngetich": "123456", "ngetich.gideon": "654321"}
username = input("Enter Your Username: ")
password = getpass.getpass("Enter Your Password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again: ")
        break
print("Verified")