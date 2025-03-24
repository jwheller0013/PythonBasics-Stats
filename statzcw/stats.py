import math
from typing import List

def zcount(data: List[float]) -> float :
    pass
    return sum(data)

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
    middle = len(data)//2
    return data(middle)

def zvariance(data: List[float]) -> float :
    pass
    n = data.count() - 1
    mean = sum(data)/n
    deviations = []
    for xi in data:
        deviations.append(math.sqrt(abs(mean - xi)))
    return sum(deviations)/n
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    pass
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float :
    pass
    return zstddev(data)/((zcount(data)) ** 0.5)

def cov(a, b):
    pass

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
