#zfill 将内容用0填充到指定的长度 从左开始
i="111"
res=i.zfill(5)  #把字符串填充到5位  如果超过5位则不填充
print(res)

# center将字符串使用指定的符号 居中显示 填充字符多的留在后面  (字符/2余数放在后面 变量放在中间)
res=i.center(10,"*") #  填充字符(可以使用空格)
print(res)

#ljust 将字符串使用指定的符号在变量右边填充(也就是说变量写在左边填充写在右边)
res=i.ljust(10,"#")
print(res)

#rjust 将字符串使用自定的符号在变量的左边填充(变量写在填充字符的右边)
res=i.rjust(10,"@")
print(res)
#任何填充字符只能使用一个字符填充

#strip 去除两侧指定的字符串  可以使用单个字符串 也可以使用多个字符串
i="@@@hello world@@@@@o"
res=i.strip("@o")
print(res)

#lstrip去除左边的指定的字符
res=i.lstrip("@")
print(res)

#rstrip去除右边指定的字符
res=i.rstrip("@o")
print(res)

#字符替换操作
i="hello world@"
#                 旧字符  新字符  去掉字符串
res="".maketrans("hello","Hello","@")   #将变量中的字符串提取出来 转换成编码格式 替换的字符串长度必须相等
res1=i.translate(res)                #使用新的变量接受旧变量.translate(编码变量)
print(res1)
#format 字符串格式化操作
i="{}去{}做了{}"
res=i.format("你","外边","什么?")  #有几个括号就填写几个参数
print(res)

i="{2}去{1}做了{2}"  #使用序号的方式来标注
i="{0}去{1}做了{2}"  #使用序号的方式来标注
res=i.format("你","外边","什么?")   # 序号顺序可以随机 但是必须是按照接受参数的顺序
print(res)

i="{no1}去{no2}做了{no3}"  #使用参数名进行标注  可以不按照顺序
res=i.format(no1="你",no2="外边",no3="什么?")
print(res)

i="{0[0]}去{0[1]}做了{0[2]}"
res=i.format(["你","外边","什么"])  #使用列表的方式进行传递
print(res)

#限定号的使用  < ^ >
#填充对齐符号          :填充符\填充左边\填充完总的字符个数      默认为空格
var="现在很多小店都用{:@>10}提升味道,所以当你吃完还想吃,请注意"
res=var.format("罂粟壳")
print(res)

#精度计算   :.几f就是几位  冒号后面有小数点
var="派的值{:.3f}"
res=var.format(3.1415926)
print(res)

#字符串进制转换  o d x b
var="杨俊的体重是{:x}公斤"
res=var.format(95)
print(res)

#金融符号 ,
var="杨俊的身价是{:,}公斤"
res=var.format(123456789)
print(res)

"""-------------------------------------------------------------------"""
#列表的内容

var=[]  #空列表
var=list() #空列表

#声明多个元素的列表
#    0        1        2
var=['hello','world','!']
#     -3       -2      -1
print(var,type(var))

#列表基本操作  访问  修改  删除
print(var[0])  #访问第0个键位

var[0]="Hello"  #修改第0个键位
print(var)

del var[2]  #删除第2个键位
print(var)

#序列操作
listvar1=['张三','李四','王五']
listvar2=['赵六','张七']

#相加操作 两个列表相加
res=listvar1+listvar2
print(res)

#相乘操作
res=listvar2*3
print(res)

#分片操作 取范围
res=listvar1[:] #全部
res=listvar1[1:] #从第1个键位开始 到结束
res=listvar1[:3] #第三个键位之前的数据
res=listvar1[1:3] #从第一个键位到第三个键位
print(res)

#成员检测 in 和 not in
var1="张三" in listvar1  #在里面
print(var1)

var1="张三" not in listvar1 #不在里面
print(var1)

#遍历列表
for i in listvar1:  #for 遍历
    print(i)

i=0
while i<len(listvar1):  #while 遍历
    print(listvar1[i])
    i+=1

#多曾列表遍历 等长二级列表  就是子列表的长度是相等的 都是两个 或多个
var1=[["hello","1"],["world","2"],["!","3"]]
for i,z in var1:
    print(i,z)
#不等长二级列表 长度不相等 需要嵌套 最长子列表的层数
for i in var1:
    for z in i:
        print(z)

#列表推导式
var1=['张安',"李四","王五"]
#   符号 变量 符号  for循环
res=["@"+i+"@" for i in var1]
print(res)
var1=[1,2,3,4,5,6,7,8,9]
res=[i*3 for i in var1]  #变量i*3 for循环
print(res)

#带有判断条件的推导式语句
var1=[1,2,3,4,5,6,7,8,9]
print(var1)
res  = [i for i in var1 if i%2==1]
print(res)
#声明一个多个人名组成的列表  找到3个字的
var=["张三","李四","高小松"]
res=[i for i in var if len(i)==3 ]
print(res)

#多循环推导式
var=[35,36,37,38,39]
var1=["黄色","白色","红色"]
res=[str(i)+z for i in var for z in var1]  #需要转换成字符串
print(res)

#男生4人女生5人相互见面
var=["男1","男2","男3","男4"]
var2=["女1","女2","女3","女4","女5"]
res=[i+":"+z for i in var for z in var2]
print(res)
#有判断条件的多循环列表推导式                 变量.(键位)   变量.(键位)
res=[i+":"+z for i in var for z in var2 if var.index(i)==var2.index(z)]  #两个列表的长度必须相等 否则多余的丢弃
print(res)

#列表函数
#在列表末尾添加元素 直接修改列表 append
var=["张三","李四","王五"]
print(var)
var.append("赵六")
print(var)

#在列表指定的位置添加元素
var.insert(2,"hello")
print(var)

#删除指定位置的元素
var.pop(0)  #默认删除-1键位
print(var)

#删除列表中指定的键名
var.remove("hello")
print(var)

#清空列表
var.clear()
print(var)

#复制列表
res=var.copy()
print(res)

#计算出现的次数
var=["张三","李四","王五"]
res=var.count("张三")  #只能统计整体
print(res)

#将一个列表合并到另一个列表
var2=["hello","world"]
var.extend(var2)  # var=var+var2 结果相同
print(var)

#获取指定字符串的索引
res=var.index("王五")
print(res)

#reverse 列表反向操作
var=["今","生","为","你"]
print(var)
var.reverse()
print(var)

#自定义排序规则

def my(num):
    res=num%2  #求余数得到的结果
    return res
i=[1,2,3,4,5,6,7,8,9]
i.sort() #默认升序排列 reverse为降序
print(i)

i.sort(key=my)  #求余数得到的结果升序排列
i.sort(key=my,reverse=True) #求余数得到的结果降序排列
print(i)
