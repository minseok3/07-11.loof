list = [100,200,400,800,1000,1300]
result = 0
for list2 in list:
    result = result + list2
avg = result / len(list)
print(int(avg))