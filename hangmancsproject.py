from tkinter import *
import csv
import random
from tkinter import messagebox


# function for storing rules from a file
def rulestext():
    with open(r'E:\projects\Hangman Game CS Project class 12\rules.txt') as f:
        return f.read()


# function to convert list to string
def lst_str(lst):  # only for words whose each letter is an element of list
    string = ''
    for char in lst:
        string += char
    return string


# function for choosing a random word for default game
def chooseword():
    with open(r'E:\projects\Hangman Game CS Project class 12\words.csv') as f:
        worddict = csv.DictReader(f)
        wordlist = []
        meaninglist = []
        for i in worddict:
            wordlist.append((i['WORDS']).lower())
            meaninglist.append(i['MEANINGS'])
    wordchosen = random.choice(wordlist)
    meaningchosen = meaninglist[wordlist.index(wordchosen)]
    return wordchosen, meaningchosen


# function for asking to replay the game
def wanttoplay():
    askplayagain = messagebox.askyesno('Game Over', 'Do you want to play again?')
    if askplayagain:
        return 'reset'
    else:
        return 'exit'


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.word = ''
        self.meaning = ''
        self.blankslist = list(len(self.word)*'-')  # list of blanks
        self.lives = 10
        self.ans = True
        self.guess_list = []
        self.GameType = 'Default'
        self.rulesscreen = Frame(bg='cyan', relief=GROOVE, border=20)
        self.ruleslabel = Label(self.rulesscreen, text=rulestext(), font='bold 20', justify='left', bg='cyan',
                                pady=18, padx=20)
        self.ruleslabel.pack()
        self.DefaultButton = Button(self.rulesscreen, text='Default', command=lambda:self.show_frame(self.mainscreen, 'Default'),
                                    font='bold 20', padx=15, bg='DarkMagenta', fg='white', activebackground='OrangeRed',
                                    relief=RIDGE, border=15, activeforeground='white')
        self.DefaultButton.place(x=900, y=300)
        self.MultiuserButton = Button(self.rulesscreen, text='Multiuser', command=lambda: self.show_frame(self.multiuserscreen, 'Multiuser'),
                                    font='bold 20', bg='DarkMagenta', fg='white', activebackground='OrangeRed',
                                    relief=RIDGE, border=15, activeforeground='white')
        self.MultiuserButton.place(x=900, y=450)
        self.mainscreen = Frame(bg='yellow')
        self.wordtoguesslabel = Label(self.mainscreen, justify='center', text=len(self.word) * '-', font='bold 50', bg='cyan',
                          border=20, relief=GROOVE, padx=25)  # blanks label
        self.liveslabel = Label(self.mainscreen, justify='center', text='Lives Remaining : ' + str(self.lives),
                                font=('italic', '15', 'bold'), bg='royalblue', fg='white',
                                border=20)  # lives display label
        self.mainscreeninfolabel = Label(self.mainscreen, justify='center',
                          text='Randomly guess a letter and press enter... to guess the word below.',
                          font='italic 15', bg='royalblue', fg='white', border=20)
        self.wordinput = Entry(self.mainscreen, justify='center', font='bold 20', relief=SUNKEN)  # input widget
        self.mainscreenheading = Label(self.mainscreen, text='--- Welcome to Hangman Game ---', padx=100, pady=10, font='Algerian 30', bg='pink',
                        border=15,
                        relief=RIDGE, width='100')
        self.hintbutton = Button(self.mainscreen, text='Hint', bg='navy', fg='white', relief=RIDGE, font='rockwellextrabold 20',
                            activebackground='blue', activeforeground='yellow', command=self.hint)
        self.hintlabel = Label(self.mainscreen, font='bold 20', bg='lightsalmon', relief=SUNKEN,
                          text='The hint will be available only if you have 3 or less lives left. If you take hint then your l')
        self.multiuserscreen = Frame(bg='GreenYellow', relief=GROOVE, border=20)
        self.muheading = Label(self.multiuserscreen, text='Multiuser play', border=15, font='cooper 30', pady=5, bg='Aqua', relief=RIDGE)
        self.muheading.pack(fill=X)
        self.muwordlabel = Label(self.multiuserscreen, text='Enter the word you want your partner to guess = ', relief=GROOVE,
                            font='bold 20',
                            border=10, pady=10)
        self.muwordinp = Entry(self.multiuserscreen, show='•', relief=GROOVE, font='bold 18', bg='Cornsilk', border=20, justify=CENTER)
        self.mumeaninglabel = Label(self.multiuserscreen, text='Enter the meaning for your partner as a hint = ', relief=GROOVE,
                               font='bold 20',
                               border=10, pady=10, width=37)
        self.mumeaninginp = Entry(self.multiuserscreen, relief=GROOVE, font='bold 20', bg='Cornsilk', border=20, justify=CENTER, width=40)
        self.mumeaninginp.default_show_val = self.mumeaninginp['show']
        self.mumeaninginp['show'] = "*"
        self.checkbutton = Checkbutton(self.multiuserscreen, font='bold 20',
                                  text="Hide meaning",
                                  onvalue=True,
                                  offvalue=False,
                                  command=self.toggle_meaning)
        self.checkbutton.var = BooleanVar(value=True)
        self.checkbutton['variable'] = self.checkbutton.var
        self.muwordlabel.place(x=0, y=100)
        self.muwordinp.place(x=620, y=100)
        self.mumeaninglabel.place(x=0, y=200)
        self.checkbutton.place(x=1000, y=300)
        self.mumeaninginp.place(x=620, y=200)
        self.muplaybutton = Button(self.multiuserscreen, text='Play Hangman', relief=GROOVE, font='bold 20',
                                   command=lambda: self.show_frame(self.mainscreen, 'Multiuser'),
                              bg='Aquamarine', activebackground='LightCyan')
        self.muplaybutton.place(x=550, y=300)
        self.rulesscreen.grid(row=0, column=0, sticky="NSEW")
        self.mainscreen.grid(row=0, column=0, sticky="NSEW")
        self.multiuserscreen.grid(row=0, column=0, sticky='NSEW')
        self.mainscreenheading.pack()  # title welcome to hangman game
        self.wordtoguesslabel.place(x=550, y=220)
        self.wordinput.place(x=530, y=360)
        self.liveslabel.place(x=1090, y=100)
        self.mainscreeninfolabel.place(y=100)
        self.hintbutton.place(x=640, y=500)
        self.hintlabel.place(y=600)
        self.show_frame(self.rulesscreen)
        self.mainscreen.bind_all('<Return>', self.checkword)

    def toggle_meaning(self):  # function to hide/show meaning
        if self.checkbutton.var.get():
            self.mumeaninginp['show'] = "*"
        else:
            self.mumeaninginp['show'] = ""

    # function to set a gametype and change the frames
    def show_frame(self, frame, gametype='Default'):
        frame.tkraise()
        self.GameType = gametype
        self.wordchoice()
        self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
        self.mainscreen.bind_all('<Return>', self.checkword)

    # function to set word to guess and hint for it
    def wordchoice(self):
        if self.GameType == 'Default':
            self.word, self.meaning = chooseword()
        elif self.GameType == 'Multiuser':
            self.word = self.muwordinp.get()
            self.meaning = self.mumeaninginp.get()
            self.muwordinp.delete(0, END)
            self.mumeaninginp.delete(0, END)
        self.blankslist = list(len(self.word) * '-')  # list of blanks

    # function of generating hint
    def hint(self):
        if self.lives <= 3:
            self.hintlabel.configure(text='Hint : ' + self.meaning)
            self.lives -= 1
            self.liveslabel.configure(text='Lives Remaining : ' + str(self.lives))
            self.hintbutton["state"] = 'disabled'

    # function for running the game main function
    def checkword(self, event):
        self.letterguessed = self.wordinput.get()  # get value from input -- entered value 'ev' of the main game input box
        self.wordinput.delete(0, END)  # delete when value entered
        if (not self.letterguessed.isalpha()) or self.letterguessed.isspace():  # checking if value entered is other than letter
            messagebox.showerror('Error', 'Wrong entry, try again')
            self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
        else:  # main logic begins
            if self.letterguessed in self.guess_list:  # if entered a value already guessed
                self.mainscreeninfolabel.configure(text='Oops, you\'ve already guessed it.\nHere\'s what you\'ve guessed : '
                                                        +str(self.guess_list)[1:-1] + '. ' + 'Try again')
                self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
            elif self.letterguessed not in self.word:  # if the letter is not in the word (wrong guess)
                self.guess_list.append(self.letterguessed)
                self.lives -= 1
                self.liveslabel.configure(text='Lives Remaining : ' + str(self.lives))
                self.mainscreeninfolabel.configure(text='Wrong guess : (')
                self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
            else:  # if guessed letter is correct
                self.guess_list.append(self.letterguessed)
                for i in range(len(self.word)):
                    if self.letterguessed == self.word[i]:
                        self.blankslist[i] = self.letterguessed
                self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
                self.mainscreeninfolabel.configure(text='Good job!!! : )')
            if self.blankslist == list(self.word):  # if the whole word is guessed
                messagebox.showinfo('You won', 'Congratulations, you won the game!')
                self.ans = wanttoplay()
            if self.lives == 0:  # if all lives are lost
                self.wordtoguesslabel.configure(text=lst_str(self.word))
                messagebox.showinfo('You lost', 'Sorry, all your lives are lost.')
                self.ans = wanttoplay()
            if self.ans == 'exit':  # if the player doesn't want to play
                win.destroy()
            elif self.ans == 'reset':  # if the user wants to play again
                if self.GameType == 'Multiuser':
                    self.show_frame(self.multiuserscreen, 'Multiuser')
                elif self.GameType == 'Default':
                    self.wordchoice()
                self.blankslist = list(len(self.word) * '-')
                self.lives = 10
                self.wordtoguesslabel.configure(text=lst_str(self.blankslist))
                self.hintlabel.configure(text='The hint will be available only if you have 3 lives left.')
                self.liveslabel.configure(text='Lives Remaining : ' + str(self.lives))
                self.guess_list = []
                self.ans = True
                self.hintbutton["state"] = 'normal'


if __name__ == "__main__":
    win = GUI()
    win.title('Play Hangman')
    win.iconbitmap(r'E:\projects\Hangman Game CS Project class 12\gameicon.ico')
    win.state("zoomed")
    win.rowconfigure(0, weight=1)
    win.columnconfigure(0, weight=1)
    win.mainloop()
