import tkinter as tk
import re


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.mode = 'getBinary'

    def create_widgets(self):
        self.integerNumberEntry = tk.Entry()
        self.conversionSign = tk.Label(text='->')
        self.resultLabel = tk.Label(text='Binary number...', fg='black')
        self.Title = tk.Label(text='Integer to Binary Converter')
        self.changeModeButton = tk.Button(text='Change mode', command=self.changeMode)
        self.convertButton = tk.Button(text='Convert to binary', command=self.binConvert)
        self.conversionTypeSign = tk.Label(text='Conversion type: Integer -> Binary', fg='black')
        self.changeModeButton.pack(side='bottom')
        self.conversionTypeSign.pack(side='bottom')
        self.Title.pack(side='top')
        self.integerNumberEntry.pack(side='left')
        self.conversionSign.pack(side='left')
        self.resultLabel.pack(side='left')
        self.convertButton.pack(side='left')

    def binConvert(self):

        try:
            integer = int(self.integerNumberEntry.get())
            if integer == 0:
                self.resultLabel.config(text='0', fg='black')
            elif integer == 1:
                self.resultLabel.config(text='1', fg='black')
            elif integer < 0:
                self.resultLabel.config(text="Can't convert negative numbers", fg='red')
            else:
                binaryNumbers = []
                num1 = integer
                while num1 > 0:
                    num2 = num1 % 2
                    binaryNumbers.append(num2)
                    if num2 == 1:
                        num1 -= 1
                        num1 = int(num1 / 2)
                    elif num2 == 0:
                        num1 = int(num1 / 2)
                bin = ''
                for bins in binaryNumbers:
                    bin = bin + str(bins)
                self.resultLabel.config(text=str(bin[::-1]), fg='black')
        except ValueError:
            self.resultLabel.config(text='Not number/s', fg='red')
    def intConvert (self) :
        binInput = str(self.integerNumberEntry.get())
        str1 = re.sub('[0-9]', '', binInput)
        str2 = re.sub('[01]', '', binInput)
        if str1 != '':
            self.resultLabel.config(text='Not number/s', fg='red')
        else :
            if str2 != '':
                self.resultLabel.config(text='Not binary number/s', fg='red')
            else :
                result = 0
                pow2 = 1
                for digitIndex in range(len(binInput) - 1, -1, -1) :
                    result += int(binInput[digitIndex]) * pow2
                    pow2 *= 2
                self.resultLabel.config(text=str(result), fg='black')
    def changeMode (self) :
        if self.mode == 'getBinary':
            self.resultLabel.config(text='Integer number...')
            self.conversionTypeSign.config(text='Conversion type: Binary -> Integer', fg='black')
            self.convertButton.config(text='Convert to integer', command=self.intConvert)
            self.mode = 'getInteger'

        elif self.mode == 'getInteger':
            self.resultLabel.config(text='Binary number...')
            self.conversionTypeSign.config(text='Conversion type: Integer -> Binary', fg='black')
            self.convertButton.config(text='Convert to binary', command=self.binConvert)
            self.mode = 'getBinary'

app = Application()
app.master.title('Convertor')
app.master.minsize(width=150, height=75)
app.mainloop()