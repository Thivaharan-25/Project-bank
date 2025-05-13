#===  FUNCTION FOR GET DATE AND TIME  ==#
def datetimeprinter():
    import datetime
    now = datetime.datetime.now()
    dt = now.strftime ("%Y-%m-%d %H:%M:%S")
    with open ("transaction.txt", "a") as transaction_file :
        transaction_file.write (f' {dt}|\t')
        
        
#===  FUNCTION FOR AUTOMATICALLY GENERATE UNIQUE ID FOR ADMIN AND CUSTOMER  ===#
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

# def check_admin():
#     try:
#         with open('Admin.txt', 'r') as file:
#             for line in file:
#                 user_data = line.strip().split(',')
#                 if user_data[0] == admin and user_data[1] == adminpassword:
#                     print ("\nlogin successful😊\n")
#                     break
#             else:
#                 print ("\nLogin failed... try again😞\n")
#         with open ("Admin.txt","a") as file:
#             file.write (f'{admin},')
#             file.write (f'{adminpassword}\t')
#             file.write ("\n")
#             file.close()
#     except FileNotFoundError: 
#         print("User data file not found.")

#=== FUNCTION FOR UPDATE NEW CUSTOMER BALANCE TO THE USERS FILE  ===#
def update_user_balance_file(user_id, password, new_balance):
    try:
        with open('users.txt', 'r') as file:
            lines = file.readlines()

        with open('users.txt', 'w') as file:
            for line in lines:
                if user_id in line and password in line:
                    file.write(f"{user_id},{password},{new_balance}\n")
                else:
                    file.write(line)
    except FileNotFoundError:
        print("User file not found.")
        
        
#===  FUNCTION FOR CREATING CUSTOMER ACCOUNT  ===#  
def get_Customer_details():
    user_name = input("Enter Customer Name: ")
    generator = customer_id_generation('C', 'user_counter.txt') 
    user_id = generator() 
    print(f"Your Unique Customer ID: {user_id}") 

    user_password = input("Enter User Password: ")
    user_address = input('Enter Customer Address: ')
    datetimeprinter()

    try:
        amount = int(input("Enter Initial Deposit Amount:$ "))
        if amount <= 0:
            print("Deposit Amount should be Greater than 0")
        elif amount > 0:
            balance = amount
            print(f'Deposit Successful.Your Account Balance: {balance}💸')
        else:
            print("❌Invalid deposit amount")
    except ValueError:
        print('Amount should be a number')

    
    user_account[user_id] = {'username': user_name, 'password': user_password, 'balance': balance}
    with open('customer.txt', 'a') as customer_file:
        customer_file.write(f'Customer_ID: {user_id},')
        customer_file.write(f'Customer_Name: {user_name},')
        customer_file.write(f'Customer_Password: {user_password}')
        customer_file.write(f'Customer_Address: {user_address}\n')
    with open("transaction.txt", "a") as transaction_file:
        transaction_file.write(f'{user_id}\t| Initial Balance\t| {amount}\t|')
        datetimeprinter()
        transaction_file.write('\n')
    with open ('users.txt','a') as user_file:
        user_file.write (f'{user_id},{user_password},{amount}\n')


#== DEPOSIT FUNCTION ==#
def deposit():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    check = user_id_checker(user_id, password)

    if check is None:
        print("❌Incorrect user ID or password.")
        return 

    try:
        balance = check
        amount = int(input("Enter Deposit Amount:$ "))
        if amount <= 0:
            print("Deposit Amount should be Greater than 0")
        else:
            balance += amount
            print(f'Deposit Successful. New Balance: {balance}')

            update_user_balance_file(user_id, password, balance)

            with open('transaction.txt', 'a') as file:
                file.write(f'{user_id}\t| Deposit amount\t| {amount}\t|')
                datetimeprinter()
                file.write('\n')

            return user_id, balance,amount
    except ValueError:
        print("Amount should be only in numbers.")



#==FUNCTION THAT CHECK THE USER DETAIL==#
def user_id_checker(user_id, password):
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[0] == user_id and user_data[1] == password:
                    print (f'User_ID: {user_data[0]}, Your Balance: {user_data[2]}💸')
                    return float(user_data[2])
    except FileNotFoundError: 
        print("User data file not found.")
    return None 

#==  WITHDRAW FUNCTION  ==#
def withdraw():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    check = user_id_checker(user_id, password)

    if check is None:
        print("❌Incorrect user ID or password.")
        return 

    try:
        balance = check
        amount = int(input("Enter Your Withdrawal Amount: "))
        if amount > balance:
            print("Withdrawal Failed. Amount exceeds balance.")
        elif amount <= 0:
            print("Withdrawal amount should be greater than 0")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your current Balance:$ {balance}")

            update_user_balance_file(user_id, password, balance)

            with open('transaction.txt', 'a') as file:
                file.write(f'{user_id}\t| Withdrawal amount\t| {amount}\t|')
                datetimeprinter()
                file.write('\n')
            return user_id, balance,amount
    except ValueError:
        print("Amount should be a number.")
        
