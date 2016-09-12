# Các cấu trúc điều khiển trong Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 09 tháng 09 năm 2016

## Lưu ý

* Khi sử dụng các cấu trúc điều khiển, kết thúc mỗi cấu trúc là dấu `:`

* Bên trong mỗi cấu trúc là khối lệnh.

## Lệnh if

* Cấu trúc 1: 

	- Cú pháp:
			
			if dieu_kien:
		
				khoi_lenh
				
	- Giải thích:
			
		+ Nếu biểu thức `dieu_kien` đúng thì thực hiện các lệnh trong `khoi_lenh`.
		
		+ Nếu biểu thức `dieu_kien` sai thì bỏ qua các lệnh trong `khoi_lenh`.
		
	- Ví dụ: Kiểm tra một số là số âm hoặc số dương hoặc bằng 0.
	
		+ Viết cho biểu thức điều kiện đúng:
		
				# Kiem tra mot so la so am hoac so duong hoac bang 0
			
				# Ten file kiemtraso_1.py
			
				a = 1
			
				if a > 0:
			
					print 'So duong'
		
		+ Thực thi script `kiemtraso_1.py`:
		
				$ python kiemtraso_1.py
				
				So duong
				
		+ Viết cho biểu thức điều kiện sai:
		
				# Kiem tra mot so la so am hoac so duong hoac bang 0
			
				# Ten file kiemtraso_2.py
			
				a = -1
			
				if a > 0:
			
					print 'So duong'
				
				print 'Ket thuc chuong trinh'
				
		+ Thực thi script `kiemtraso_2.py`:
		
				$ python kiemtraso_2.py
				
				Ket thuc chuong trinh
				
			Do biểu thức điều kiện sai nên không thực hiện các lệnh trong cấu trúc `if` ở script `kiemtraso_2.py`.
	
* Cấu trúc 2:

	- Cú pháp:
	
			if dieu_kien:
		
				khoi_lenh_1
			
			else:
			
				khoi_lenh_2
				
	- Giải thích:
	
		+ Nếu biểu thức `dieu_kien` đúng thì thực hiện các lệnh trong `khoi_lenh_1`.
		
		+ Nếu biểu thức `dieu_kien` sai thì thực hiện các lệnh trong `khoi_lenh_2`.
		
	- Ví dụ: Kiểm tra một số là số âm hoặc số dương hoặc bằng 0.
			
		+ Viết cho biểu thức điều kiện đúng:
		
				# Kiem tra mot so la so am hoac so duong hoac bang 0
			
				# Ten file kiemtraso_3.py
			
				a = 1
			
				if a > 0:
			
					print 'So duong'
					
				else:
				
					print 'So khong duong'
			
		+ Thực thi script `kiemtraso_3.py`:
		
				$ python kiemtraso_3.py
				
				So duong
				
		+ Viết cho biểu thức điều kiện sai:
		
				# Kiem tra mot so la so am hoac so duong hoac bang 0
			
				# Ten file kiemtraso_4.py
			
				a = -1
			
				if a > 0:
			
					print 'So duong'
				
					print 'Ket thuc chuong trinh'
				
		+ Thực thi script `kiemtraso_4.py`:
		
				$ python kiemtraso_4.py
				
				Ket thuc chuong trinh
	
			
* Cấu trúc 3:
	
	- Cú pháp:

			if dieu_kien_1:
			
				khoi_lenh_1
			
			elif dieu_kien_2:
		
				khoi_lenh_2
			
			elif dieu_kien_3:
		
				khoi_lenh_3
			
			...
		
			else:			# Có thể bỏ qua
				
				khoi_lenh_cuoi_cung
			
	- Giải thích:
		
		+ Khi `dieu_kien_1` đúng: thì thực hiện các lệnh trong `khoi_lenh_1`.
		
		+ Khi `dieu_kien_1` sai thì kiểm tra `dieu_kien_2`, nếu `dieu_kien_2` đúng thì thực hiện các lệnh 
		trong `khoi_lenh_2`.
		
		+ Khi `dieu_kien_1` và `dieu_kien_2` cùng sai thì kiểm tra `dieu_kien_3`, nếu `dieu_kien_3` đúng thì thực hiện 
		các lệnh trong `khoi_lenh_3`.
		
		+ Quá trình kiểm tra tiếp tục các các điều kiện còn lại: `...`
		
		+ Nếu cấu trúc có `else`: mà tất cả các điều kiện đều sai thì thực hiện các lệnh trong `khoi_lenh_cuoi_cung`.
		
	- Nhận xét: Với cấu trúc 3, chúng ta xét được tất cả các trường hợp xảy ra của một điều kiện.
	
	- Ví dụ: Xét dấu của một số được nhập từ bàn phím.
	
		+ Viết script `kiemtraso_5.py`:
		
				# Kiem tra mot so la so am hoac so duong hoac bang 0
			
				# Ten file kiemtraso_5.py
			
				a = int(raw_input('Nhap vao mot so: '))		# Chuyen sang gia tri so de so sanh
			
				if a > 0:
			
					print `So duong`
			
				elif a < 0:
				
					print `So am`
				
				else:
				
					print `So bang 0`
			
		+ Thực thi script `kiemtraso_5.py`:
					
				$ python kiemtraso_5.py
				
				Nhap vao mot so: 1
				
				So duong
				
				
				$ python kiemtraso_5.py
			
				Nhap vao mot so: -1
				
				So am
				
				
				$ python kiemtraso_5.py
				
				Nhap vao mot so: 0

				So bang 0
				
