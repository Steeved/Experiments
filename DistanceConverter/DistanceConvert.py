import json


def exchange(input, output, value):
    if str(input) in dist and output in dist:
        return (float(value) * float(dist[input])) / float(dist[output])
    else:
        exit('No Such Distance type')


file = open('values.txt', 'r')
dist = dict(json.loads(file.read()))
print("\nAvailable Distance types:\n" + ", ".join(dist.keys()) + '\n')
inp = input('Value to convert from:')
out = input('Value to convert to:')
value = float(input('Amount:'))
input(str(exchange(inp, out, value)))
