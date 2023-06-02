from common.common import  is_email, user_exist, add_new_account
from tkinter import messagebox
import random
def sign_up(first_name, last_name, email, password):
    if(first_name == "" or last_name == "" or email == "" or password == ""):
        messagebox.showerror("Error", f"Fill all the spaces")
        return False

    if(not is_email(email)):
        
        messagebox.showerror("Error", f"Invalid email")
        return False
    
    if(user_exist(email)):
        messagebox.showinfo("message", "Account with this email address exist")
        return False
    account = generateAccountNo()
    new_account = new_user(first_name, last_name, email, password, account)
    add_new_account(new_account)

    messagebox.showinfo('message', f'You successfully created a new account. Your account number is {account}')


def generateAccountNo():
    accountNo = '89'
    for i in range(10):
        accountNo += str(random.randrange(0, 9, 1))
    return accountNo

def new_user( name, surname, email, password, account):
    balance = 0
    return f"{account}, {name}, {surname}, {email}, {password}, {balance}"


