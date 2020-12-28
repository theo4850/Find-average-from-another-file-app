import statistics as st

z = input('Εισάγετε το όνομα του αρχείου που θέλετε να ανοίξετε(μαζί με την txt κατάληξη): ')

def average(dlist):
    numlist = [float(i) for i in dlist]
    av = st.mean(numlist)
    return av

def standard_deviation(dlist):
    numlist = [float(i) for i in dlist]
    std = st.stdev(numlist)
    return std

try:
    with open(z, 'r') as id:
        datalist = id.read().splitlines()
except Exception as error:
    print(error)
else:
    avg = average(datalist)
    avg_real = round(avg, 3)
    stdev = standard_deviation(datalist)
    stdev_real = round(stdev, 3)
    with open('outputdata.txt', 'w') as od:
        Line = 'Μέσος όρος = '+str(avg_real)+'\n'
        od.write(Line)
    with open('outputdata.txt', 'a') as ot:
        Line2 = 'Τυπική απόκλειση = '+str(stdev_real)
        ot.write(Line2)
        
        
