data = []
with open('export.txt', 'r') as infile:
    for line in infile:
        data.append(line.split('.')[0])

with open('output', 'wb') as outfile:
    for line in data:
        outfile.write(bytes.fromhex(line))
