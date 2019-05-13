list1 = ['Google', 'tango', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print ("原始列表 : ", list1)
del list1[2]
print ("删除第三个元素 : ", list1)
a=len([1, 2, 3])
print(a)
b=[1, 2, 3] + [4, 5, 6]
print(b)
c=['Hi!'] * 4
print(c)
d= 3 in [1, 2, 3]
print(d)
for x in [1, 2, 3]:
    print(x, end=" ")
print(list1[1:])
print(list1[2])
print(list1[-2])
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
a=len(x)
b=max(x)
c=min(x)
x.append(4)
x.extend(list1)
x.pop(index=x.index(max(x)))
x.remove(index=x.index(min(x)))
x.sort()
x.reverse()
print(x)
