#!/usr/bin/python
#
# Thuc hanh Python: Chu de Python Math
#
# Nguon bai tap tham khao: http://www.w3resource.com/python-exercises/math/index.php
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# De bai - Bai tap 3:
#
#	Viet chuong trinh tinh dien tich hinh thang
#

def AreaOfTrap(height, basefirst, basesecond):
	area = (basefirst + basesecond)*height/2.0
	return area


# Chuong trinh chinh

height = eval(raw_input("Height: ")) 			# Nhap vao chieu cao hinh thang

basefirst = eval(raw_input("Base, first value: "))    	# Nhap vao do dai canh day thu nhat

basesecond = eval(raw_input("Base, second value: ")) 	# Nhap vao do dai canh day thu hai


area = AreaOfTrap(height, basefirst, basesecond)	# Thuc hien chuyen doi tu Degree to Radian

print "Expected Output: Area is: ", area 		# Hien thi ket qua

