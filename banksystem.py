def datetimeprinter():
    # import datetime
    # date = datetime.datetime.now()
    # return date
    import datetime
    x = datetime.datetime.now()
    print(x)

def userid():
    count = 000
    while True:
        count += 1
        return count
def get_Customer_details():
    user_name = input ("Enter User Name: ")
    userid()
    user_password =input ("Enter User Password")
    datetimeprinter()
    amount = int (input ("Enter Deposit Amount: "))
    try:
        if amount <= 0:
            print ("Deposit Amount should be Greater than 0")
        elif amount > 0:
            balance = amount
            print (f'Deposit Successful. New Balance: {balance}')
        else:
            print ("invalid")
    except ValueError:
            print('Amount should be in number')
    user_account[userid] = {'username':user_name ,'password': user_password , 'Balance': balance}
    with open ('user.txt','a') as userfile : 
        userfile.write (f'User_name: {user_name}\t')
        userfile.write (f'User_ID: {userid}\t')
        userfile.write (f'User_Password: {user_password}\t')
        userfile.write ('\n')
    with open ("transaction.txt", "a") as transaction_file :
        transaction_file.write (f'Initial Balance: {amount}\t')
        transaction_file.write (f'{datetimeprinter}\t')
        file.write ('\n')


def deposit():
    amount = int (input ("Enter Deposit Amount: "))
    try:
        if amount <= 0:
            print ("Deposit Amount should be Greater than 0")
        elif amount > 0:
            balance += amount
            print (f'Deposit Successful. New Balance: {balance}')
        else:
            print ("invalid")
    except ValueError:
        print("Amount should be Only in Numbers")

def withdraw():
    amount = int (input ("Enter Your Withdrawal Amount: "))
    try:
        if amount > balance:
            print ("Withdrawal Failed. Withdrawal amount cannot be greater than balance")
            print (f'Your Current Balance: {balance}')
        elif amount <= 0:
            print ("Withdrawal amount should be Greater than 0")
        elif amount <= balance:
            balance -= amount
            print (f"your current Balance: {balance}")
        else:
            print ("insifficent fund")
    except ValueError:
        print('Amount should be in number')

def account_balance_check():
    userid = input ("enter Your ID to Check Balance: ")
    if userid in user_account:
        check = userid.get ('balance')
        print (f'Your Curreent Balance is : {check}')
    else:
        print ('Customer Account NOT Found')

user_account = {}
print ("\n HINA BANK \n")

print("1.Admin Login")
print("2.Customer Login")
choice = input ("choose a Number between 1 and 2 : ")
try:
    if choice == '1':
        print ("adminid = 1010  admin password = Thivah200425")
        Admin_account = {'adminid': '1010', 'password' : 'Thivah200425'}
        while True:
            print ("\n====Login====\n")
            file = open ('user.txt' , 'a')
            admin = (input ('Enter Admin name : '))
            adminpassword = (input ('Enter Admin Password: '))
            if admin == Admin_account['adminid'] and adminpassword == Admin_account['password']:
            # if admin in Admin_account :
            #     check = admin.get('adminid') and adminpassword.get('password')
                print ("\nlogin successful😊\n")
                break
            else:
                print ("\nLogin failed... try again😞\n")

            file.write (f'AdminID= {admin}\t')
            file.write (f'Admin_password= {adminpassword}\t')
            file.write ("\n")
            file.close()
        while True:
            print ("\n=== MINI BANK SYSTEM ===\n")
            print ("1.create Account")
            print ("2.Deposit Money")
            print ("3.Withdraw Money")
            print ("4.Check Balance")
            print ("5.Transaction History")
            print ("6.Exit")

            choice = input ("Enter a Number between 1 to 6 : ")
            try:
                if choice == '1':
                    get_Customer_details()
                    # with open ('user.txt','a') as userfile , open ("transaction.txt", "a")as transactionfile:
                    # # user_account[userid] = {'username':user_name , 
                    # # 'password': user_password , 'Balance': balance}
                    #     userfile.write (f'User_name: {user_name}\t')
                    #     userfile.write (f'User_ID: {userid}\t')
                    #     userfile.write (f'User_Password: {user_password}\t')
                    #     transactionfile.write (f'Initial Balance: {amount}\t')
                    #     transactionfile.write (f'{datetimeprinter}\t')
                    #     file.write ('\n')
                    
                elif choice == '2':
                    file = open ('transaction.txt', 'a')
                    datetimeprinter()
                    deposit()
                    user_account[userid]['balance'] = balance
                    file.write(f'{userid} deposit amount: {amount}\t')
                    file.write(f'{deposit}\t')
                    file.write (f'{datetimeprinter}\t')
                    file.write('\n')
                    file.close()
                elif choice == '3':
                    file = open ('transaction.txt', 'a')
                    datetimeprinter()
                    withdraw()
                    user_account[userid]['balance'] = balance
                    file.write (f'{userid} Withdrawal amount: {amount}\t')
                    file.write (f'Transaction Date And Time: {datetimeprinter}\t')
                    file.write (f'{withdraw}\t')
                    file.write('\n')
                    file.close()
                elif choice == '4':
                    account_balance_check()
                elif choice == '5':
                    file = open ('transaction.txt')
                    print (file.read())
                elif choice == '6':
                    print ("Thank You For Using Our Bank Service😊")
                    break
                else:
                    print ("❌invalid Number...select a number between 1 to 6 ")
            except ValueError:
                print ('Choice should be in Number')

    elif choice == '2':
        while True:
            print ('1.Check balance')
            print ('2.Deposit Money')
            print ('3.Withdraw Money')
            print ('4.Exit')

            choice = input ('Choose a Number Between 1 to 4: ')
            try:
                if choice == '1':
                    account_balance_check()
                elif choice == '2':
                        file = open ('transaction.txt', 'a')
                        datetimeprinter()
                        deposit()
                        user_account[userid]['balance'] = balance
                        file.write(f'{userid} deposit amount: {amount}\t')
                        file.write(f'{deposit}\t')
                        file.write (f'{datetimeprinter}\t')
                        file.write('\n')
                        file.close() 
                elif choice == '3':
                        file = open ('transaction.txt', 'a')
                        datetimeprinter()
                        withdraw()
                        user_account[userid]['balance'] = balance
                        file.write (f'{userid} Withdrawal amount: {amount}\t')
                        file.write (f'Transaction Date And Time: {datetimeprinter}\t')
                        file.write (f'{withdraw}\t')
                        file.write('\n')
                        file.close()
                elif choice == '4':
                    print ('Thank You For Using Our Bank Service💖')
                    break
                else:
                    print ("Invalid Number... Select a Number Between 1 to 4")  
            except ValueError:
                 print ('Choice should be in Number')
except ValueError:
                 print ('Choice should be in Number')











