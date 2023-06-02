from common.common import update, update_user_infor, add_transaction, transaction
from tkinter import messagebox
import os
def withdraw(email, amount):
        
    if(amount.isdigit() and amount.isnumeric()):
        user, index, users = update(email)
        if(int(user[5].strip()) < int(amount) or int(user[5].strip()) <= 0):
            make_noise()
            messagebox.showwarning("Warning", "You have insufficient funds.")

        else:
            new_amount = str(int(user[5].strip()) - int(amount))
            user[5] =  " " + new_amount + '\n'
            users[index] = ",".join(user)
            update_user_infor(users)
            
            add_transaction(transaction(user[0], "Withdraw", amount))
            return True
    return False


def make_noise():
    '''Make noise after finishing executing a code'''
    duration = 1  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