## Cấu trúc lặp while

* Cú pháp:

		bien_khoi_tao
		
		while dieu_kien:
	
			khoi_lenh
		
			bien_thay_doi_lien_tuc	# Không bắt buộc với vòng lặp vô tận
		
* Giải thích:

	- Lệnh `bien_khoi_tao` để bắt đầu điều kiện vòng lặp.

	- Nếu `dieu_kien` còn đúng, thì thực hiện các lệnh trong `khoi_lenh`.
	
	- Lệnh `bien_thay_doi_lien_tuc` làm ảnh hưởng đến điều kiện, đến một thời điểm nào đó, `dieu_kien` không còn đúng, 
	thoát khỏi cấu trúc `while`.
	
	- Với những vòng lặp vô tận: không cần thiết đến  `bien_khoi_tao` và `bien_thay_doi_lien_tuc`.
	
* Ví dụ: In ra các số từ 1 - 5.

	- Viết script `inso_1.py`:
		
			# In ra cac so tu 1 - 5
		
			# Ten file inso_1.py
		
			i = 1
		
			while i <= 5:
		
				print i
			
				i = i + 1
				
	- Thực thi script `inso_1.py`:
	
			$ python inso_1.py
			
			1
			
			2
			
			3
			
			4
			
			5

* Nhận xét: với cấu trúc lặp `while` không cần phải biết chính xác số lần lặp.

## Cấu trúc lặp for

* Lệnh `range`:

	- Lệnh `range(n)`: tạo dãy số từ `0 - (n-1)`, giá trị lớn nhất trong dãy luôn nhỏ hơn `n`.
				
			>>> range(10)
			
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
			
	- Lệnh `range(start,n)`: tạo dãy số từ `start - (n-1)`, giá trị lớn nhất trong dãy luôn nhỏ hơn `n`.
	
			>>> range(5,10)
			
			[5, 6, 7, 8, 9]
			
	- Lệnh `range(start,n,step)`: tạo một dãy số từ `start - (n-1)` với khoảng cách là `step`.
	
			>>> range(1,10,2)
			
			[1, 3, 5, 7, 9]
			
			>>> range(1,10,-2)
			
	- Lệnh `range(n,stop,step)`: tạo một dãy số từ `n - stop` với khoảng cách là `step`, giá trị nhỏ nhất trong dãy 
	luôn lớn hơn giá trị `stop`.
	
			>>> range(10,0,-2)
			
			[10, 8, 6, 4, 2]
			

* Cú pháp:

		for i in range(n):
		
			khoi_lenh
	
* Giải thích:

	- Với lệnh `range(n)`: 
	
		+ Biến chạy `i`: chạy từ `0 - (n-1)`, mỗi lần chạy thực hiện `khoi_lenh` một lần.
		
		+ Thực hiện `khoi_lenh` với `n` lần rồi thoát khỏi vòng lặp `for`.
		
	- Tương tự với các tham số khác cho lệnh `range`.
	
* Ví dụ: In ra các số từ 1 - 5.

	- Viết script `inso_2.py`:
		
			# In ra cac so tu 1 - 5
		
			# Ten file inso_2.py
		
			for i in range(1,6):
			
				print i
				
				
	- Thực thi script `inso_2.py`:
	
			$ python inso_1.py
			
			1
			
			2
			
			3
			
			4
			
			5
			
* Nhận xét: với cấu trúc lặp `for`, chúng ta biết được chính xác số lần lặp.

## Thoát khỏi vòng lặp while hoặc for

* Dùng lệnh `break` để thoát khỏi vòng lặp `while` hoặc `for` gần nhất.

* Ví dụ:
		
	- Viết script `thoatkhoi_vonglap.py`:
	
			# Thoat khoi vong lap voi lenh break
		
			# Ten file thoatkhoi_vonglap.py
			
			for i in range(1, 10):
		
				print i
				
				if i >= 5:
				
					break
					
	- Thực thi script `thoatkhoi_vonglap.py`:
	
			$ python thoatkhoi_vonglap.py
			
			1
			
			2
			
			3
			
			4
			
			5
	- Nhận xét: nhờ có lệnh `break`, thay vì in ra dãy số từ `1 - 9` thì chương trình in ra dãy số từ `1 - 5` do có điều kiện 
	giới hạn `i > = 5`.
								
		
		
		

		
