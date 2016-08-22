f = open('phone_numbers6.txt', 'w')

for i in range(0,1000000):
    #print (str(i).zfill(7))    #prints to stdout
    #print >> f, (str(i).zfill(7))
    f.write(str(i).zfill(6))
    f.write('\n')
f.close()