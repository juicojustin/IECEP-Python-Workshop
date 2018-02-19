file_text = open("DNA Sampling.txt").read()
length = len(file_text)
C = 0
G = 0

for x in range(0,length):
    if file_text[x] == 'C':
        C = C+1
    else:
        C = C+0
    if file_text[x] == 'G':
        G = G+1
    else:
        G = G+0
    sum = C+G

print "The percent of C+G is equal",(100.0*sum)/length,"%"
