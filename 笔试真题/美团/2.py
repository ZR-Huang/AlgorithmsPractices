'''
一段伪代码：
while True:
    x = (a*x+b) % m
    print(x)
endwhile
假如a=2, b=1, m=5, x=2
会输出一个循环序列：0，1，3，2，0，1，3，2，0，1，3，2，……
其中0,1,3,2为最短重复序列，长度为4
在给定任意，a,b,m,x的情况下，求这段伪代码的最短重复序列的长度
'''
# AC
s = input()
a, b, m, x = list(map(int, s.strip().split(" ")))
x = (a * x + b) %m
prefix = [x]
buff = []
i = 0
while True:
    x = (a * x + b) %m
    if prefix[i] != x:
        prefix.append(x)
    elif i < len(prefix):
        if i == len(prefix)-1:
            break
        buff.append(x)
        i += 1
    else:
        prefix += buff
        buff = []
        i = 0
    
print(len(prefix))