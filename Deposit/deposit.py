from common.common import update_user_infor, add_new_account, user_exist, is_email, logged_in_user, update, fetch_user_infor, get_user_being_paid, add_transaction, get_transactions
import datetime


def deposit(email, amount):


        if(amount.isdigit() and amount.isnumeric()):
            
            user, index, users = update(email)
            new_amount = str(int(user[5].strip()) + int(amount))
            user[5] =  " " + new_amount + '\n'
            users[index] = ",".join(user)

            update_user_infor(users)
            add_transaction(transaction(user[0], "Deposited", amount))
            return True

def transaction(account, transaction_message, amount):
    current_date = datetime.datetime.now()
    return account +", "+ transaction_message + ", "+amount +", "+ str(current_date) +'\n'