
import datetime


print(datetime.datetime.now())
def my_num(n):
    num = 1000
    three_times_table = []
    for n in range(num):
        if n % 3 == 0 or n % 5 == 0:
            three_times_table.append(n)
            print(sum(three_times_table))
        
my_num('n')            

print(datetime.datetime.now())


'''
print(datetime.datetime.now())


print(datetime.datetime.now())
sum = 0
for n in range (1000):
    if n%3==0 or n%5==0:
        sum = sum + n

print(sum)

print(datetime.datetime.now())
'''