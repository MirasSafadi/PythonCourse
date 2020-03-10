db = {
    "user1":"password1",
    "user2":"password2",
    "user3":"password3",
    "user4":"password4",
    "user5":"password5",
    "user6":"password6",
    "user7":"password7",
    "user8":"password8",
    "user9":"password9",
    "user10":"password10"
}
username = str(input("Enter username..."))
password = str(input("Enter password..."))
if(db.get(username) != None):
    if(db.get(username) == password):
        print("ypu are now connected")
    else:
        print("incorrect password")
else:
    print("user does not exist")