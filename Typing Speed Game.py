from tkinter import *
from tkinter import messagebox
from words import word_list
import random

# Variables
HIT = 0
MISS = 0
COUNT = 0
SLIDERWORDS = ''
TIME = 60

# Functions
def headslider():
    global COUNT, SLIDERWORDS
    text = "Typing Speed Increaser Game"
    if(COUNT >= len(text)):
        COUNT = 0
        SLIDERWORDS = ''
    SLIDERWORDS += text[COUNT]
    COUNT += 1
    heading.config(text=SLIDERWORDS)
    heading.after(100, headslider)

def check(event):
    global HIT, MISS, TIME
    user_text = entry.get()

    if(user_text.upper() == word['text'].upper()):
        HIT += 1
        score_count.config(text=HIT)
        num = random.randint(0, len(word_list)-1)
        word.config(text=word_list[num])
        info.config(text='CORRECT', fg='green')
        if TIME == 60:
            timeCount()
    
    elif user_text != '':
        MISS += 1
        info.config(text='INCORRECT', fg='red')
    
    entry.delete(0, END)

def timeCount():
    global HIT, MISS, TIME
    if TIME>0:
        TIME -= 1
        time_count.config(text=TIME)
        time_count.after(1000, timeCount)
    else:
        info.config(text=f'Correct : {HIT}, Incorrect : {MISS}, Net Score : {HIT - MISS}', fg='black')
        retry = messagebox.askretrycancel("Game Over", "Do you want to Play Again?")
        if retry == True:
            HIT = 0
            MISS = 0
            TIME = 60
            word.config(text='START')
            score_count.config(text=HIT)
            time_count.config(text=TIME)
            info.config(text='Type the Word and Hit Enter')
            entry.delete(0, END)

        else:
            exit()

# Root Method
root = Tk()
root.geometry("600x600+400+100")
root.configure(bg='powder blue')
root.title('Typing Speed Game')
root.iconbitmap("images/Typing Speed Game Icon.ico")
root.resizable(False, False)

# Label Methods
heading = Label(root, text="", font=("Arial", 25, "bold"), bg="powder blue", fg="white", width='25')
heading.place(x=50, y=50)
headslider()

word = Label(root, text='START', font=("Arial", 20, "bold"), bg="powder blue", fg="white", width=20)
word.place(x=120, y=300)

score_text = Label(root, text="Score", font=("Arial", 15, "bold"), bg="powder blue", fg="green")
score_text.place(x=50, y=200)

score_count = Label(root, text=HIT, font=("Arial", 15), bg="powder blue", fg="white")
score_count.place(x=65, y=230)

time_text = Label(root, text="Time Left", font=("Arial", 15, "bold"), bg="powder blue", fg="red")
time_text.place(x=450, y=200)

time_count = Label(root, text=TIME, font=("Arial", 15), bg="powder blue", fg="white")
time_count.place(x=490, y=230)

info = Label(root, text='Type the Word and Hit Enter', font=("Arial", 15), bg="powder blue", fg="black", width=40)
info.place(x=70, y=400)

# entryVar = StringVar()
entry = Entry(root, font=("Arial", 15, "bold"), fg="powder blue", justify='center')
entry.place(x=180, y=350)
entry.focus_set()

# Binding ENTER Key with check function
root.bind('<Return>', check)

root.mainloop()