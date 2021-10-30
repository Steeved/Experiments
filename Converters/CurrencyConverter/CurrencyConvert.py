#from values import kurs
import json


def exchange(input, output, value):  # Converts the "value" in currency "input" to currency "output"
    if str(input) in kurs and output in kurs:
        return round((value * kurs[input]) / kurs[output], 2)
    else:
        exit('No Such Currency')


file = open('values.txt', 'r')
kurs = dict(json.loads(file.read()))

print("\nAvailable currency types:\n"+", ".join(kurs.keys())+'\n')
inp = input('Value to convert from:')
out = input('Value to convert to:')
value = input('Amount:')
input(str(exchange(inp, out, value)))


