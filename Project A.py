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
    print('Θέλετε να εμφανιστούν τα αποτελέσματα, να εισαχθούν σε ξεχωριστό αρχείο ή και τα δύο;')
    select = input('Γράψτε 1 για την πρώτη επιλογή, 2 για την δεύτερη και 3 για την τρίτη: ')
    if select == 1:
        print('Μέσος όρος: ', avg_real, '/n', 'Τυπική απόκλειση: ', stdev_real)
    elif select == 2:
        with open('outputdata.txt', 'w') as od:
            Line = 'Μέσος όρος = '+str(avg_real)+'\n'
            od.write(Line)
        with open('outputdata.txt', 'a') as ot:
            Line2 = 'Τυπική απόκλειση = '+str(stdev_real)
            ot.write(Line2)
    elif select == 3:
        print('Μέσος όρος: ', avg_real, '/n', 'Τυπική απόκλειση: ', stdev_real)
        try:
            with open('outputdata.txt', 'w') as od:
                Line = 'Μέσος όρος = '+str(avg_real)+'\n'
                od.write(Line)
            with open('outputdata.txt', 'a') as ot:
                Line2 = 'Τυπική απόκλειση = '+str(stdev_real)
                ot.write(Line2)
        except Exception as error:
            print(error)
        else:
            print('Τα αποτελέσματα εισήχθησαν επιτυχώς σε ξεχωριστό αρχείο.')
