f = open('day1data','r')
data = f.readlines()
data1 = []
for i in data:
    data1.append(int(i.strip()))


for j in data1:     #part 1
    for k in data1:
        if j+k == 2020:
            print(j*k)
        
for j in data1:     #part 2
    for k in data1:
        for l in data1:
            if j+k+l == 2020:
                print(j*k*l)
        