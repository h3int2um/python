# Xây dựng hàm trong Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 13 tháng 09 năm 2016

## Giới thiệu về hàm

* Khi cần thực hiện một công việc lập đi lập lại nhiều lần, chúng ta cần xây dựng các hàm để thực hiện chức năng đó, 
gọi lại với tên ngắn gọn thay vì phải viết cả một khối lệnh lặp đi lặp lại nhiều lần.

* Việc sử dụng hàm có một số lợi ích sau:

	- Tiết kiệm thời gian và công sức lập trình.
	
	- Chương trình dễ quản lý.
	
	- Thực hiện nhiều khối lệnh với một dòng lệnh: gọi lại hàm.
	
	- Có thể sử dụng các hàm này để xuất thành các module (sẽ đề cập ở phần sau).
	
* Một số cấu trúc của hàm:

	- Hàm có hoặc không có đổi số.
	
	- Hàm có hoặc không có kết quả trả về.

## Lưu ý

* Khi xây dựng hàm, sau định nghĩa tên hàm là dấu `:`

* Vị trí của hàm: thường đặt trước chương trình chính.

* Tên hàm: tên hàm được đặt theo quy tắc

	- Quy tắc giống như đặt tên cho biến: không chứa ký tự đặc biệt, không bắt đầu bằng số, không chứa dấu cách, 
	không trùng với từ khóa, không trùng với tên biến.
	
	- Tên hàm không trùng với các hàm đã có sẳn.
	
	- Tên hàm nên gợi nhớ đến chức năng của hàm.
	
* Xây dựng hàm nên áp dụng được cho trường hợp tổng quát: người dùng chỉ việc truyền tham số vào và nhận kết quả trả về, 
hàm áp được cho đa số trường hợp, áp dụng được cho mọi trường hợp thì càng tốt.

* Khi xây dựng hàm cần có những dòng chú thích về *cách sử dụng* và *chức năng của hàm* một cách rõ ràng để tiện cho việc kiểm tra sau này.

## Biến toàn cục và biến cục bộ

* Biến toàn cục: biến ảnh hưởng đến mọi hàm con và chương trình chính.

* Biến cục bộ: biến chỉ ảnh hưởng đến phạm vi trong chương trình con.

## Xây dựng hàm trong Python

* Hàm không có đối số:
	
	- Cú pháp:

			def tenham():
		
				Khối lệnh thực hiện chức năng
				
	- Ví dụ: viết hàm có tên `hello` (không có đối số) với nội dung là in ra dòng thông báo `Hello Python!` khi hàm được gọi.
	
		+ Viết script `def-hello-1.py`
	
				# Ten file: def-hello-1.py
			 
				# Giai thich: 
			
				# Cu phap: Ham khong co doi so 
			
				# Chuc nang: In ra thong bao 'Hello Python!'
			
				def hello():
			
					print 'Hello Python!'
				
				# Chuong trinh chinh
			
				hello()
				
		+ Thực thi script `def-hello-1.py`:
		
				$ python def-hello-1.py
				
				Hello Python!
				
* Hàm có đối số:

	- Cú pháp:

			def tenham(danhsachdoiso):
		
				Khối lệnh thực hiện chức năng
				
		Danh sách đối số cách nhau bằng dấu phẩy ','
				
	- Ví dụ: viết hàm có tên `hello` (có một đối số là `name` - kiểu chuỗi) với nội dung là in ra dòng thông báo `Hello name!` khi hàm được gọi. 
	Ví dụ: khi gọi `hello('Python')` thì in ra là `Hello Python!`.
	
		+ Viết script `def-hello-2.py`
	
				# Ten file: def-hello-2.py
			 
				# Giai thich: 
			
				# Cu phap: Ham co 1 doi so la 'name' - kieu chuoi
			
				# Chuc nang: In ra thong bao 'Hello name!'
			
				def hello(name):
			
					print 'Hello ' + name + '!'
				
				# Chuong trinh chinh
			
				hello('Python')
				
				hello('Linux')
				
		+ Thực thi script `def-hello-2.py`:
		
				$ python def-hello-2.py
				
				Hello Python!
				
				Hello Linux!
				
* Hàm không có kết quả trả về:

	- Làm những hàm có hoặc không có đối số như cấu trúc của 2 cách xây dựng hàm như trên.
	
	- Những hàm không có kết quả trả về có đặc điểm là không được kết thúc bằng `return`.
	
* Hàm có có kết quả trả về:

	- Kết quả trả về ở đây: nghĩa là có thể sử dụng giá trị của hàm cho mục đích khác.
	
	- Những hàm kết thúc bằng `return` là những hàm có kết quả trả về.
	
	- Hàm có thể có hoặc không có đối số. Thông thường là hàm có đối số. Nhưng có khi hàm không cần đối số.
	
	- Cú pháp:
	
			def tenham(danhsachdoiso): 
				
				Khối lệnh thực hiện chức năng
				
				return danhsachketqua
				
		+ Danh sách đối số cách nhau bằng dấu phẩy ','.
		
		+ Danh sách kết quả trả về cách nhau bằng dấu phẩy ','.
				
	- Ví dụ: viết hàm `tong2so` (có 2 đối số là `a, b` - kiểu số) tính tổng của 2 số. 
	Ví dụ: khi gọi `tong = tong2so(1, 2)` thì `tong` sẽ có giá trị là `3`.
	
		+ Viết script `def-tong2so.py`
		
				# Ten file: def-tong2so.py
			 
				# Giai thich: 
			
				# Cu phap: Ham co 2 doi so la a, b - kieu so
			
				# Chuc nang: Tinh tong cua 2 so
			
				def tong2so(a, b):
			
					s = a + b
					
					return s
					
				# Chuong trinh chinh
			
				tong = tong2so(1, 2)
				
				print tong
				
		+ Thực thi script `def-tong2so.py`:
		
				$ python def-tong2so.py
				
				3
