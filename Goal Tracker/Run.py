from Login import *
import shutil



def UserMenu(login_path,Parent):
    User_Menu = input('What do you want to do? \n1.View Goals\n2.Create Goal\n3.Delete Goal\n4.Delete Account\n\nYour Choice: ')
    if User_Menu == '1':
        Goals_list = os.listdir(login_path)
        Goals_list.remove('password.txt')
        if len(Goals_list) == 0:
            print('You have no goals to view, please create one first.\n')
            time.sleep(2)
            UserMenu(login_path,Parent)
        else:
            print('\nSelect which goal you would like to view\n')
            for i in range(len(Goals_list)):
                print(f"{i+1}. {Goals_list[i].replace('.txt','')}")
            Goal_num = int(input('\nWhich goal do you want to view? '))-1
            print('\n')
            with open(login_path+'/'+Goals_list[Goal_num]) as f:
                print(f.read())
            time.sleep(5)
            UserMenu(login_path,Parent)
    if User_Menu == '2':
        NGoal = input('What is your new goal?\nGoal:')
        NGoal = NGoal+'.txt'
        Goal = open(NGoal,'a')
        print('What are the steps to your goal?(Type end to finish)')
        time.sleep(1)
        steps = ''
        stepnum = 1
        while steps != 'end':
            steps = input(f'What is step {stepnum}?: ')
            if steps != 'end':
                Goal.write(steps + '\n')
                stepnum+=1
            else:
                print('steps recorded succefully\n')
                time.sleep(2)
                UserMenu(login_path,Parent)                
    if User_Menu == '3':
        Goals_list = os.listdir(login_path)
        Goals_list.remove('password.txt')
        if len(Goals_list) == 0:
            print('You have no goals to delete, please create one first')
        else:
            print('Select which goal you would like to delete\n')
            for i in range(len(Goals_list)):
                print(f"{i+1}. {Goals_list[i].replace('.txt','')}")
            Goal_num = int(input('\nWhich goal do you want to delete? '))-1
            print('\n')
            goal_path = login_path+'/'+Goals_list[Goal_num]
            os.remove(goal_path)
            print(f"The goal '{Goals_list[Goal_num].replace('.txt','')}' has been deleted.")
            time.sleep(2)
            UserMenu(login_path,Parent)
    if User_Menu == '4':
        os.chdir(Parent)
        Delete_account = input('Are You Sure you want to delete account? Type Yes: ')
        if Delete_account == 'Yes':
            print('Deleting Acount...')
            time.sleep(3)
            shutil.rmtree(login_path,ignore_errors=True)
            print('Account Deletion Succeful')
            quit()

    
    