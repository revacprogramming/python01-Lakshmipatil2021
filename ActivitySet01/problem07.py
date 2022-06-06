text = "X-DSPAM-Confidence: 0.8475";
x=text.find(":")
fpstring = text[x+1:]
fvalue=float(fpstring)
print(fvalue)