#==FUNCTION THAT CHECK THE USER DETAIL==#
def account_balance_check():
    user_id = input("Enter Your User ID: ")
    password = input("Enter Your Password: ")
    
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[0] == user_id and user_data[1] == password:
                    print(f"✅ User_ID: {user_data[0]}, Your Balance:$ {user_data[2]}")
                    return float(user_data[2])
            print("❌ Incorrect user ID or password.")
    except FileNotFoundError:
        print("❌ User file not found.")

#====   CREATNG ADMIN FILE   ====#    
try:
    with open('Admin.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    lines = []

found = False
for line in lines:
    if "A000" in line:
        found = True
        break

if not found:
    with open('Admin.txt', 'a') as file:
        file.write('A000,1999\n')

user_account = {}
print ("\n KARSHA BANK \n")

#=================LOG-IN SYSTEM=======================#

print("1.Admin Login")
print("2.Customer Login")
choice = input ("choose a Number between 1 and 2 : ")
try:
    if choice == '1':
        print("adminid = A000  admin password = 1999")
        max_attempts = 5
        attempt = 0
        
        logged_in = False

        while attempt < max_attempts:
            print("\n==== Admin Login ====")
            admin_id = input("Enter Admin ID: ")
            admin_password = input("Enter Admin Password: ")

            with open('Admin.txt', 'r') as file:
                for line in file:
                    admin_data = line.strip().split(',')
                    if admin_data[0] == admin_id and admin_data[1] == admin_password:
                        print("\nLogin successful😊")
                        logged_in = True
                        break  

            if logged_in:
                break 
            else:
                attempt += 1
                print(f"\nLogin failed... {max_attempts - attempt} attempts remaining😞\n")

        if not logged_in:
            print("You have been locked out due to too many failed login attempts.")
            exit()
        #=== MAIN LOBBY FOR ADMIN ===#
        while True:
            print ("\n=== MINI BANK SYSTEM ===\n")
            print ("1.create Account")
            print ("2.Deposit Money")
            print ("3.Withdraw Money")
            print ("4.Check Balance")
            print ("5.Transaction History")
            print ('6.Add New Admin')
            print ("7.Exit")

            choice = input ("Enter a Number between 1 to 7 : ")
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
                    # if result:
                    #     user_id, balance = result
                    #     user_account[user_id] = {'balance': balance}
                    #     with open("transaction.txt", 'a') as file:
                    #         file.write(f'{user_id} deposit amount: {amount} balance: {balance}\n')

                elif choice == '3':
                    datetimeprinter()
                    result = withdraw()
                    # if result:
                    #     user_id, balance = result
                    #     user_account[user_id] = {'balance': balance}
                    #     with open("transaction.txt", 'a') as file:
                    #         file.write(f'{user_id} Withdrawal amount: {amount} balance: {balance}\n')

                        
                elif choice == '4':
                    account_balance_check()
                elif choice == '5':
                    user_id = input ('Enter Your User ID: ')
                    try:
                        print("================================================================================================")
                        print("                      DATE & TIME         |    USER_ID   |       TYPE            |   AMOUNT    |")
                        print('================================================================================================')
                        file = open ('transaction.txt', 'r')
                        for line in file:
                            user_data = line.strip().split('\t')
                            # print (user_data)
                            if user_data[2] == user_id :
                                print (f'{user_data[0]}--{user_data[1]}\t {user_data[2]}\t {user_data[3]}\t {user_data[4]}' )
                        print("================================================================================================")
                    except FileNotFoundError:
                        print ('Transaction File Not Found')
                elif choice == "6":
                    generator = customer_id_generation('A', 'Admin_counter.txt')
                    new_admin_id = generator()
                    password = input ('Enter Admin Password: ')
                    with open ('Admin.txt', 'a') as file:
                        file.write (f'{new_admin_id},{password}\n')
                        print(f'New Admin ID:{new_admin_id}')
                        print(f"Admin password:{password}")
                elif choice == '7':
                    print ("Thank You For Using Our Bank Service💖")
                    break
                else:
                    print ("❌invalid Number...select a number between 1 to 6 ")
            except ValueError:
                print ('Choice should be in Number')


    elif choice == '2':
        #== MAIN LOBBY FOR CUSTOMER ==#
        while True:
            print('1. Check balance')
            print('2. Deposit Money')
            print('3. Withdraw Money')
            print('4. Exit')

            print('\n')
            choice = input('Choose a Number Between 1 to 4: ')
            try:
                if choice == '1':
                    account_balance_check()
                elif choice == '2':
                    datetimeprinter()
                    result = deposit()
                    # if result:
                    #     user_id, balance = result
                    #     user_account[user_id] = {'balance': balance}
                    #     with open("transaction.txt", 'a') as file:
                    #         file.write(f'{user_id} Deposit amount: {amount} balance: {balance}\n')
                elif choice == '3':
                    datetimeprinter()
                    result = withdraw()

                elif choice == '4':
                    print ('Thank You For Using Our Bank Service💖')
                    break
                else:
                    print ("Invalid Number... Select a Number Between 1 to 4")  
            except ValueError:
                    print ('Choice should be in Number')
except ValueError:
                    print ('Choice should be in Number')











