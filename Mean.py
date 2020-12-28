import statistics as st

def average(dlist):
    numlist = [float(i) for i in dlist]
    av = st.mean(numlist)
    return av
