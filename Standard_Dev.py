import statistics as st

def standard_deviation(dlist):
    numlist = [float(i) for i in dlist]
    std = st.stdev(numlist)
    return std
