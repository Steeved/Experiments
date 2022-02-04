import tkinter as tk
from re import sub as s


def binConvert(a):
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


def intConvert(b):
    c = 1
    d = 0
    for g in range(len(str(b)) - 1, -1, -1):
        d += int(str(b)[g]) * c
        c *= 2
    return str(d)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.mode = 'getBinary'
        self.currentInt = ''
        self.currentBin = ''

    def create_widgets(self):
        self.integerNumberEntry = tk.Entry()
        self.conversionSign = tk.Label(text='->')
        self.resultLabel = tk.Label(text='Binary number...', fg='black')
        self.Title = tk.Label(text='Integer to Binary Converter')
        self.changeModeButton = tk.Button(text='Change mode', command=self.changeMode)
        self.convertButton = tk.Button(text='Convert to binary', command=self.binConv)
        self.conversionTypeSign = tk.Label(text='Conversion type: Integer -> Binary', fg='black')
        self.changeModeButton.pack(side='bottom')
        self.conversionTypeSign.pack(side='bottom')
        self.Title.pack(side='top')
        self.integerNumberEntry.pack(side='left')
        self.conversionSign.pack(side='left')
        self.resultLabel.pack(side='left')
        self.convertButton.pack(side='left')

    def binConv(self):
        self.currentInt = self.integerNumberEntry.get().split()
        valid = True
        for ab in self.currentInt:
            try:
                integer = int(ab)
                if integer < 0:
                    self.resultLabel.config(text="Can't convert negative numbers", fg='red')
                    valid = False
            except ValueError:
                self.resultLabel.config(text='Not number/s', fg='red')
                valid = False
        if valid:
            ac = ''
            for ad in self.currentInt:
                ac += str(binConvert(int(ad))) + ' '
            self.resultLabel.config(text=ac, fg='black')

    def intConv(self):
        self.currentBin = self.integerNumberEntry.get().split()
        valid2 = True
        for ae in self.currentBin:
            if s('[0-9]', '', ae) != '':
                self.resultLabel.config(text='Not number/s', fg='red')
                valid2 = False
            else:
                if s('[01]', '', ae) != '':
                    self.resultLabel.config(text='Not binary number/s', fg='red')
                    valid2 = False
        if valid2:
            x = ''
            for aa in self.currentBin:
                x += str(intConvert(int(aa))) + ' '
            self.resultLabel.config(text=str(x), fg='black')

    def changeMode(self):
        if self.mode == 'getBinary':
            self.resultLabel.config(text='Integer number...')
            self.conversionTypeSign.config(text='Conversion type: Binary -> Integer', fg='black')
            self.convertButton.config(text='Convert to integer', command=self.intConv)
            self.mode = 'getInteger'

        elif self.mode == 'getInteger':
            self.resultLabel.config(text='Binary number...')
            self.conversionTypeSign.config(text='Conversion type: Integer -> Binary', fg='black')
            self.convertButton.config(text='Convert to binary', command=self.binConv)
            self.mode = 'getBinary'


app = Application()
app.master.title('Convertor')
app.master.minsize(width=150, height=75)
app.mainloop()
