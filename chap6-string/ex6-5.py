text = "X-DSPAM-Confidence:    0.8475"

index = text.find(':')
snum = text[index+1:]
fnum = float(snum.strip())
print(fnum)
