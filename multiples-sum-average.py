for i in range(0, 1000):
    if i % 2 != 0:
        print i


for i in range(5, 1000000):
    if i % 5 == 0:
        print i


a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
print sum


avg = sum / len(a)
print avg
