from common.common import get_user_being_paid, update, update_user_infor
import pyautogui as pag
from tkinter import messagebox
def pay_someone(email, account_no, amount_to_transfer):

    if(account_no == ""):
        messagebox.showerror("Error", "Please enter the account no!")
        return

    if(amount_to_transfer.isdigit() == False and amount_to_transfer.isnumeric() == False ):
        messagebox.showwarning("Warning", "Please enter the correct amount!")
        return

    user_being_paid, index_ = get_user_being_paid(account_no)

    if(user_being_paid is None or user_being_paid[0].strip() != account_no):
        messagebox.showerror("Error", f"The account no \'{account_no}\' does not exist. Please provide the correct account no.")
        return
    
    user, index, users = update(email)

    if((int(user[5].strip()) - int(amount_to_transfer) <= 0)):
        messagebox.showinfo("message", "You have insufficient funds.")
        return
    
    if(messagebox.askquestion("Confirm", "Press yes to confirm transactions.") == 'no'):
        return 
    my_new_balance = int(user[5].strip()) - int(amount_to_transfer)
    user[5] =  " " + str(my_new_balance) + '\n'
    users[index] = ",".join(user)


    their_new_balance = int(user_being_paid[5].strip()) + int(amount_to_transfer)
    user_being_paid[5] =  " " + str(their_new_balance) + '\n'
    users[index_] = ",".join(user_being_paid)

    update_user_infor(users)
    messagebox.showinfo("message", f"You have succefully transfered -R{amount_to_transfer} ✅ to the account {user_being_paid[0][:2]}*******{user_being_paid[0][9:]}")