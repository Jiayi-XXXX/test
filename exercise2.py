def valid_username(user,L):
    if user=='sunny1' or user=='superS' or user=='likeA' or user=='qwerty':
        print('User Name Exists')
        return False
    elif len(user)>=4 and user.isalnum() and user[0].isalpha():
        print('Valid')
        return True
    else:
        print('Invalid')
        return False
        
def valid_password(pwd):
    if len(pwd)>=10 and pwd.isalnum():
        x,y,z=0,0,0      
        for i in pwd:
            if i.isupper():
                x+=1
            elif i.islower():
                y+=1
            elif i.isdigit():
                z+=1
        if x>=1 and y>=1 and z>=1:
            print('Valid')
            return True
        else:
            print('Invalid')
            return False
                

def add_user(L):
    x=0
    while x==0:
        username=input('Enter Username: ')
        if valid_username(username,userList):
            x=1
    while x==1:
         password=input('Enter Password: ')
         if valid_password(password):
             password2=input('Confirm Password: ')
             if password2==password:
                 print('User created')
                 userList.append([username,password])
                 x=2
   

userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'],
['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]

add_user(userList)
