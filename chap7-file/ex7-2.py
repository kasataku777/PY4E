add = 0.0
count = 0

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print('File cannnot be open:', fname)

for line in fhand:
    index = line.find('X-DSPAM-Confidence:')
    if(index == -1):
        continue
    snum = line[index+len('X-DSPAM-Confidence:'):]
    fnum = float(snum.strip())
    count = count+1
    add += fnum

average = add/count
print('Average spam confidence:', average)
