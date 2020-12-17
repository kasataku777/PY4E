# 10.2 Write a program to read through the mbox-short.
# txt and figure out the distribution by hour of the
#  day for each of the messages.
#  You can pull the hour out from the 'From ' line by
# finding the time and then splitting the string a second time
# using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)


di = dict()

for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    if len(wds) < 6 or wds[0] != 'From':
        continue
    time = wds[5]
    tlist = time.split(':')
    hour = tlist[0]
    di[hour] = di.get(hour, 0)+1

# sort
lst = list()
for key, value in di.items():
    lst.append((key, value))

lst.sort()

for k, v in lst:
    print(k, v)
