import os
import math
def strtodigit(s):						#传入变量的名字
	x = input("请输入 "+ s +" 的值：")	#“-123.45”
	flag = False						#判定字符串里面有没有 “-”，是不是负数
	if x[0:1]=='-':
		flag = True						#True
		x=x[1:]							#“123.45”
	while not x.isdigit():				#not x(不)是数字(“-123.45”)的话
		x = input("无效的数据，请重新输入 "+ s +" 的值：")
	if flag:
		return -float(x);				#-123.45	
	else:
		return float(x);

a = strtodigit("a")
b = strtodigit("b")
c = strtodigit("c")

if a==0:
	if b==0:
		if c==0:#0=0x2+0x+0
			print("x ∈ (-∞，+∞)")
		else:#0=0x2+0x+!0 => 0 = !0(1,2,3,4)
			print("x 无解！")
	else:#0=0x2 + bx +c	->  bx+c=0  x=-c/b
		print("x=%.6f"%(-c/b))
else:# a!=0 一元二次
	d = b*b-4*a*c
	if d<0:
		print("x 无解！")
	else:
		x1 = (-b + math.sqrt(d))/(2*a)
		x2 = (-b - math.sqrt(d))/(2*a)
		print("x1 = %.6f , x2 = %.6f"%(x1,x2))
os.system("pause")
