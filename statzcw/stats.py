import math
from typing import List

def zcount(data: List[float]) -> float :
    pass
    return len(data)

def zmean(data: List[float]) -> float :
    pass
    return sum(data)/len(data)

def zmode(data: List[float]) -> float :
    pass
    mode = 0
    for i in data:
        if data.count(i) > mode:
            mode = i
    return mode

def zmedian(data: List[float]) -> float :
    pass
    middle = (len(data))//2
    return data[middle]

def zvariance(data: List[float]) -> float :
    pass
    n = len(data)
    mean = sum(data)/n
    deviations = []
    for xi in data:
        deviations.append((abs(mean - xi)) ** 2)
    return sum(deviations)/(n-1)
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    pass
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float :
    pass
    return zstddev(data)/((zcount(data)) ** 0.5)

def cov(a, b):
    pass
    sum = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            sum += ((a[i] - zmean(a)) * (b[i]) - zmean(b))
        return sum/(len(a) - 1)

def zcorr(datax: List[float], datay: List[float]) -> float :
    pass



def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data

# data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
# data2 = [1.0, 2.0, 2.0, 4.0, 5.0]
#
# print(zmedian(data0))