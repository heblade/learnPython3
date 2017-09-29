import keyword
#第一个注释
print("Hello python 3.6")
print(keyword.kwlist)

word='字符串'
sentence="这是一个句子"
paragraph = """这是一个段落，
可以由多行组成"""

print(word, '\n', sentence, '\n', paragraph)

count = 100
miles = 1000.0
name = "runoob"

print(count)
print(miles)
print(name)

intNumber, floatNumber, boolValue, complexValue = 20, 5.5, True, 4+3j
print(type(intNumber), type(floatNumber), type(boolValue), type(complexValue))

print("5+4=", 5+4)
print("4.3-2=",4.3-2)
print("3*7=",3*7)
print("2/4=", 2/4)
print("2//4=", 2//4)
print("17%3=", 17%3)
print("2**5=", 2**5)

testStr = "厉害了"
print(testStr)
print(testStr[2:])
print(testStr * 2)
print (testStr, "Test")
print (testStr + "Test")

#Python 使用反斜杠(\)转义特殊字符，
# 如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print("Inter\net")
print(r"Inter\net")

print("List（列表） 是 Python 中使用最频繁的数据类型")
list = ['abcd', 785, 2.23, 'runoob', 70.2]
tinylist = [123, 'Blade']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

print("元组（tuple）与列表类似，不同之处在于元组的元素不能修改。"
      "元组写在小括号(())里，元素之间用逗号隔开")
tuple = ('abcd', 332, 1.88, 'Jodan', 110.22)
tinyTuple = (332, 'Projector')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)

print("集合（set）是一个无序不重复元素的序列")
student = {'Tom', 'Jean', 'Mary', 'Tom', 'Jack', 'Rose'}
# 输出集合，重复的元素被自动去掉
print(student)

if('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

print('set可以进行集合运算')
setA = set('abracadabra')
setB = set('alacazam')
print('setA', setA)
print('setB', setB)

print('setA-setB', setA-setB)
print('setA | setB', setA | setB)
print('setA & setB', setA & setB)
print('setA ^ setB', setA ^ setB)

print("字典（dictionary）是Python中另一个非常有用的内置数据类型")
print("列表是有序的对象结合，字典是无序的对象集合。"
      "两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。")
print("字典是一种映射类型，字典用'{ }'标识，它是一个无序的键(key) : 值(value)对集合")
print("键(key)必须使用不可变类型")
print("在同一个字典中，键(key)必须是唯一的")
dict = {}
dict['one'] = '1 - bad'
dict[2] = '2 - good'
tinydict = {'name': 'Blade', 'code': '186766', 'address': 'shenzhen'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())