import time
import grovepi

filename = "indent_decode.py"

def get_indentlevel_from_file(filename):
    filehandle = open(filename, 'r')
    ind = []
    empty = 0
    j = 0
    while True:
        line = filehandle.readline()
        if not line:
            break;
        elif (len(line.strip())==0):
            ind.append(empty)
            j=j+1
        else:
            leading_spaces = len(line) - len(line.lstrip())
            ind.append(leading_spaces)
            j=j+1
 
    filehandle.close()
    return(ind)

yPin = 1
grovepi.pinMode(yPin,"INPUT")

i=0
get_bin = lambda x: format(x, 'b')

while True:
        y = grovepi.analogRead(yPin)

        if ((y>700)and(i<j)):
                k=0
                while(((i+k)<j)and(k<5)):
                        if(i>0):
                                s1.write(get_bin((ind[i+k]-ind[i+k-1])))
                                k=k+1
                                i=i+1
                                time.sleep(.5)
                        elif(i==0):
                                s1.write(get_bin((ind[i+k])))
                                k=k+1
                                i=i+1
                                time.sleep(.5)

        elif((y<200)and(i>0)):
                k=0
                while(((i-k)>0)and(k<5)):
                        if(i<j):
                                s1.write(get_bin((ind[i+k]-ind[i+k+1])))
                                k=k+1
                                i=i-1
                                time.sleep(.5)

                        elif(i==j):
                                s1.write(get_bin((ind[i+k])))
                                k=k+1
                                time.sleep(.5)
                                i=i-1
