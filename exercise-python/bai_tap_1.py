# Nguon bai tap: Khoa hoc Python nang cao cua kienhoc.vn: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/info
# 
# Dia chi bai tap: http://study.kienhoc.vn/courses/course-v1:UMICH+CS201+2016_T3/courseware/69fc4a28a278432997bb5e491b717a2d/9624fb13a5c842f2ba3a5b5bebe43df6/
#
# SVTH: Thi Minh Nhut - Email: thiminhnhut@gmail.com
#
# Thoi gian: Ngay 20 thang 09 nam 2016
#
# De bai:
#	File bai_tap_1.txt chua thong tin ve email tu server. 
#	Moi email duoc danh gia voi chi so spam luu o dong bat dau bang "X-DSPAM-Confidence".
#	Vi du, chi so spam cua email dau tien la: 0.8475.
#
# Yeu cau: 
#	Hay viet chuong trinh duyet file bai_tap_1.txt, tinh gia tri trung binh cua cac chi so spam roi in ra man hinh
#
# Phuong phap: thuc hien 4 phuong phap voi cac giai thuat khac nhau
#
#	tong_chiso_spam_pp1(str_search)		# Khong su dung continue va khong su dung list
#
#	tong_chiso_spam_pp2(str_search)		# Su dung continue va khong su dung list
#	
#	tong_chiso_spam_pp3(str_search)		# Khong su dung continue va su dung list
#	
#	tong_chiso_spam_pp4(str_search)		# Su dung continue va su dung list
#

filetxt = "bai_tap_1.txt"			# Ten file chua du lieu spam mail

try:
	fhand = open(filetxt)			# Mo file de doc (tham so mac dinh la r (read))
except:						# Neu file khong ton tai thi thoat khoi chuong trinh ma khong bao loi
	print "File khong ton tai!"	
	exit()
	
str_search = "X-DSPAM-Confidence"		# Dong co chuoi nay duoc la dong spam


def tong_chiso_spam_pp1(text_spam):	# Tinh trung binh tong chi so spam theo pp 1 - Khong dung continue va list
	count = 0                               # Khoi tao gia tri cho bien dem
	s = 0                                   # Khoi tao gia tri cho bien tong

	for line in fhand:                      # Doc tat ca cac dong trong file .txt
		line = line.rstrip()            # Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		if line.startswith(text_spam):	# Neu dong bat dau bang chuoi trong bien text_spam
			count = count + 1	# Dem so dong bat dau bang chuoi trong bien text_spam
			
			# Dong co chi so spam duoc dinh dang:   X-DSPAM-Confidence: 0.8879 (vi du)
			# Tinh tong cac so o cuoi chuoi, phan chu bo di khong can den
			s = s + float(line[len(text_spam)+2:])  # Tinh tong cua cac chi so spam (chuyen chuoi sang so thuc de tinh)

	print "So dong bat dau bang " + text_spam + ": " + str(count) + " dong" + " (PP 1)"
	
	try:
		print "Trung binh chi so spam la: " + str(s/count) + " (PP 1)"
	except:
		print "Khong co noi dung spam"


def tong_chiso_spam_pp2(text_spam):	# Tinh trung binh tong chi so spam theo pp 2 - Dung continue khong dung list
	count = 0				# Khoi tao gia tri cho bien dem 
	s = 0					# Khoi tao gia tri cho bien tong

	for line in fhand:			# Doc tat ca cac dong trong file .txt
		line = line.rstrip()		# Loai bo ky tu trong (vi du: \n,...) o cuoi dong

		if not line.startswith(text_spam):	# Neu dong khong bat dau bang chuoi trong bien text_spam
			continue			# Quay tro lai vong lap for ma khong thuc hien cac lenh duoi

		count = count + 1			# Dem so dong bat dau bang chuoi trong bien text_spam

		# Dong co chi so spam duoc dinh dang:	X-DSPAM-Confidence: 0.8879 (vi du)
		# Tinh tong cac so o cuoi chuoi, phan chu bo di khong can den
		s = s + float(line[len(text_spam)+2:])	# Tinh tong cua cac chi so spam (chuyen chuoi sang so thuc de tinh)
		
	print "So dong bat dau bang " + text_spam + ": " + str(count) + " dong" + " (PP 2)" 
	
	try:
		print "Trung binh chi so spam la: " + str(s/count) + " (PP 2)"
	except:
		print "Khong co noi dung spam"


def tong_chiso_spam_pp3(text_spam):	# Tinh trung binh tong chi so spam theo pp 2 - Khong dung continue va su dung list
	s = list()				# Khoi tao list rong

	for line in fhand:                      # Doc tat ca cac dong trong file .txt
		line = line.rstrip()           	# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		if line.startswith(text_spam):  # Neu dong bat dau bang chuoi trong bien text_spam
			# Dong co chi so spam duoc dinh dang:   X-DSPAM-Confidence: 0.8879 (vi du)
			chiso_spam = line.split(':')	# Tach rieng phan chu va phan so ra
			s.append(float(chiso_spam[1]))  # Them chi so spam vao list (phan so cho chi so la 1)
			
	print "So dong bat dau bang " + text_spam + ": " + str(len(s)) + " dong" + " (PP 3)"
	
	try:
		print "Trung binh chi so spam la: " + str(sum(s)/len(s)) + " (PP 3)"
	except:
		print "Khong co noi dung spam"
		
		
def tong_chiso_spam_pp4(text_spam):	# Tinh trung binh tong chi so spam theo pp 2 - Khong dung continue va su dung list
	s = list()					# Khoi tao list rong

	for line in fhand:                      	# Doc tat ca cac dong trong file .txt
		line = line.rstrip()           		# Loai bo ky tu trong (vi du: \n,...) o cuoi dong
		if not line.startswith(text_spam):  	# Neu dong khong bat dau bang chuoi trong bien text_spam
			continue			# Quay tro lai vong lap for ma khong thuc hien cac lenh duoi
			
		# Dong co chi so spam duoc dinh dang:   X-DSPAM-Confidence: 0.8879 (vi du)
		chiso_spam = line.split(':')		# Tach rieng phan chu va phan so ra 
		s.append(float(chiso_spam[1]))  	# Them chi so spam vao list, phan so co chi so la 1
		
	print "So dong bat dau bang " + text_spam + ": " + str(len(s)) + " dong" + " (PP 4)"
	
	try:
		print "Trung binh chi so spam la: " + str(sum(s)/len(s)) + " (PP 4)"
	except:
		print "Khong co noi dung spam"

#tong_chiso_spam_pp1(str_search)		# Khong su dung continue va khong su dung list
#tong_chiso_spam_pp2(str_search)		# Su dung continue va khong su dung list
#tong_chiso_spam_pp3(str_search)               	# Khong su dung continue va su dung list
tong_chiso_spam_pp4(str_search) 		# Su dung continue va su dung list
