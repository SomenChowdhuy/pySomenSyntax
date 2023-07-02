num = (2,4,6,8)
print(type(num))
print(num[0],num[2],num[-1])

tpl = (10,20,30)
for i in tpl:
    print(i)
print(tpl,type(tpl))

#list is changeable(mutable) , tuple is not changeable
li = [3,4,5]
tpl = (3,4,5)
li[2] = 6
print(li)
#tpl[2] = 6
#print(tpl) 

print(dir(tuple))
tpl = (1,2,5,6,2)
print(tpl,tpl.count(2))
print(tpl.count(6))
print(tpl.count(1))

#unpack
tpl = (1,2,3,4,5)
a,b,c,d = tpl
print(a,b,c,d)

while True:
    print