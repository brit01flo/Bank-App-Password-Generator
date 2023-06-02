
# import os 

# def make_noise():
#     '''Make noise after finishing executing a code'''
#     duration = 1  # seconds
#     freq = 440  # Hz
#     os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))



# def main():
#     even_arr = []
#     for i in range(10000):
#         if i%2==0:
#             even_arr.append(i)
#     make_noise()

# if __name__=='__main__':
#     main()


# from knockknock import slack_sender

# webhook_url = "webhook_url_to_your_slack_room"

# @slack_sender(webhook_url=webhook_url, channel="<your_favorite_slack_channel>", user_mentions=["<your_slack_id>", "<grandma's_slack_id>"])
# def main():
#     even_arr = []
#     for i in range(10000):
#         if i%2==0:
#             even_arr.append(i)


import os 

def make_noise():
    '''Make noise after finishing executing a code'''
    duration = 1  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

if __name__=='__main__':
    make_noise()
import pyautogui as pag
pag.alert(text="Hello World", title="The Hello World Box")

# pag.countdown

# Imports
# import tkinter
# from tkinter import messagebox

# # This code is to hide the main tkinter window
# root = tkinter.Tk()
# root.withdraw()

# # Message Box
# messagebox.showinfo("Account No", "Account No does not exist")

from tkinter import Label, Tk, mainloop

root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
greeting = Label(root, text="Hello, Tkinter")
greeting.place(3,3)
mainloop()