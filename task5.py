class Person(object):  # 定义一个父类
    def talk(self):  # 父类中的方法
        print("person is talking....")
class Chinese(Person):  # 定义一个子类， 继承Person类
    def walk(self):  # 在子类中定义其自身的方法
        print('is walking...')
c = Chinese()
c.talk()  # 调用继承的Person类的方法
c.walk()  # 调用本身的方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'
    def talk(self):
        print("person is talking....")
class Chinese(Person):
    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language  # 定义类的本身属性
    def walk(self):
        print('is walking...')
class American(Person):
    pass
c = Chinese('bigberg', 22, 'Chinese')
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'
    def talk(self):
        print("person is talking....")
class Chinese(Person):
    def __init__(self, name, age, language):
        Person.__init__(self, name, age)
        self.language = language
        print(self.name, self.age, self.weight, self.language)
    def talk(self):  # 子类 重构方法
        print('%s is speaking chinese' % self.name)
    def walk(self):
        print('is walking...')
c = Chinese('bigberg', 22, 'Chinese')
c.talk()
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1) )
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
line = "Cats are smarter than dogs"
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print( "match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print( "search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
import urllib
response = urllib.urlopen('http://localhost:8080/jenkins/api/json?pretty=true')
print(response.read())
import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
data2 = r2.read()
conn.close()
import httplib
import urllib
params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",  "Accept": "text/plain"}
conn = httplib.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
data = response.read()
print (data)
conn.close()
