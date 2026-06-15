
balance = 0.0

def check_balance():
    global balance
    print()
    print("============================================")
    print(f"Your current balance is: {balance}")
    print("============================================")
    
    
def deposit(amount):
    global balance
    print()
    if amount > 0:
        print("============================================")
        balance += amount
        print(F"Succesfully Deposit. Toatl amount: {balance}")
        print("============================================")
    else:
        print("============================================")
        print("we cannot deposit. The amount are Negative! or Zero!")   
        print("============================================")
    
def withdraw(amount):
    global balance
    print()
    if amount <= 0:
        print("============================================")
        print("Insufficient funds")
        print("============================================")
    else:
        print("============================================")
        balance -= amount
        print(F"Succesfully Withdrawl. Toatl amount: {balance}")
        print("============================================")
    
    
if __name__ == "__main__":
    print()
    print("============================================")
    print("      Welcome to the 'ABC bank'   ")
    print("============================================")
    
    
    while True:
        print()
        print("============================================")
        print('1. Check your balance ') 
        print('2. Deposit the amount') 
        print('3. Withdraw the amount') 
        print('4. Quit') 
        print("============================================")
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1: 
            check_balance()
            print()
        elif choice == 2: 
            amount = float(input("Enter the amount to Deposit: "))
            deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to Withdrawl: "))
            withdraw(amount)
        elif choice == 4:
            print("Quiting, Have a nice day")
            break
        else:
            print("Invalid chioce, Try Again!") 
            

            
