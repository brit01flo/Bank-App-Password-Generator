import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def fetch_user_infor():
    with open('DataBase/user_info.txt', "r") as f:    
        _list = f.readlines()
        return _list


def add_new_account(new_account):
        
    with open("DataBase/user_info.txt","a") as f:
        f.write("\n")
        f.write(new_account) 


def is_email(email):
    
    if(re.fullmatch(regex, email)):
        return True
    return False


def user_exist(email):
    users = fetch_user_infor()
    for user in users:
        if email in user:
            return True
    return False


def get_user(users, email):
    for i, user in enumerate(users):
        if email in user:
            return user.strip().split(','), i
    return None


def logged_in_user(email):
    users = fetch_user_infor()
    for user in users:
        if email in user:
            return user.strip().split(',')
    return None


def get_user_being_paid(account_no):
    users = fetch_user_infor()
    for i, user in enumerate(users):
        if account_no in user:
            return user.strip().split(','), i
    return None, -1


def update(email):
    users = fetch_user_infor()
    user, index = get_user(users, email)
    print(user)
    return user, index, users


def update_user_infor(users):
    users = "".join(users)
    with open('DataBase/user_info.txt', "w") as f:    
        f.write(users)


def add_transaction(transaction):
    with open('DataBase/transactions.txt', "a") as f:    
        f.write(transaction)


def get_transactions():
    with open("DataBase/transactions.txt", "r") as f:
        _list = f.readlines()
        return _list


def transaction(account, transaction_message, amount):
    current_date = datetime.datetime.now()
    return account +", "+ transaction_message + ", "+amount +", "+ str(current_date) +'\n'
if __name__ == '__main__':
    print(logged_in_user())