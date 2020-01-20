from tkinter import *
from functools import partial

alphs = [
    ['a', 'j', 's'],
    ['b', 'k', 't'],
    ['c', 'l', 'u'],
    ['d', 'm', 'v'],
    ['e', 'n', 'w'],
    ['f', 'o', 'x'],
    ['g', 'p', 'y'],
    ['h', 'q', 'z'],
    ['i', 'r']
]
# coding=utf-8
data = [
    [],
    [
        'Testing 1 & 1',
        'Testing 1 & 2',
        'Testing 1 & 3',
        'Testing 1 & 4',
        'Testing 1 & 5'
    ],
    [
        'Testing 2 & 1',
        'Testing 2 & 2',
        'Testing 2 & 3',
        'Testing 2 & 4',
        'Testing 2 & 5'
    ],
    [
        'Testing 3 & 1',
        'Testing 3 & 2',
        'Testing 3 & 3',
        'Testing 3 & 4',
        'Testing 3 & 5'
    ],
    [
        'Testing 4 & 1',
        'Testing 4 & 2',
        'Testing 4 & 3',
        'Testing 4 & 4',
        'Testing 4 & 5'
    ],
    [
        'Testing 5 & 1',
        'Testing 5 & 2',
        'Testing 5 & 3',
        'Testing 5 & 4',
        'Testing 5 & 5'
    ],
    [
        'Testing 6 & 1',
        'Testing 6 & 2',
        'Testing 6 & 3',
        'Testing 6 & 4',
        'Testing 6 & 5'
    ],
    [
        'Testing 7 & 1',
        'Testing 7 & 2',
        'Testing 7 & 3',
        'Testing 7 & 4',
        'Testing 7 & 5'
    ],
    [
        'Testing 8 & 1',
        'Testing 8 & 2',
        'Testing 8 & 3',
        'Testing 8 & 4',
        'Testing 8 & 5'
    ],
    [
        'Testing 9 & 1',
        'Testing 9 & 2',
        'Testing 9 & 3',
        'Testing 9 & 4',
        'Testing 9 & 5'
    ]
]

result = 0


def calculatePoint(self):
    global result
    result = 0
    name = txtEntry.get()
    for n in name.lower():
        i = 0
        for a in alphs:
            i += 1
            if n in a:
                result += i

    test = 0
    while result >= 10:
        moreResult = 0
        for i in str(result):
            moreResult += int(i)
        result = moreResult

    lblPoint.config(text=str(result))
    lblPoint.grid(row=1, column=2, sticky=S, ipadx=38, pady=50)
    root.update()


def resultGuess(num):
    global result
    if result > 0:
        txtResult.delete('1.0', END)
        txtResult.insert(INSERT, data[result][num])


root = Tk()
root.title('Guessing')

frameHeader = Frame(root, bg='green')
frameHeader.grid(row=0, column=0)
title = Label(frameHeader, text='Guessing by name', font=("Courier", 44), bg='green', fg='#fff')
title.grid(row=0, column=0, columnspan=10, padx=50, pady=10)

frameBody = Frame(root, bg='#fff')
frameBody.grid(row=1, column=0)
textLbl = Label(frameBody, text='Name: ', font=("Courier", 20), bg='#fff')
textLbl.grid(row=1, column=0, sticky=NW, ipadx=50, pady=50)
txtEntry = Entry(frameBody, font=("Courier", 20), bg='#fff')
txtEntry.bind('<Return>', calculatePoint)
txtEntry.grid(row=1, column=1, sticky=S, ipadx=20, pady=50)
lblPoint = Label(frameBody, text='', font=("Courier", 20), bg='#fff')
lblPoint.grid(row=1, column=2, sticky=S, ipadx=46, pady=50)

wrapper = Frame(root, bg='#fff')
wrapper.grid(row=2, column=0)
frameFooter = Frame(wrapper, bg='#fff')
frameFooter.grid(row=2, column=0, padx=63)


btnFirst = Button(frameFooter, text="Character", font=("Courier", 14), command=partial(resultGuess, 0))
btnFirst.grid(row=2, column=0, sticky=W, padx=10, pady=15)
btnSecond = Button(frameFooter, text="Individual", font=("Courier", 14), command=partial(resultGuess, 1))
btnSecond.grid(row=2, column=1, sticky=W, padx=10, pady=15)
btnThird = Button(frameFooter, text="Love", font=("Courier", 14), command=partial(resultGuess, 2))
btnThird.grid(row=2, column=2, sticky=W, padx=10, pady=15)
btnFourth = Button(frameFooter, text="Work", font=("Courier", 14), command=partial(resultGuess, 3))
btnFourth.grid(row=2, column=3, sticky=W, padx=10, pady=15)
btnFifth = Button(frameFooter, text="Money", font=("Courier", 14), command=partial(resultGuess, 4))
btnFifth.grid(row=2, column=4, sticky=W, padx=10, pady=15)

wrappBottom = Frame(root, bg='#fff')
wrappBottom.grid(row=3, column=0)
resultWrap = Frame(wrappBottom, bg='#fff')
resultWrap.grid(row=3, column=0, padx=10, pady=10)

txtResult = Text(resultWrap, bg='#eaeaea')
txtResult.grid(row=3, column=0)

root.mainloop()