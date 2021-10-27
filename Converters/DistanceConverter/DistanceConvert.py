import json


def exchange(input, output, value):
    if str(input) in dist and output in dist:
        return (float(value) * float(dist[input])) / float(dist[output])
    else:
        exit('No Such Unit of length')


file = open('values.txt', 'r')
dist = dict(json.loads(file.read()))
print("\nAvailable Units of length:\n" + ", ".join(dist.keys()) + '\n')
inp = input('Unit to convert from:')
out = input('Unit to convert to:')
value = float(input('Units:'))
input(str(exchange(inp, out, value)))
