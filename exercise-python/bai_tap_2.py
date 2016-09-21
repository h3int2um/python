# Nguon bai tap: Khoa hoc Python nang cao cua kienhoc.vn: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/info
# 
# Dia chi bai tap: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/courseware/2face09100b94104a893f7359f8e93c4/3624c0cb47f748c9948e5031af6e9ab5/
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# Thoi gian: Ngay 21 thang 09 nam 2016
#
# De bai:
#	File bai_tap_2.txt chua van ban "Dai cao binh Ngo" cua Nguyen Trai, viet khong dau
#	Xem chu cai thuong va chu cai in hoa la giong nhau, vi du: 'a' va 'A' duoc xem la mot
#
# Yeu cau: 
#	Hay dem so lan xuat hien cua cac chu cai Tieng Viet co trong van ban "Dai cao binh Ngo"
#
# Phuong phap:
#	demchucai_pp1() 			# Su dung list, khong su dung dictionary --> Ket qua uoc xep thu tu
#	demchucai_pp2()                         # Su dung list va dictionary		 --> Ket qua khong duoc xep thu thu tu
#

filetxt = "bai_tap_2.txt"			# Ten file chua du ten nuoc va ten thu do

try:
	fhand = open(filetxt)			# Mo file de doc (tham so mac dinh la r (read))
except:						# Neu file khong ton tai thi thoat khoi chuong trinh ma khong bao loi
	print "File khong ton tai!"	
	exit()
	
def demchucai_pp1():		# Dem so lan xuat hien cua chu cai co trong van ban theo pp 1 - su dung list, khong su dung dictionary
	lst = list()				# Chua ma ASCII cua cac chu cai
	# Ma ASCII cua cac ord('A') = 65; ord('Z') = 90 --> 'A' - 'Z' = 65 - 90
	for line in fhand:
		line = line.upper()		# Chuyen chu cai in hoa ve chu cai in hoa
		line = line.rstrip()		# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		for i in line:
			if ord(i) < 65 or ord(i) > 90:		# Loai bo cac ky tu khong thuoc 'A' -- 'Z'	
				continue
			lst.append(ord(i))
		
	lst.sort()						# Sap xep cac chu cai thu duoc theo thu tu ban chu cai

	print "So lan xuat hien cua chu cai:"
	for i in range(65,91):					# Xet cac chu cai tu 'A' - 'Z'
		if i == 70 or i == 74 or i == 87 or i == 90:	# Loai bo cac chu 'F', 'J', 'W', 'Z'
			continue
			
		print chr(i) + ": " + str(lst.count(i))		# Dem so lan xuat hien cua mot so trong list bang ham count va chuyen gia tri so ve ky tu 

		
def demchucai_pp2():		# Dem so lan xuat hien cua chu cai co trong van ban theo pp 2 - su dung list va dictionary
	lst = list()				# Chua ma ASCII cua cac chu cai
	counts = dict()
	# Ma ASCII cua cac ord('A') = 65; ord('Z') = 90 --> 'A' - 'Z' = 65 - 90
	for line in fhand:
		line = line.upper()		# Chuyen chu cai in hoa ve chu cai in hoa
		line = line.rstrip()		# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		for i in line:
			if ord(i) < 65 or ord(i) > 90:		# Loai bo cac ky tu khong thuoc 'A' -- 'Z'	
				continue
			lst.append(ord(i))

	for chucai in lst:
		chucai = chr(chucai) 				# Chuyen tu so sang ky tu
		counts[chucai] = counts.get(chucai, 0) + 1	# Dem so lan xuat hien cua ky tu trong dict counts
	
	print "So lan xuat hien cua chu cai:"	
	for k, v in counts.items():
		print k, v					# In ra so lan xuat hien cua ky tu

#demchucai_pp1() 			# Su dung list, khong su dung dictionary
demchucai_pp2() 			# Su dung list va dictionary
