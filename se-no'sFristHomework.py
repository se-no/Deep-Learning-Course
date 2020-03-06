import os
import math
def strtodigit(s):						
	x = input("请输入 "+ s +" 的值：")	
	flag = False						
	if x[0:1]=='-':
		flag = True						
		x=x[1:]							
	while not x.isdigit():				
		x = input("无效的数据，请重新输入 "+ s +" 的值：")
	if flag:
		return -float(x);				
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
	else:
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
