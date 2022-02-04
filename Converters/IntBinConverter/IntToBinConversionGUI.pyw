from tkinter import *
from re import sub


def binConv(a):  # Converts an integer to binary
    b = []
    c = a
    while c > 0:
        if c < 2:
            b.append(str(c))
        else:
            b.append(c % 2)
        c -= c % 2
        c //= 2
    e = ''
    for h in b:
        e = e + str(h)
    return e[::-1]


def intConv(b):  # Converts a binary to an integer
    c = 1
    d = 0
    for g in range(len(str(b)) - 1, -1, -1):
        d += int(str(b)[g]) * c
        c *= 2
    return str(d)


class Application(Tk):
    def __init__(self, master=None):
        super(Application, self).__init__()
        self.title('Currency Converter')  # Set window size and title
        self.geometry("400x100")
        self.create_widgets()
        self.mode = 'getBinary'

    def create_widgets(self):  # Define and pack buttons, labels ...
        self.currentNumber = StringVar(self)

        self.numberEntry = Entry(self, textvariable=self.currentNumber)
        self.conversionSign = Label(text='->')
        self.resultLabel = Label(text='Binary number...', fg='black')
        self.Title = Label(text='Integer to Binary Converter')
        self.changeModeButton = Button(text='Change mode', command=self.changeMode)
        self.conversionTypeSign = Label(text='Converting from Integer to Binary numbers', fg='black')

        self.changeModeButton.pack(side='bottom')
        self.conversionTypeSign.pack(side='bottom')
        self.Title.pack(side='top')
        self.numberEntry.pack(side='left')
        self.conversionSign.pack(side='left')
        self.resultLabel.pack(side='left')

        self.currentNumber.trace_add('write', self.updateValues)  # Activates when changing the value

    def changeMode(self):
        if self.mode == 'getBinary':
            self.resultLabel.config(text='Integer number...')
            self.conversionTypeSign.config(text='Converting from Binary to Integer numbers', fg='black')
            self.mode = 'getInteger'

        elif self.mode == 'getInteger':
            self.resultLabel.config(text='Binary number...')
            self.conversionTypeSign.config(text='Converting from Integer to Binary numbers', fg='black')
            self.mode = 'getBinary'

    def updateValues(self, *args):
        num = int(sub('[^0-9]', '', self.currentNumber.get()) or 0)
        binNum = int(sub('[^01]', '', str(num)) or 0)
        if self.mode == 'getBinary':
            self.resultLabel.config(text=str(binConv(num)))
        else:
            self.resultLabel.config(text=str(intConv(binNum)))


app = Application()
app.mainloop()
