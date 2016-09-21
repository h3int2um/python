# Nguon bai tap: Khoa hoc Python nang cao cua kienhoc.vn: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/info
# 
# Dia chi bai tap: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/courseware/3211b8a51e434d928695a53c2b90592c/0677a96db5914fe3881d76f07e2dba95/?child=first
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# Thoi gian: Ngay 21 thang 09 nam 2016
#
# De bai:
#	File bai_tap_4.txt chua thong tin ve ten, nam sinh va diem thi cua thi sinh
#
# Yeu cau: 
#	Doc du lieu tu file .txt va luu du lieu vao co so du lieu phu hop
#	Nguoi dung nhap vao ten thi sinh va nam sinh tra ve diem thi tuong ung
#
# Phuong phap: su dung cau truc list + tuple
#

filetxt = "bai_tap_4.txt"			# Ten file chua du ten thi sinh, nam sinh va diem thi

try:
	fhand = open(filetxt)			# Mo file de doc (tham so mac dinh la r (read))
except:						# Neu file khong ton tai thi thoat khoi chuong trinh ma khong bao loi
	print "File khong ton tai!"	
	exit()

tenthisinh = raw_input("Nhap vao ten thi sinh: ")	# Nhap vao ten thi sinh

namsinh = raw_input("Nhap vao nam sinh thi sinh: ")	# Nhap vao nam sinh thi sinh

def diemthi(name, birth):		# Tim diem thi khi biet ten thi sinh va nam sinh
	thongtin = list()				# list chua thong tin sinh vien
	kt = 0						# Khong co thi sinh trong danh sanh kt = 0
	for line in fhand: 				# Doc tat ca cac dong trong file .txt
		line = line.rstrip()			# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		if line.startswith("#"): 		# Neu bat dau bang '#' thi quay lai lap tiep
			continue
		line = line.split(', ')			# Tach ten thi sinh, nam sinh va diem thi
		thongtin.append(((line[0], line[1]), line[2]))
	
	for i in thongtin:
		if (name, birth) == i[0]:		# Ten thi sinh trung co trong danh sach
			print "Diem so cua thi sinh " + name + " sinh nam " + birth + ": " + i[1] + " diem"
			kt = 1				# Co thi sinh trong danh sach
			break
			
	if kt == 0:
		print "Khong co ten thi sinh " + name + " sinh nam " + birth + " trong danh sach"
	
			
diemthi(tenthisinh, namsinh)
