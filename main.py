# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import keyword
print(keyword.kwlist)

print(520)
print(85.2)
print("PyCharm")
print('PyCharm')
print(3+1)
print(3+1)

item_one=0
item_two=0
item_three=0
total = item_one\
        + item_two \
        + item_three
print(total)
#将数据输出到文件中
fp=open('E:/var/text.txt','a+')#'a+':若指定文件不存在则创建该文件
print('helloworld',fp)
print('helloworld',file=fp)#将数据输出到fp指定的文件中
fp.close()

print('hello','world','Python')

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')
print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')
#原字符，不希望字符串中的转义字符起作用，在字符串之前加上r或R
print(r'hello\rworld')
#最后一个字符不能为单数个\
#print(r'hello\rworld\')
print(r'hello\rworld\\\\')
#print(r'hello\rworld\\\')


#二进制以0b开头，八进制以0o开头，十六进制以0x开头
print(chr(0b100111001011000))
print(ord('承'))

n=3
print(n,type(n))

print('十进制',118)
print('二进制',0b10101111)
print('八进制',0o176)
print('十六进制',0x1eaf)
print('十六进制',0x1EAF)

#浮点型计算导入模块decimal
print(1.1+2.2)
print(1.1+2.1)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔型True-->1;False-->0
print(True+1)
print(False+1)

#字符串，'xxx'    "xxx"     '''xxx'''     """xxx"""
str1='人生苦短，我用python'
str2="人生苦短，我用python"
str3='''人生苦短，我用python'''
str3='''人生苦短，
我用python'''
str4="""人生苦短，
我用python"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))