from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Label
from Deposit.deposit import deposit
from Balance.balance import balance
from Withdrawal.withdrawal import withdraw
from Payment.payment import pay_someone
from SignUp.SignUp import sign_up
from SignIn.SignIn import sign_in
from Transactions.transactions import transactions
import pyautogui as pag

OUTPUT_PATH = Path(__file__).parent
BALANCE_PATH = OUTPUT_PATH / Path(r"./Balance/balance_images/frame0")
DEPOSIT_PATH = OUTPUT_PATH / Path(r"./Deposit/deposit_images/frame0")
WITHDRAWAL_PATH = OUTPUT_PATH / Path(r"./Withdrawal/withdrawal_images/frame0")
BALANCE_PATH = OUTPUT_PATH / Path(r"./Balance/balance_images/frame0")
TRANSACTION_PATH = OUTPUT_PATH / Path(r"./Transactions/transaction_images/frame0")
PAYMENT_PATH = OUTPUT_PATH / Path(r"./Payment/payment_images/frame0")
SIGN_IN_PATH = OUTPUT_PATH / Path(r"./SignIn/frame0")
SIGN_UP_PATH = OUTPUT_PATH / Path(r"./SignUp/frame1")
EMAIL = 'mphela@gmail.com'

def relative_to_balance(path: str) -> Path:
    return BALANCE_PATH / Path(path)


def relative_to_deposit(path: str) -> Path:
    return DEPOSIT_PATH / Path(path)


def relative_to_payment(path: str) -> Path:
    return PAYMENT_PATH / Path(path)


def relative_to_withdrawal(path: str) -> Path:
    return WITHDRAWAL_PATH / Path(path)


def relative_to_transactions(path: str) -> Path:
    return TRANSACTION_PATH / Path(path)


def relative_to_sign_in(path: str) -> Path:
    return SIGN_IN_PATH / Path(path)


def relative_to_assets(path: str) -> Path:
    return SIGN_UP_PATH / Path(path)

window = Tk()

window.geometry("1297x618")
window.configure(bg = "#7A8EC0")

""" ************************************************
                DECLARE FRAME
************************************************ """

