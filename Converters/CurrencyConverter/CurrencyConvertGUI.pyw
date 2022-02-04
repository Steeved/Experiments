from tkinter import *
from tkinter import ttk
from re import sub
import requests

file = open('values.txt', 'r')
values = file.read().split()
url = f'https://v6.exchangerate-api.com/v6/4a39ffad1f4db72dbaf9ca8c/latest/{values[0]}'
response = requests.get(url).json()
allRates = response['conversion_rates']
rates = {}
for takeValue in values:
    if takeValue in allRates.keys():
        rates[takeValue] = allRates[takeValue]


class Application(Tk):
    def __init__(self):
        super(Application, self).__init__()
        self.title('Currency Converter')
        self.geometry("400x80")
        self.create_widgets()

    def create_widgets(self):
        self.selectedIn = StringVar(self)
        self.selectedOut = StringVar(self)
        self.selectedValue = StringVar(self)
        self.key = list(rates.keys())
        self.input = self.key[0]
        self.output = self.key[1]

        self.Title = Label(text='Currency Converter')
        self.numberEntry = Entry(textvariable=self.selectedValue)
        self.modeLabel = Label(text=f'Converting from {self.input} to {self.output}')
        self.conversionSign = Label(text='->')
        self.resultLabel = Label(text='Output Value...')
        self.InValue = ttk.OptionMenu(self, self.selectedIn, self.key[0], *self.key, command=self.updateValues)
        self.OutValue = ttk.OptionMenu(self, self.selectedOut, self.key[1], *self.key, command=self.updateValues)

        self.Title.pack(side='top')
        self.modeLabel.pack(side='top')
        self.InValue.pack(side='left')
        self.numberEntry.pack(side='left')
        self.conversionSign.pack(side='left')
        self.OutValue.pack(side='left')
        self.resultLabel.pack(side='left')

        self.selectedValue.trace_add('write', self.updateValues)  # Activates when changing the value

    def updateValues(self, *args):
        num = sub('[^0-9]', '', self.selectedValue.get())
        input = self.selectedIn.get()
        output = self.selectedOut.get()
        self.resultLabel.config(text=str(  # Converts from the currency 'input' to 'output'
            round(float(num or 0) * float(rates[output]) / float(rates[input]), 2)))
        self.modeLabel.config(text=f'Converting from {input} to {output}')  # Change mode


app = Application()
app.mainloop()
