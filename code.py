import re
hand = open('regex_sum_42.txt')
numlist = list()
numbers_sum = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    #if len(stuff) == 0: continue
    num = int(stuff[0])
    #numbers_sum += int(stuff)
    numlist.append(num)
print len(numlist)