#!/usr/bin/python
#
# Thuc hanh Python: Chu de Python Math
#
# Nguon bai tap tham khao: http://www.w3resource.com/python-exercises/math/index.php
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# De bai - Bai tap 1:
#
#	Viet chuong trinh chuyen doi tu do sang radian: Degree to Radian
#

import math

def deg2rad(degree):
	radian = degree*math.pi/180
	return radian


# Chuong trinh chinh

degree = eval(raw_input("Degree: ")) 	# Nhap gia tri tu ban phim

radian = deg2rad(degree) 		# Thuc hien chuyen doi tu Degree to Radian

print "Expected Result in radians: ", radian 	# Hien thi ket qua

