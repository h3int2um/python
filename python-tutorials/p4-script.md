# Viết các script .py trong Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 08 tháng 09 năm 2016

## Tạo các file .py

* Các script được viết bằng Python có phần mở rộng là `.py`.

* Khi làm việc với các chương trình dài và phức tạp, việc nhập vào từng lệnh không đem lại hiệu quả, tốn nhiều thời gian. 
Nên cần tạo các file script `.py` gồm nhiều lệnh trong đó, dễ dàng quản lý và thay đổi nội dung chương trình.

* Với các script `.py` thao tác chủ yếu trên các biến. Khi cần kiểm tra giá trị của biến dùng lệnh `print` để in ra thông tin của biến.

## Khối lệnh trong Python

* Các lệnh nằm chung trong một khối lệnh: có khoảng cách `indent` như nhau. Nếu vi phạm quy tắc này thì chương trình báo lỗi.

* Với Python, khoảng cách `indent` quan trọng khi viết các file `.py`, các lệnh trong một khối lệnh thì có cùng khoảng cách `indent`.

* Nếu trong file `.py` có lỗi về khoảng cách `indent` thì khi thực thi sẽ thông báo lỗi:

		IndentationError: unexpected indent
	
* Sau dấu `:` kết thúc trong một số cấu trúc, sẽ là một khối lệnh sau nó. Ví dụ:

		for i in range(10):		# Bắt đầu một khối lệnh
		
			i = i + 1
				
			print i
			
		
		i = 0
		
		while i < 10:
			
			i = i + 1
			
			print i
			
* Ví dụ về viết đúng khối lệnh trong Python

		# Mô tả khối lệnh trong Python với cùng khoảng cách indent
		
		# Tên file khoilenh.py
		
		a = 2
		
		b = 3 
		
		c = a + b
		
		if c % 2 == 0:
		
			print 'True'
			
			print 'c la so chan'
			
			for i in range(10):
			
				print i
				
			for j in range(0,5):
			
				print j
			
		else:
			
			print 'False
			
			print 'c la so le'
			
		print 'Ket thuc chuong trinh'

	Các lệnh cùng một khoảng cách `indent` được xem là khối lệnh và cú pháp hợp lệ, ví dụ: 2 lệnh `print` dưới `if` hoặc `else`.
	
* Ví dụ về viết sai khối lệnh trong Python

		# Mô tả khối lệnh trong Python sai cú pháp về indent
		
		# Tên file khoilenh-sai.py
		
		a = 2
		
		b = 3
		
			c = a + b
		
		print c
		
		for i in range(10):
		
			i = i + 1
			
				print i				
			
	Dòng `c = a + b` được `indent` vào không thuộc khối lệnh nào nên sai cú pháp. Dòng `print i` không thuộc khối lệnh trong 
	cấu trúc `for`.
	
## Giao tiếp giữ người dùng và script.py

* Lệnh `print`: Hiển thị giá trị của biến lên màn hình.

* Lệnh `raw_input`: Người dùng nhập giá trị từ bàn phím. Kết quả nhận được là kiểu chuỗi.

* Ví dụ: 

	+ Tạo một script `.py`: thực hiện cộng 2 số
	
			# Ten script phepcong1.py
	
			a = 2
	
			b = 3
	
			c = a + b
	
			print c
			
	+ Thực thi script `.py`: Chuyển đến thư mục chứa file `phepcong1.py` vừa tạo.
	
			$ python phepcong1.py 
			
			5
			
	+ Tạo một script `.py`: thực hiện cộng 2 chuỗi nhập từ bàn phím
	
			# Ten script phepcong2.py
	
			str1 = raw_input('Chuoi thu nhat: ')	# Nhan mot chuoi nhap tu ban phim va gan vao bien str1
			
			str2 = raw_input('Chuoi thu hai: ')		# Nhan mot chuoi nhap tu ban phim va gan vao bien str2
			
			s = str1 + str2							# Cong 2 chuoi vua nhap
			
			print s									# Hien thi len man hinh
			
	+ Thực thi script `.py`: Chuyển đến thư mục chứa file `phepcong2.py` vừa tạo.
	
			$ python phepcong2.py 
			
			Chuoi thu nhat: Hello		# Nhap vao chu Hello
			
			Chuoi thu hai: Python		# Nhap vao chu Python
			
			HelloPython					# Ket qua nhan duoc
			
* Chú thích trong Python

	+ Dùng dấu `#`: Nội dung sau dấu `#` được xem là phần chú thích
	
			# Đây là nội dung được chú thích
	
	+ Dùng  `''' ... '''`:
	
			'''
				Nội dụng bên trong cặp dấu ''' và ''' được xem là phần chú thích
			'''
