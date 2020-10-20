# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
Total, c = 0, 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    Total += float(line[(line.find(':'))+2:])
    c += 1
print("Average spam confidence: ", Total/c)