def datetimeprinter():
    import datetime
    now = datetime.datetime.now()
    dt_string = now.strftime ("%Y-%m-%d %H:%M:%S")
    with open ("transaction.txt", "a") as transaction_file :
        transaction_file.write (f'Transcation Date and Time: {dt_string}\t')
        transaction_file.write('\n')

def customer_id_generation(prefix_letter, counter_file):
    try:
        with open(counter_file, 'r') as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        count = 0 

    def generate_user_id():
        nonlocal count
        count += 1
        user_id = f"{prefix_letter}{str(count).zfill(3)}"  

        
        with open(counter_file, 'w') as file:
            file.write(str(count))

        return user_id

    return generate_user_id

    
def get_Customer_details():
    user_name = input("Enter User Name: ")
    generator = customer_id_generation('C', 'user_counter.txt') 
    user_id = generator() 
    print(f"Your Unique User ID: {user_id}") 

    user_password = input("Enter User Password: ")
    datetimeprinter()
    amount = int(input("Enter Deposit Amount: "))

    try:
        if amount <= 0:
            print("Deposit Amount should be Greater than 0")
        elif amount > 0:
            balance = amount
            print(f'Deposit Successful. New Balance: {balance}')
        else:
            print("Invalid deposit amount")
    except ValueError:
        print('Amount should be a number')

    
    user_account[user_id] = {'username': user_name, 'password': user_password, 'balance': balance}
    with open('customer.txt', 'a') as customer_file:
        customer_file.write(f'User_ID: {user_id},')
        customer_file.write(f'User_Name: {user_name},')
        customer_file.write(f'User_Password: {user_password},')
        customer_file.write(f'Balance: {balance}\n')
    with open("transaction.txt", "a") as transaction_file:
        transaction_file.write(f'User ID: {user_id}, Initial Balance: {amount},')
        datetimeprinter()
        transaction_file.write('\n')


def deposit():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    balance = user_id_checker(user_id, password)

    if balance is None:
        print("Incorrect user ID or password.")
        return 
    try:
        amount = int (input ("Enter Deposit Amount: "))
        if amount <= 0:
            print ("Deposit Amount should be Greater than 0")
        elif amount > 0:
            balance += amount
            print (f'Deposit Successful. New Balance: {balance}')
            return user_id,balance
        else:
            print ("invalid")
    except ValueError:
        print("Amount should be Only in Numbers")

def user_id_checker(user_id, password):
    try:
        with open('customer.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[0] == user_id and user_data[2] == password:
                    return float(user_data[3]) 
    except FileNotFoundError: 
        print("User data file not found.")
    return None 

def withdraw():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    balance = user_id_checker(user_id, password)

    if balance is None:
        print("Incorrect user ID or password.")
        return 

    try:
        amount = int(input("Enter Your Withdrawal Amount: "))
        if amount > balance:
            print("Withdrawal Failed. Withdrawal amount cannot be greater than balance")
            print(f"Your Current Balance: {balance}")
        elif amount <= 0:
            print("Withdrawal amount should be greater than 0")
        elif amount <= balance:
            balance -= amount
            print(f"Your current Balance: {balance}")

            with open('customer.txt', 'r') as file:
                lines = file.readlines()
            
            with open('users.txt', 'w') as file:
                for line in lines:
                    user_data = line.strip().split(',')
                    if user_data[0] == user_id:
                        file.write(f"{user_id},{password},{balance}\n")
                    else:
                        file.write(line)

            with open('transaction.txt', 'a') as file:
                file.write(f'{user_id} Withdrawal amount: {amount}\t')
                datetimeprinter()
                file.write(f'{amount}\t')
                file.write('\n')
            return user_id,balance
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Amount should be a number.")

def account_balance_check():
    user_id = input ("enter Your ID to Check Balance: ")
    if user_id in user_account:
        check = user_id.get ('balance')
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
                    datetimeprinter()
                    result = deposit()
                    if result:
                        user_id, balance = result
                        user_account[user_id] = {'balance': balance}
                        with open("transaction.txt", 'a') as file:
                            file.write(f'{user_id} deposit amount: {balance}\n')

                elif choice == '3':
                    datetimeprinter()
                    result = withdraw()
                    if result:
                        user_id, balance = result
                        user_account[user_id] = {'balance': balance}
                        with open("transaction.txt", 'a') as file:
                            file.write(f'{user_id} Withdrawal amount: {balance}\n')

                        
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
                    datetimeprinter()
                    result = deposit()
                    if user_id and balance is not None:
                        user_account[user_id] = {'balance': balance}
                        with open("transaction.txt", 'a') as file:
                            file.write(f'{user_id} deposit amount: {balance}\n')

                elif choice == '3':
                    datetimeprinter()
                    result = withdraw()
                    if result:
                        user_id, balance = result
                        user_account[user_id] = {'balance': balance}
                        with open("transaction.txt", 'a') as file:
                            file.write(f'{user_id} Withdrawal amount: {balance}\n')

                elif choice == '4':
                    print ('Thank You For Using Our Bank Service💖')
                    break
                else:
                    print ("Invalid Number... Select a Number Between 1 to 4")  
            except ValueError:
                 print ('Choice should be in Number')
except ValueError:
                 print ('Choice should be in Number')











