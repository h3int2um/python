# Xây dựng module trong Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 15 tháng 09 năm 2016

## Khái niệm về Module trong Python

* Module là một file gồm các lớp các hàm, các biến được định nghĩa sẵn.

* Sử dụng Module giúp chương trình dễ quản lý hơn, có thể sử dụng lại khi cần đến, giúp tiết kiệm thời gian.

* Module có thể do người dùng định nghĩa hoặc các module được Python xây dựng sẳn.

## Cách xây dựng một module

* Viết một script `.py` gồm các hàm hoặc các lớp trong đó và lưu với tên gợi nhớ chức năng.

* Lưu ý: không xây dựng module trùng tên với module được Python xây dựng sẳn.

* Script vừa tạo là một module.

* Ví dụ: Xây dựng một module có tên là `pheptinhcoban`: với 2 chức năng là cộng và trừ cho 2 số.

	- Viết một script `pheptinhcoban.py`

			# Module pheptinhcoban gom: phep cong (+) và phep tru (-) cho 2 so.
			
			# Ten file pheptinhcoban.py
			
			def phepcong(a, b):		# Phep cong 2 so
			
				return a + b
				
				
			def pheptru(a, b):		# Phep tru 2 so
			
				return a - b
				
	- Lưu lại với tên là `pheptinhcoban.py` trong thư mục cùng với chương trình chính.
	
## Thêm Module vào chương trình chính

* Sử dụng lệnh `import`:

	- Cú pháp `import module 1, module 2, ...` với `module 1, module 2, ...` là các module chúng ta tạo ra 
hoặc Python xây dụng sẳn.
	- Sử dụng chức năng trong Module: `tenmodule.chucnang`.

* Sử dụng lệnh `from`:

	- Cú pháp: `from module import *` sử dụng tất cả chức năng trong module
	
	- Cú pháp `from module import chucnang 1` chỉ sử dụng được `chucnang 1` trong module.
	
	- Sử dụng chức năng trong Module: `chucnang`.	

* Ví dụ: thêm module `pheptinhcoban` vừa tạo ở phần trên vào chương trình chính. Module `pheptinhcoban` 
với 2 chức năng là `phepcong(a, b)` và `pheptru(a, b)`.
	
	- Tạo script `moduletrongpython-1.py`
	
			# Them module tu xay dung (hoac co san) vao chuong trinh chinh trong Python
			
			# Ten file moduletrongpython-1.py
			
			import pheptinhcoban		# Module tu xay dung
			
			import time					# Module duoc Python xay dung san
			
			
			a = 1
			
			b = 2
			
			print pheptinhcoban.phepcong(a, b)		# Thuc hien phep cong 2 so a, b
			
			time.sleep(1)							
			
			print pheptinhcoban.pheptru(a, b)		# Thuc hien phep tru 2 so a, b
			
	- Thực thi script `moduletrongpython-1.py`:
	
			$ python moduletrongpython-1.py
			
			3
			
			-1
			
	- Cách khác tạo script `moduletrongpython-2.py`
	
			# Them module tu xay dung (hoac co san) vao chuong trinh chinh trong Python
			
			# Ten file moduletrongpython-2.py
			
			from pheptinhcoban import *		# Them tat cac chuc nang trong module pheptinhcoban
			
			import time						# Module duoc Python xay dung san
			
			
			a = 1
			
			b = 2
			
			print phepcong(a, b)		# Thuc hien phep cong 2 so a, b
			
			time.sleep(1)
			
			print pheptru(a, b)			# Thuc hien phep tru 2 so a, b
			
	- Thực thi script `moduletrongpython-2.py`:
	
			$ python moduletrongpython-2.py
			
			3
			
			-1
			
## Nhận xét

* Với cú pháp `import` tuy sử dụng lại với tên dài do phải khai báo là `tenmodule.chucnang`. 
Ưu điểm là dễ quản lý module hơn, tránh các sai sót nhầm lẫn chức năng giữa các module.

* Với cú pháp `from` tuy sử dụng lại với tên ngắn với khai báo là `chucnang`. 
Nhược điểm là khó quản lý module hơn, dễ bị các sai sót nhầm lẫn chức năng giũa các module.
