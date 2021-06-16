import csv
with open("data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
newData = data[0]
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total+=int(i)
    mean = total/n
    return mean
squaredList = []
for q in newData:
    a = int(q)-mean(newData)
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum+=i
n = len(newData)
result = sum/(n-1)
standardDiviation = math.sqrt(result)