"""
#list1.extend(list2)
num1 = [1,2,3,4]
num2 = [5,6,7]
print(num1 + num2)
"""

num1 = [2,4,6]
num2 = [8,10,12]
num1.extend(num2)
print(num1)

li1 = [10,20,30]
li2 = [40,50,60]
li1.extend(li2)
print(li1)

#list.insert(index,item)
"""
li = [1,2,3,4]
li.insert(1,6)
print(li)

li = [10,20,30,40]
li.insert(2,60)
print(li)

li = [4,6,8]
li.insert(3,10)
print(li)

#list.index(item)

li = [1,2,4,3,2,5]
print(li.index(2)) 

li = [1,2,3,5,3] 
print(li.index(3)) 

li = [2,3,4,5]
if 5 in li:
    print(li.index(5))

li = [3,4,5,6]
print(li.index(50))

li = [3,4,5,6]
if 50 in list:
    print(li.index(50))
"""
#list.remove(item)
li = [1,2,3,5,3]
li.remove(3)
print(li)

li = [2,4,5,6,8]
li.remove(4)
print(li)

li = [100,200,300,500]
li.remove(500)
print(li)

li = [3,4,6,7]
li.remove(3)
print(li)

#list.pop(index)
list = [3,5,7,9]
print(list.pop()) 
print(list)

list = [10,2,30,40]
print(list.pop())
print(list)

li = [4,5,6,7,8]
print(li.pop(3))
print(li)

li = [10,20,30,50]
print(li.pop(1))
print(li)

"""
li = [1,2,3,4,6]
print(li.pop(5))
print(li)
"""
#list.sort 
li = [2,4,3,1,6,5]
li.sort()
print(li)
li.reverse()
print(li)

li = [200,100,300,500,400]
li.sort()
print(li)
li.reverse()
print(li)

li = [7,5,4,2,1,10]
li.sort()
print(li)
li.reverse()
print(li)