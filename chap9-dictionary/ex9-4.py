# 9.4 Write a program to read through the mbox-short.txt
#  and figure out who has sent the greatest number of
# mail messages. The program looks for 'From ' lines
#  and takes the second word of those lines
#  as the person who sent the mail.
# The program creates a Python dictionary
# that maps the sender's mail address to a count
# of the number of times they appear in the file.
# After the dictionary is produced, the program reads
#  through the dictionary using a maximum loop to
#  find the most prolific committer.

fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)


di = dict()

for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    if len(wds) < 2 or wds[0] != 'From':
        continue
    mail = wds[1]
    di[mail] = di.get(mail, 0)+1

# detect largest

largest = -1
largekey = None
for key, value in di.items():
    if value > largest:
        largest = value
        largekey = key

print(largekey, largest)
