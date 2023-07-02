li = ['apple','banana','orange','mango']
fruits = [fruit.capitalize() for fruit in li] 
print(fruits)
li_len= [len(x) for x in li]
print(li_len)

fruit = ['APPLE','BANANA','ORANGE']
x = [f.lower() for f in fruit]
print(x)


cube_list = [x*x*x for x in range(1,11)]
print(cube_list) 
odd_num = [x for x in range(1,11) if x%2 == 1]
print(odd_num) 
cube_list= [x*x*x for x in range(1,11) if x%2 == 1]  # x**3
print(cube_list)   
even_num = [x for x in range(1,20) if x%2 == 0]
print(even_num)


