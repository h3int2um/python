# Nguon bai tap: Khoa hoc Python nang cao cua kienhoc.vn: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/info
# 
# Dia chi bai tap: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/courseware/242657a851844c7ca71581af6e53c044/45e51fcb3be646fcb720946a4f645707/
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# Thoi gian: Ngay 21 thang 09 nam 2016
#
# De bai:
#	File bai_tap_3.txt chua thong tin ve ten nuoc va ten thu do
#
# Yeu cau: 
#	Nguoi dung nhap vao ten nuoc va tra ve ten thu do cua nuoc do
#	Neu nuoi dung nhap vao ten nuoc khong co trong danh sach thi bao loi: "Ten nuoc khong hop le"
#
# Phuong phap: su dung cau truc dictionary
#

filetxt = "bai_tap_3.txt"			# Ten file chua du ten nuoc va ten thu do

try:
	fhand = open(filetxt)			# Mo file de doc (tham so mac dinh la r (read))
except:						# Neu file khong ton tai thi thoat khoi chuong trinh ma khong bao loi
	print "File khong ton tai!"	
	exit()

c = raw_input("Nhap vao ten quoc gia: ")	# Nhap vao ten quoc gia can biet thu do

def tennuoc_tenthudo(country):		# Tim ten quoc gia co trong file hay khong
	d = dict()				# Tao mot dict rong
	for line in fhand: 			# Doc tat ca cac dong trong file .txt
		line = line.rstrip()		# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		line = line.split(',')		# Tach ten nuoc va ten thu do ra 2 phan
		d[line[0]] = line[1]

	if country in d:			# Kiem tra ten quoc gia co trong file hay khong
		print d[country]
	else:
		print "Ten nuoc khong hop le" 

tennuoc_tenthudo(c)				# Kiem tra ten nuoc co trong file .txt hay khong