# Balance Frame
balance_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Deposit Frame
deposit_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Payment Frame
payment_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Withdrawal Frame
withdrawal_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Transaction Frame
transaction_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Sign In Frame
sign_in_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Sign Up Frame
sign_up_canvas = Canvas(
    window,
    bg = "#7A8EC0",
    height = 618,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

""" ************************************************
                CHANGE FRAMES
************************************************ """

def to_deposit():
    deposit_canvas.place(x = 0, y = 0)
    withdrawal_canvas.place_forget()
    transaction_canvas.place_forget()
    payment_canvas.place_forget()
    balance_canvas.place_forget()
    sign_in_canvas.place_forget()
    sign_up_canvas.place_forget()


def to_withdrawal():
    deposit_canvas.place_forget()
    withdrawal_canvas.place(x = 0, y = 0)
    transaction_canvas.place_forget()
    payment_canvas.place_forget()
    balance_canvas.place_forget()
    sign_in_canvas.place_forget()
    sign_up_canvas.place_forget()


def to_transactions():
    deposit_canvas.place_forget()
    withdrawal_canvas.place_forget()
    transaction_canvas.place(x = 0, y = 0)
    payment_canvas.place_forget()
    balance_canvas.place_forget()
    sign_in_canvas.place_forget()
    sign_up_canvas.place_forget()
    _transactions()


def to_payment():
    deposit_canvas.place_forget()
    withdrawal_canvas.place_forget()
    transaction_canvas.place_forget()
    payment_canvas.place(x = 0, y = 0)
    balance_canvas.place_forget()
    sign_in_canvas.place_forget()
    sign_up_canvas.place_forget()


def to_balance():
    deposit_canvas.place_forget()
    withdrawal_canvas.place_forget()
    transaction_canvas.place_forget()
    payment_canvas.place_forget()
    balance_canvas.place(x = 0, y = 0)
    sign_in_canvas.place_forget()
    sign_up_canvas.place_forget()
    _balance()

def to_sign_in():
    deposit_canvas.place_forget()
    withdrawal_canvas.place_forget()
    transaction_canvas.place_forget()
    payment_canvas.place_forget()
    balance_canvas.place_forget()
    sign_in_canvas.place(x = 0, y = 0)
    sign_up_canvas.place_forget()


def to_sign_up():
    deposit_canvas.place_forget()
    withdrawal_canvas.place_forget()
    transaction_canvas.place_forget()
    payment_canvas.place_forget()
    balance_canvas.place_forget()
    sign_in_canvas.place_forget()
    sign_up_canvas.place(x = 0, y = 0)



""" ************************************************
                SIGN IN 
************************************************ """
def _sign_in():
    email =  sign_in_entry_2.get()
    password =  sign_in_entry_1.get()
    if(sign_in(email, password)):
        to_balance()
    

sign_in_image_image_1 = PhotoImage(
    file=relative_to_sign_in("image_1.png"))
sign_in_canvas.create_image(
    991.0,
    422.0,
    image=sign_in_image_image_1
)

sign_in_image_image_2 = PhotoImage(
    file=relative_to_sign_in("image_2.png"))
sign_in_canvas.create_image(
    764.0,
    323.0,
    image=sign_in_image_image_2
)

sign_in_image_image_3 = PhotoImage(
    file=relative_to_sign_in("image_3.png"))
sign_in_canvas.create_image(
    960.0,
    476.0,
    image=sign_in_image_image_3
)

sign_in_button_image_1 = PhotoImage(
    file=relative_to_sign_in("button_1.png"))
sign_in_button_1 = Button(
    sign_in_canvas,
    image=sign_in_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=_sign_in,
    relief="flat"
)
sign_in_button_1.place(
    x=739.0,
    y=386.0,
    width=466.0,
    height=43.0
)

sign_in_image_image_4 = PhotoImage(
    file=relative_to_sign_in("image_4.png"))
sign_in_canvas.create_image(
    765.0,
    246.0,
    image=sign_in_image_image_4
)

sign_in_image_image_5 = PhotoImage(
    file=relative_to_sign_in("image_5.png"))
sign_in_canvas.create_image(
    330.0,
    309.0,
    image=sign_in_image_image_5
)

sign_in_button_image_2 = PhotoImage(
    file=relative_to_sign_in("button_2.png"))
sign_in_button_2 = Button(
    sign_in_canvas,
    image=sign_in_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_up,
    relief="flat"
)
sign_in_button_2.place(
    x=997.0,
    y=464.0,
    width=69.0,
    height=23.0
)

sign_in_canvas.create_text(
    809.0,
    464.0,
    anchor="nw",
    text="Don’t have an account? ",
    fill="#FFF0F0",
    font=("Inter Regular", 15 * -1)
)

sign_in_canvas.create_text(
    836.0,
    93.0,
    anchor="nw",
    text="Sign In",
    fill="#FFFFFF",
    font=("Inter Bold", 74 * -1)
)

sign_in_canvas.create_text(
    739.0,
    275.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_in_canvas.create_text(
    741.0,
    198.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_in_entry_image_1 = PhotoImage(
    file=relative_to_sign_in("entry_1.png"))
sign_in_canvas.create_image(
    997.0,
    323.0,
    image=sign_in_entry_image_1
)
sign_in_entry_1 = Entry(
    sign_in_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_in_entry_1.place(
    x=790.0,
    y=302.0,
    width=414.0,
    height=40.0
)

sign_in_entry_image_2 = PhotoImage(
    file=relative_to_sign_in("entry_2.png"))
sign_in_canvas.create_image(
    997.0,
    246.0,
    image=sign_in_entry_image_2
)
sign_in_entry_2 = Entry(
    sign_in_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_in_entry_2.place(
    x=789.0,
    y=225.0,
    width=416.0,
    height=40.0
)

sign_in_canvas.place(x = 0, y = 0)
# balance_canvas.place(x=0, y=0)

""" ************************************************
                DEPOSIT 
************************************************ """
def _deposit():
    amount = deposit_entry_1.get()
    if messagebox.askquestion("Confirm", f"Confirm the deposit, R{amount}.00?") == "yes":
        deposit( sign_in_entry_2.get(), amount)
        _balance()
        ...


payment_image_image_6 = PhotoImage(
    file=relative_to_payment("image_6.png"))
deposit_canvas.create_image(
    296.0,
    309.0,
    image=payment_image_image_6
)


deposit_canvas.create_rectangle(
    593.0,
    0.0,
    1297.0,
    618.0,
    fill="#7A8EC0",
    outline="")

deposit_button_image_1 = PhotoImage(
    file=relative_to_deposit("button_1.png"))
deposit_button_1 = Button(
    deposit_canvas,
    image=deposit_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
deposit_button_1.place(
    x=1082.0,
    y=10.0,
    width=152.0,
    height=62.0
)

deposit_image_image_1 = PhotoImage(
    file=relative_to_deposit("image_1.png"))
deposit_canvas.create_image(
    950.0,
    218.0,
    image=deposit_image_image_1
)

deposit_image_image_2 = PhotoImage(
    file=relative_to_deposit("image_2.png"))
deposit_canvas.create_image(
    716.0,
    206.0,
    image=deposit_image_image_2
)

deposit_entry_image_1 = PhotoImage(
    file=relative_to_deposit("entry_1.png"))
deposit_canvas.create_image(
    798.0,
    206.5,
    image=deposit_entry_image_1
)
deposit_entry_1 = Entry(
    deposit_canvas,
    bd=0,
    bg="#99A0C7",
    fg="#FFFFFF",
    highlightthickness=0
)
deposit_entry_1.place(
    x=720.0,
    y=186.0,
    width=156.0,
    height=39.0
)

deposit_image_image_3 = PhotoImage(
    file=relative_to_deposit("image_3.png"))
deposit_canvas.create_image(
    615.0,
    218.0,
    image=deposit_image_image_3
)

deposit_button_image_2 = PhotoImage(
    file=relative_to_deposit("button_2.png"))
deposit_button_2 = Button(
    deposit_canvas,
    image=deposit_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=_deposit,
    relief="flat"
)
deposit_button_2.place(
    x=713.0,
    y=250.0,
    width=104.0,
    height=36.0
)

deposit_canvas.create_text(
    679.0,
    150.0,
    anchor="nw",
    text="Amount",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

deposit_canvas.create_text(
    683.0,
    192.0,
    anchor="nw",
    text="R",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

deposit_image_image_5 = PhotoImage(
    file=relative_to_balance("image_2.png"))
deposit_canvas.create_image(
    1097.0,
    437.0,
    image=deposit_image_image_5
)

deposit_image_image_6 = PhotoImage(
    file=relative_to_balance("image_4.png"))
deposit_canvas.create_image(
    750.0,
    438.0,
    image=deposit_image_image_6
)

deposit_image_image_7 = PhotoImage(
    file=relative_to_balance("image_5.png"))
deposit_canvas.create_image(
    926.0,
    444.0,
    image=deposit_image_image_7
)

deposit_image_image_8 = PhotoImage(
    file=relative_to_balance("image_6.png"))
deposit_canvas.create_image(
    1269.0,
    438.0,
    image=deposit_image_image_8
)

deposit_button_image_3 = PhotoImage(
    file=relative_to_deposit("button_3.png"))
deposit_button_3 = Button(
    deposit_canvas,
    image=deposit_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_balance,
    relief="flat"
)
deposit_button_3.place(
    x=671.0,
    y=505.0,
    width=117.0,
    height=100.0
)

deposit_button_image_4 = PhotoImage(
    file=relative_to_deposit("button_4.png"))
deposit_button_4 = Button(
    deposit_canvas,
    image=deposit_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=to_withdrawal,
    relief="flat"
)
deposit_button_4.place(
    x=817.0,
    y=393.0,
    width=117.0,
    height=100.0
)

deposit_button_image_5 = PhotoImage(
    file=relative_to_deposit("button_5.png"))
deposit_button_5 = Button(
    deposit_canvas,
    image=deposit_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
deposit_button_5.place(
    x=965.0,
    y=393.0,
    width=117.0,
    height=100.0
)

deposit_button_image_6 = PhotoImage(
    file=relative_to_deposit("button_6.png"))
deposit_button_6 = Button(
    deposit_canvas,
    image=deposit_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=to_payment,
    relief="flat"
)
deposit_button_6.place(
    x=669.0,
    y=393.0,
    width=117.0,
    height=100.0
)

deposit_button_image_7 = PhotoImage(
    file=relative_to_deposit("button_7.png"))
deposit_button_7 = Button(
    deposit_canvas,
    image=deposit_button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=to_transactions,
    relief="flat"
)
deposit_button_7.place(
    x=1113.0,
    y=393.0,
    width=117.0,
    height=100.0
)

deposit_image_image_71 = PhotoImage(
    file=relative_to_balance("image_7.png"))
deposit_canvas.create_image(
    296.0,
    309.0,
    image=deposit_image_image_71
)

""" ************************************************
                WITHDRAWAL 
************************************************ """
def _withdraw():
    amount = withdrawal_entry_1.get()
    if(not amount.isdigit() or not amount.isnumeric()):
        messagebox.showinfo("Warning", "Please enter a number.")
        return
    if messagebox.askquestion("message", f"Confirm withdrawal. R{amount}.00?") == "yes":
        if(withdraw(sign_in_entry_2.get(),amount)):
            _balance()


withdrawal_canvas.create_rectangle(
    593.0,
    0.0,
    1297.0,
    618.0,
    fill="#7A8EC0",
    outline="")

withdrawal_image_image_1 = PhotoImage(
    file=relative_to_withdrawal("image_1.png"))
withdrawal_canvas.create_image(
    950.0,
    218.0,
    image=withdrawal_image_image_1
)

withdrawal_image_image_2 = PhotoImage(
    file=relative_to_withdrawal("image_2.png"))
withdrawal_canvas.create_image(
    716.0,
    206.0,
    image=withdrawal_image_image_2
)

withdrawal_entry_image_1 = PhotoImage(
    file=relative_to_withdrawal("entry_1.png"))
withdrawal_canvas.create_image(
    798.0,
    206.5,
    image=withdrawal_entry_image_1
)
withdrawal_entry_1 = Entry(
    withdrawal_canvas,
    bd=0,
    
    font='#FFFFFF',
    bg="#99A0C7",
    fg="#FFFFFF",
    highlightthickness=0
)
withdrawal_entry_1.place(
    x=720.0,
    y=186.0,
    width=156.0,
    height=39.0
)

withdrawal_canvas.create_text(
    679.0,
    150.0,
    anchor="nw",
    text="Amount",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

withdrawal_canvas.create_text(
    683.0,
    192.0,
    anchor="nw",
    text="R",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

withdrawal_image_image_3 = PhotoImage(
    file=relative_to_withdrawal("image_3.png"))
withdrawal_canvas.create_image(
    615.0,
    218.0,
    image=withdrawal_image_image_3
)

withdrawal_image_image_5 = PhotoImage(
    file=relative_to_balance("image_2.png"))
withdrawal_canvas.create_image(
    1097.0,
    437.0,
    image=withdrawal_image_image_5
)

withdrawal_image_image_6 = PhotoImage(
    file=relative_to_balance("image_4.png"))
withdrawal_canvas.create_image(
    750.0,
    438.0,
    image=withdrawal_image_image_6
)

withdrawal_image_image_7 = PhotoImage(
    file=relative_to_balance("image_5.png"))
withdrawal_canvas.create_image(
    926.0,
    444.0,
    image=withdrawal_image_image_7
)

withdrawal_image_image_8 = PhotoImage(
    file=relative_to_balance("image_6.png"))
withdrawal_canvas.create_image(
    1269.0,
    438.0,
    image=withdrawal_image_image_8
)

withdrawal_button_image_1 = PhotoImage(
    file=relative_to_withdrawal("button_1.png"))
withdrawal_button_1 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=_withdraw,
    relief="flat"
)
withdrawal_button_1.place(
    x=713.0,
    y=250.0,
    width=104.0,
    height=36.0
)

withdrawal_button_image_2 = PhotoImage(
    file=relative_to_withdrawal("button_2.png"))
withdrawal_button_2 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
withdrawal_button_2.place(
    x=1082.0,
    y=10.0,
    width=152.0,
    height=62.0
)

withdrawal_button_image_3 = PhotoImage(
    file=relative_to_withdrawal("button_3.png"))
withdrawal_button_3 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_deposit,
    relief="flat"
)
withdrawal_button_3.place(
    x=965.0,
    y=393.0,
    width=117.0,
    height=100.0
)

withdrawal_button_image_4 = PhotoImage(
    file=relative_to_withdrawal("button_4.png"))
withdrawal_button_4 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("withdrawal"),
    relief="flat"
)
withdrawal_button_4.place(
    x=814.0,
    y=393.0,
    width=120.0,
    height=100.0
)

withdrawal_button_image_5 = PhotoImage(
    file=relative_to_withdrawal("button_5.png"))
withdrawal_button_5 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=to_payment,
    relief="flat"
)
withdrawal_button_5.place(
    x=669.0,
    y=393.0,
    width=117.0,
    height=100.0
)

withdrawal_button_image_6 = PhotoImage(
    file=relative_to_withdrawal("button_6.png"))
withdrawal_button_6 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=to_transactions,
    relief="flat"
)
withdrawal_button_6.place(
    x=1110.0,
    y=393.0,
    width=117.0,
    height=100.0
)

withdrawal_button_image_7 = PhotoImage(
    file=relative_to_withdrawal("button_7.png"))
withdrawal_button_7 = Button(
    withdrawal_canvas,
    image=withdrawal_button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=to_balance,
    relief="flat"
)
withdrawal_button_7.place(
    x=669.0,
    y=504.0,
    width=117.0,
    height=100.0
)

withdrawal_image_image_9 = PhotoImage(
    file=relative_to_withdrawal("image_9.png"))
withdrawal_canvas.create_image(
    296.0,
    309.0,
    image=withdrawal_image_image_9
)

""" ************************************************
                TRANSACRIONS 
************************************************ """
def _transactions():
    transaction =  transactions()
    temp_l = []
    if len(transaction) > 4:
        temp_l = transaction[-4:].copy()
        print(temp_l)
    x_choord=0
    y_choord=0
    for i, item in enumerate(temp_l):
        transaction_amount = Label(
            transaction_canvas,
            text=item,
            bg='#E729DF',
            font=("inter", 12),
            fg='white',
        )
        transaction_amount.place(x=699.0, y=151.0+ y_choord)
        y_choord += 22
        x_choord += 1
        if(x_choord > 5):
            break


transaction_canvas.create_rectangle(
    593.0,
    0.0,
    1297.0,
    618.0,
    fill="#7A8EC0",
    outline="")

transaction_image_image_1 = PhotoImage(
    file=relative_to_transactions("image_1.png"))
transaction_canvas.create_image(
    296.0,
    309.0,
    image=transaction_image_image_1
)

transaction_button_image_1 = PhotoImage(
    file=relative_to_transactions("button_1.png"))
transaction_button_1 = Button(
    transaction_canvas,
    image=transaction_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
transaction_button_1.place(
    x=1082.0,
    y=10.0,
    width=152.0,
    height=62.0
)

transaction_image_image_2 = PhotoImage(
    file=relative_to_transactions("image_2.png"))
transaction_canvas.create_image(
    615.0,
    218.0,
    image=transaction_image_image_2
)

transaction_image_image_3 = PhotoImage(
    file=relative_to_transactions("image_3.png"))
transaction_canvas.create_image(
    950.0,
    218.0,
    image=transaction_image_image_3
)

transaction_image_image_4 = PhotoImage(
    file=relative_to_transactions("image_4.png"))
transaction_canvas.create_image(
    1101.0,
    440.0,
    image=transaction_image_image_4
)

transaction_image_image_5 = PhotoImage(
    file=relative_to_transactions("image_5.png"))
transaction_canvas.create_image(
    750.0,
    433.0,
    image=transaction_image_image_5
)

transaction_image_image_6 = PhotoImage(
    file=relative_to_transactions("image_6.png"))
transaction_canvas.create_image(
    926.0,
    439.0,
    image=transaction_image_image_6
)

transaction_image_image_7 = PhotoImage(
    file=relative_to_transactions("image_7.png"))
transaction_canvas.create_image(
    1269.0,
    433.0,
    image=transaction_image_image_7
)

transaction_button_image_2 = PhotoImage(
    file=relative_to_transactions("button_2.png"))
transaction_button_2 = Button(
    transaction_canvas,
    image=transaction_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Transactions"),
    relief="flat"
)
transaction_button_2.place(
    x=1113.0,
    y=393.0,
    width=117.0,
    height=100.0
)

transaction_button_image_3 = PhotoImage(
    file=relative_to_transactions("button_3.png"))
transaction_button_3 = Button(
    transaction_canvas,
    image=transaction_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_deposit,
    relief="flat"
)
transaction_button_3.place(
    x=965.0,
    y=393.0,
    width=117.0,
    height=100.0
)

transaction_button_image_4 = PhotoImage(
    file=relative_to_transactions("button_4.png"))
transaction_button_4 = Button(
    transaction_canvas,
    image=transaction_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=to_withdrawal,
    relief="flat"
)
transaction_button_4.place(
    x=817.0,
    y=393.0,
    width=117.0,
    height=100.0
)

transaction_button_image_5 = PhotoImage(
    file=relative_to_transactions("button_5.png"))
transaction_button_5 = Button(
    transaction_canvas,
    image=transaction_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=to_payment,
    relief="flat"
)
transaction_button_5.place(
    x=669.0,
    y=393.0,
    width=117.0,
    height=100.0
)

transaction_button_image_6 = PhotoImage(
    file=relative_to_transactions("button_6.png"))
transaction_button_6 = Button(
    transaction_canvas,
    image=transaction_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=to_balance,
    relief="flat"
)
transaction_button_6.place(
    x=671.0,
    y=505.0,
    width=117.0,
    height=100.0
)

""" ************************************************
                PAYMENT 
************************************************ """
def _payment():
    amount_to_transfer = payment_entry_1.get().strip()
    account_no = payment_entry_2.get().strip()
    
    print(account_no, amount_to_transfer)
    pay_someone(sign_in_entry_2.get(),account_no,amount_to_transfer)


payment_canvas.create_rectangle(
    593.0,
    0.0,
    1297.0,
    618.0,
    fill="#7A8EC0",
    outline="")

payment_image_image_1 = PhotoImage(
    file=relative_to_payment("image_1.png"))
payment_canvas.create_image(
    615.0,
    218.0,
    image=payment_image_image_1
)

payment_image_image_7 = PhotoImage(
    file=relative_to_payment("image_7.png"))
payment_canvas.create_image(
    950.0,
    218.0,
    image=payment_image_image_7
)


payment_image_image_2 = PhotoImage(
    file=relative_to_balance("image_2.png"))
payment_canvas.create_image(
    1097.0,
    437.0,
    image=payment_image_image_2
)

payment_image_image_3 = PhotoImage(
    file=relative_to_balance("image_4.png"))
payment_canvas.create_image(
    750.0,
    438.0,
    image=payment_image_image_3
)

payment_image_image_4 = PhotoImage(
    file=relative_to_balance("image_5.png"))
payment_canvas.create_image(
    926.0,
    444.0,
    image=payment_image_image_4
)

payment_image_image_5 = PhotoImage(
    file=relative_to_balance("image_6.png"))
payment_canvas.create_image(
    1269.0,
    438.0,
    image=payment_image_image_5
)

payment_button_image_1 = PhotoImage(
    file=relative_to_payment("button_1.png"))
payment_button_1 = Button(
    payment_canvas,
    image=payment_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
payment_button_1.place(
    x=1082.0,
    y=10.0,
    width=152.0,
    height=62.0
)

payment_button_image_2 = PhotoImage(
    file=relative_to_payment("button_2.png"))
payment_button_2 = Button(
    payment_canvas,
    image=payment_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_deposit,
    relief="flat"
)
payment_button_2.place(
    x=965.0,
    y=393.0,
    width=117.0,
    height=100.0
)

payment_button_image_3 = PhotoImage(
    file=relative_to_payment("button_3.png"))
payment_button_3 = Button(
    payment_canvas,
    image=payment_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_withdrawal,
    relief="flat"
)
payment_button_3.place(
    x=814.0,
    y=393.0,
    width=120.0,
    height=100.0
)

payment_button_image_4 = PhotoImage(
    file=relative_to_payment("button_4.png"))
payment_button_4 = Button(
    payment_canvas,
    image=payment_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Payment"),
    relief="flat"
)
payment_button_4.place(
    x=669.0,
    y=393.0,
    width=117.0,
    height=100.0
)

payment_button_image_5 = PhotoImage(
    file=relative_to_payment("button_5.png"))
payment_button_5 = Button(
    payment_canvas,
    image=payment_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=to_transactions,
    relief="flat"
)
payment_button_5.place(
    x=1110.0,
    y=393.0,
    width=117.0,
    height=100.0
)

payment_button_image_6 = PhotoImage(
    file=relative_to_payment("button_6.png"))
payment_button_6 = Button(
    payment_canvas,
    image=payment_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=to_balance,
    relief="flat"
)
payment_button_6.place(
    x=669.0,
    y=504.0,
    width=117.0,
    height=100.0
)

payment_image_image_6 = PhotoImage(
    file=relative_to_payment("image_6.png"))
payment_canvas.create_image(
    296.0,
    309.0,
    image=payment_image_image_6
)

payment_canvas.create_text(
    690.0,
    226.0,
    anchor="nw",
    text="R",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

payment_entry_image_1 = PhotoImage(
    file=relative_to_payment("entry_1.png"))
payment_canvas.create_image(
    799.0,
    239.5,
    image=payment_entry_image_1
)
payment_entry_1 = Entry(
    payment_canvas,
    bd=0,
    bg="#99A0C7",
    fg="#FFFFFF",
    highlightthickness=0
)
payment_entry_1.place(
    x=722.0,
    y=219.0,
    width=154.0,
    height=39.0
)

payment_image_image_8 = PhotoImage(
    file=relative_to_payment("image_8.png"))
payment_canvas.create_image(
    717.0,
    239.0,
    image=payment_image_image_8
)

payment_canvas.create_text(
    711.0,
    190.0,
    anchor="nw",
    text="Amount",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

payment_canvas.create_text(
    713.0,
    117.0,
    anchor="nw",
    text="Account no",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

payment_entry_image_2 = PhotoImage(
    file=relative_to_payment("entry_2.png"))
payment_canvas.create_image(
    796.5,
    165.5,
    image=payment_entry_image_2
)
payment_entry_2 = Entry(
    payment_canvas,
    bd=0,
    bg="#99A0C7",
    fg="#FFFFFF",
    highlightthickness=0
)
payment_entry_2.place(
    x=720.0,
    y=145.0,
    width=153.0,
    height=39.0
)

payment_button_image_7 = PhotoImage(
    file=relative_to_payment("button_7.png"))
payment_button_7 = Button(
    payment_canvas,
    image=payment_button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=_payment,
    relief="flat"
)
payment_button_7.place(
    x=716.0,
    y=275.0,
    width=104.0,
    height=36.0
)

payment_image_image_9 = PhotoImage(
    file=relative_to_payment("image_9.png"))
payment_canvas.create_image(
    715.0,
    165.0,
    image=payment_image_image_9
)

""" ************************************************
                BALANCE 
************************************************ """
def _balance():
    balance_amount['text'] = balance(sign_in_entry_2.get())


balance_canvas.create_rectangle(
    593.0,
    0.0,
    1297.0,
    618.0,
    fill="#7A8EC0",
    outline="")
balance_button_image_1 = PhotoImage(
    file=relative_to_balance("button_1.png"))
balance_button_1 = Button(
    balance_canvas,
    image=balance_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
balance_button_1.place(
    x=1082.0,
    y=10.0,
    width=152.0,
    height=62.0
)

balance_image_image_1 = PhotoImage(
    file=relative_to_balance("image_1.png"))
balance_canvas.create_image(
    950.0,
    218.0,
    image=balance_image_image_1
)

balance_amount = Label(
    balance_canvas,
    text=sign_in_entry_2["text"],
    bg='#E729DF',
    font=("inter Extra bold", 25),
    fg='white',
)
balance_amount.place(x=730.0, y=273.0)

balance_image_image_2 = PhotoImage(
    file=relative_to_balance("image_2.png"))
balance_canvas.create_image(
    1097.0,
    437.0,
    image=balance_image_image_2
)

balance_image_image_3 = PhotoImage(
    file=relative_to_balance("image_3.png"))
balance_canvas.create_image(
    615.0,
    218.0,
    image=balance_image_image_3
)

balance_image_image_4 = PhotoImage(
    file=relative_to_balance("image_4.png"))
balance_canvas.create_image(
    750.0,
    438.0,
    image=balance_image_image_4
)

balance_image_image_5 = PhotoImage(
    file=relative_to_balance("image_5.png"))
balance_canvas.create_image(
    926.0,
    444.0,
    image=balance_image_image_5
)

balance_image_image_6 = PhotoImage(
    file=relative_to_balance("image_6.png"))
balance_canvas.create_image(
    1269.0,
    438.0,
    image=balance_image_image_6
)

balance_button_image_2 = PhotoImage(
    file=relative_to_balance("button_2.png"))
balance_button_2 = Button(
    balance_canvas,
    image=balance_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_withdrawal,
    relief="flat"
)
balance_button_2.place(
    x=817.0,
    y=393.0,
    width=117.0,
    height=100.0
)

balance_button_image_3 = PhotoImage(
    file=relative_to_balance("button_3.png"))
balance_button_3 = Button(
    balance_canvas,
    image=balance_button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=to_payment,
    relief="flat"
)
balance_button_3.place(
    x=669.0,
    y=393.0,
    width=117.0,
    height=100.0
)

balance_button_image_4 = PhotoImage(
    file=relative_to_balance("button_4.png"))
balance_button_4 = Button(
    balance_canvas,
    image=balance_button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=to_deposit,
    relief="flat"
)
balance_button_4.place(
    x=965.0,
    y=393.0,
    width=117.0,
    height=100.0
)

balance_image_image_7 = PhotoImage(
    file=relative_to_balance("image_7.png"))
balance_canvas.create_image(
    296.0,
    309.0,
    image=balance_image_image_7
)

balance_button_image_5 = PhotoImage(
    file=relative_to_balance("button_5.png"))
balance_button_5 = Button(
    balance_canvas,
    image=balance_button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Balance"),
    relief="flat"
)
balance_button_5.place(
    x=670.0,
    y=505.0,
    width=117.0,
    height=100.0
)

balance_button_image_6 = PhotoImage(
    file=relative_to_balance("button_6.png"))
balance_button_6 = Button(
    balance_canvas,
    image=balance_button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=to_transactions,
    relief="flat"
)
balance_button_6.place(
    x=1117.0,
    y=393.0,
    width=117.0,
    height=100.0
)


""" ************************************************
                SIGN UP 
************************************************ """
def _sign_up():
    first_name =  sign_up_entry_4.get()
    last_name =  sign_up_entry_3.get()
    email =  sign_up_entry_2.get()
    password =  sign_up_entry_1.get()
    sign_up(first_name, last_name, email, password)


sign_up_image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
sign_up_canvas.create_image(
    991.0,
    417.0,
    image=sign_up_image_image_1
)

sign_up_image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
sign_up_canvas.create_image(
    764.0,
    430.0,
    image=sign_up_image_image_2
)

sign_up_image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
sign_up_canvas.create_image(
    960.0,
    544.0,
    image=sign_up_image_image_3
)

sign_up_button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
sign_up_button_1 = Button(
    sign_up_canvas,
    image=sign_up_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=_sign_up,
    relief="flat"
)
sign_up_button_1.place(
    x=741.0,
    y=473.0,
    width=466.0,
    height=43.0
)

sign_up_image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
sign_up_canvas.create_image(
    765.0,
    349.0,
    image=sign_up_image_image_4
)

sign_up_image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
sign_up_canvas.create_image(
    765.0,
    268.0,
    image=sign_up_image_image_5
)

sign_up_image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
sign_up_canvas.create_image(
    765.0,
    194.0,
    image=sign_up_image_image_6
)

sign_up_image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
sign_up_canvas.create_image(
    330.0,
    309.0,
    image=sign_up_image_image_7
)

sign_up_button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
sign_up_button_2 = Button(
    sign_up_canvas,
    image=sign_up_button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=to_sign_in,
    relief="flat"
)
sign_up_button_2.place(
    x=1009.0,
    y=532.0,
    width=69.0,
    height=23.0
)

sign_up_canvas.create_text(
    830.0,
    532.0,
    anchor="nw",
    text="have an account? ",
    fill="#FFF0F0",
    font=("Inter Regular", 15 * -1)
)

sign_up_canvas.create_text(
    824.0,
    48.0,
    anchor="nw",
    text="Sign Up",
    fill="#FFFFFF",
    font=("Inter Bold", 74 * -1)
)

sign_up_canvas.create_text(
    740.0,
    382.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_up_canvas.create_text(
    740.0,
    301.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_up_canvas.create_text(
    741.0,
    146.0,
    anchor="nw",
    text="First Name",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_up_canvas.create_text(
    740.0,
    220.0,
    anchor="nw",
    text="Last Name",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

sign_up_entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
sign_up_canvas.create_image(
    997.0,
    430.0,
    image=sign_up_entry_image_1
)
sign_up_entry_1 = Entry(
    sign_up_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_up_entry_1.place(
    x=790.0,
    y=409.0,
    width=414.0,
    height=40.0
)

sign_up_entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
sign_up_canvas.create_image(
    997.0,
    349.0,
    image=sign_up_entry_image_2
)
sign_up_entry_2 = Entry(
    sign_up_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_up_entry_2.place(
    x=789.0,
    y=328.0,
    width=416.0,
    height=40.0
)

sign_up_entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
sign_up_canvas.create_image(
    998.0,
    268.0,
    image=sign_up_entry_image_3
)
sign_up_entry_3 = Entry(
    sign_up_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_up_entry_3.place(
    x=790.0,
    y=247.0,
    width=416.0,
    height=40.0
)

sign_up_entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
sign_up_canvas.create_image(
    998.0,
    194.0,
    image=sign_up_entry_image_4
)
sign_up_entry_4 = Entry(
    sign_up_canvas,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
sign_up_entry_4.place(
    x=790.0,
    y=173.0,
    width=416.0,
    height=40.0
)


window.resizable(False, False)
window.mainloop()
