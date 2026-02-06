import os
import json 

def load_account():
    if not os.path.exists("data.json"):
        return{}
    else:
        with open("data.json","r") as f:
            return json.load(f)
        
def save_account(accounts):
    with open("data.json","w") as f:
        json.dump(accounts,f,indent=4)


accounts=load_account()

while True:
    acc_no=(input("ENTER ACCOUNT.NO:"))

    if acc_no not in accounts:
        print("Creating A New Account...")
        name=input("ENTER NAME:").upper()
        pin=int(input("SET PIN:"))
        accounts[acc_no]= {
            "name":name,
            "pin":pin,
            "balance":0
        }
        save_account(accounts)

    else:    
        print(f"WELCOME BACK {accounts[acc_no]['name']}")
    
    option=input("WANT TO DEPOSIT(d) / WITHDRAW(w) / CHECK BALANCE(c) / EXIT(e) \n \t \t SELECT OPTION(d/w/c/e):").lower()    
    if(option=="d"):
        verify1=int(input('ENTER PIN:'))
        pin1=accounts[acc_no]["pin"]
        if(verify1!=pin1):
            print('INCORRECT PIN!')
        else:
            amount=int(input("ENTER DEPOSIT AMOUNT:"))
            accounts[acc_no]["balance"]+=amount
            print(" *** AMOUNT DEPOSITED *** ")
            save_account(accounts)
            print()

    elif(option=="w"):
        verify2=int(input("ENTER PIN:"))
        pin2=accounts[acc_no]["pin"]
        if(verify2!=pin2):
            print("INCORRECT PIN!")  
        else:
            amount=int(input("ENTER WITHDRAW AMOUNT:"))
            if(amount>accounts[acc_no]["balance"]):     
                print("INSUFFICIENT BALANCE")  
            else:
                accounts[acc_no]["balance"]-=amount
                save_account(accounts)
            print(" *** AMOUNT WITHDRAWN ***")
            print()

    elif(option=="c"):
        verify=int(input("ENTER PIN:"))
        pin=accounts[acc_no]["pin"]
        if(verify!=pin):
            print("INCORRECT PIN")
        else:
            print(f"ACCOUNT BALANCE: {accounts[acc_no]["balance"]}")
            print()  

    elif(option=="e"):
        print(f'THANK YOU {accounts[acc_no]["name"]}!') 
        break   

    else:    

        print("INVALID OPTION")

