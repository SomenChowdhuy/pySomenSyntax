#create a list with 10 values and find the smallest, largest and sum of all the number in the list
list = [11,55,22,58,87,3,23,8,104,44]
print("Smallest number is: ",min(list))
print("Largest number is: ",max(list))
print("Sum of all numbers is: ",sum(list))

li = [1,3,6,10,100,14,5,9]
max_num = max(li)
min_num = min(li)
result = sum(li)
print(max_num)
print(min_num)
print(result)

li = [1,3,6,10,100,14,5,9]
for num in li:
    if num > max_num:
        max_num = num 
    if num < min_num:
        min_num = num
print(min_num)

#find sum using loop
li = [10,20,30,40,50]
result = 0
for num in li:
    result = result + num
print(result) 

li = [2,4,6,8,10]
res = 1
for num in li:
    res = res + num
print(res)

