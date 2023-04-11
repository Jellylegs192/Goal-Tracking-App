#Pre installed python packages
import os
import time
#My Files
from Run import UserMenu


Parent = ''

os.chdir(Parent)
Menu = input('1. Log In\n2. New User\n\nYour Choice: ')

if Menu == '1':
    count = 0
    User_name = input('Username: ')
    Read_Users = open('user_list.txt','r')
    for i in Read_Users:
        stripped = i.strip('\n')
        if User_name == stripped:
            count+=1
            print('Login Found')
            login_path = os.path.join(Parent,stripped)
            os.chdir(login_path)
            time.sleep(2)
            Read_password = input('What is your password?\nPassword: ')
            pass_login = open('password.txt','r')
            password_strip = pass_login.readline()
            password_strip = password_strip.strip('\n')
            if Read_password == password_strip:
                pass_login.close()
                print('\nLogged in Succefully\n')
                UserMenu(login_path,Parent)
            else:
                print('\nError: Incorrect Password, please try again')            
    if count == 0:
        print('\nError, User not found. Please Try again or Create an account.') 
if Menu == '2':
    os.chdir(Parent)
    New_User = input('Welcome! Please input your Username\n\nUsername: ')
    user_file = open('user_list.txt','a')
    user_file.write(f'\n{New_User}')
    user_file.close()
    npath = os.path.join(Parent, New_User)
    os.makedirs(npath)
    os.chdir(npath)
    password_file = open('password.txt','w')
    NPassword = input('Please Provide a password:\n\nPassword: ')
    password_file.write(NPassword)
    password_file.close()
    print('Success! Account has been created succefully. Please log in with your credentials')
