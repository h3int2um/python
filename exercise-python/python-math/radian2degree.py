#!/usr/bin/python
#
# Thuc hanh Python: Chu de Python Math
#
# Nguon bai tap tham khao: http://www.w3resource.com/python-exercises/math/index.php
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# De bai - Bai tap 2:
#
# 	Viet chuong trinh chuyen doi tu radian sang do: Radian to Degree
#

import math

def rad2deg(rad):
	degree = rad*180/math.pi
	return degree 

# Chuong trinh chinh
radian = eval(raw_input("Radian: ")) 	# Nhap gia tri tu ban phim

radian = rad2deg(radian) 		# Thuc hien chuyen doi tu Degree to Radian

print "Expected Result: ", radian	# Hien thi ket qua

