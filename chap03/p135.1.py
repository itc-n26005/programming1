#f = open('sample.txt', 'r')
#data = f.readline()
#print(data)
#f.close()

with open('sample.txt','r') as f:
    data = f.readline()
    print(data)
