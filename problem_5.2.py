d = {"login": "sda", "password": 4234}
i=0
while i < 2:
    i+=1
    a = input('login')
    b = input('password') 
    d["login"] = a
    d["password"] = b
    print(d)
    with open("database.txt", 'a') as f:
        f.write(str(d))