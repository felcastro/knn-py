import csv
import math

def knn(k, exemple, data, weighted):
    distances = [[euclidianDistance(exemple, row[:-1]), row[-1]] for row in data]
    distances.sort(key=lambda x: x[0])
    if weighted:
        exempleClass = getBestWeightedDistance(distances[:k])
    else:
        exempleClass = max([row[1] for row in distances[:k]])
    return exempleClass

def getBestWeightedDistance(distances):
    classes = {}
    for row in distances:
        if row[1] in classes:
            classes[row[1]] += 1/row[0]
        else:
            classes[row[1]] = 1/row[0]
    return max(classes, key=classes.get)

def euclidianDistance(x, y):
    attrSum = 0
    for i in range(len(x)):
        attrSum += math.pow(int(x[i]) - int(y[i]), 2)
    return math.sqrt(attrSum)

def dataToString(data):
    string = ""
    for i in data:
        string += str(i) + "\n"
    return string

openFile = open("data.csv", "r")
data = list(csv.reader(openFile))
printData = {"y": True, "n": False}[input("Print data? <Y, N>").lower()]
if printData:
    print(dataToString(data))
while(True):
    k = int(input("Inform the K value:"))
    exemple = input("Inform the exemple as <1,2,3,...,n>: ")
    exemple = [int(x) for x in exemple.split(",")]
    isWeighted = {"y": True, "n": False}[input("Use weighted distances? <Y, N>").lower()]
    print(knn(k, exemple, data, isWeighted))