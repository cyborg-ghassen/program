# read file bitcoinAddresses and split
f = open("bitcoinAddresses.txt", "r")
lines = f.readlines()

list_lines = []
for i in lines:
    list_lines += [i.split(' ')]

phrases = []
for i in list_lines:
    try:
        phrases.append(i[1])
    except Exception as e:
        continue

# write into file
f = open("phrases.txt", "w")
for i in phrases:
    f.writelines(i + '\n')
