import re
hand = open('regex_sum_258025.txt')
numlist = list()
final_list = list()
numbers_sum = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    #num = int(stuff[0])
    #numbers_sum += int(stuff)
    numlist.append(stuff)
for i in numlist:
    for n in i:
        final_list.append(int(n))
print sum(final_list)