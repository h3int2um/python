# Các toán tử logic và các biểu thức logic trong Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 09 tháng 09 năm 2016

## Ứng dụng của biểu thức Logic

Các biểu thức logic có ứng dụng quan trọng trong cấu trúc lệnh điều khiển: `if` và `while`.

## Kết quả của biểu thức logic

* Biểu thức logic chỉ nhận 1 trong 2 giá trị sau: `1` hoặc `0` hay `True` hoặc `False`.

* Trong chương trình có thể so sánh các biểu thức logic với các giá trị trên. 

* Lưu ý: Cần viết đúng `True` hoặc `False` trong khi viết chương trình, không phải là `true` hoặc `false`.

## Các toán tử logic thường sử dụng

* Gồm các toán tử logic thường dùng sau: `>, < , ==, >=, <=, !=` (dùng để so sánh), `|, &` và `and, or, not` 
(dùng để kết hợp các biểu thức logic).

* Toán tử `>`: so sánh lớn hơn. Ví dụ:

		>>> 1 > 0
		
		True
		
		>>> 1 > 2
		
		False

* Toán tử `<`: so sánh bé hơn. Ví dụ:

		>>> 1 < 2
		
		True
		
		>>> 1 < 0
		
		False

* Toán tử `==`: so sánh bằng. Ví dụ:

		>>> 2 == 2
		
		True
		
		>>> 2 == 3
		
		False

* Toán tử `>=`: so sánh lớn hơn hoặc bằng. Ví dụ:

		>>> 2 >= 1
		
		True
		
		>>> 2 >= 2
		
		True
		
		>>> 2 >= 3
		
		False

* Toán tử `<=`: so sánh nhỏ hoặc bằng. Ví dụ:

		>>> 2 <= 3
		
		True
		
		>>> 2 <= 2
		
		True
		
		>>> 2 <= 1
		
		False
		

* Toán tử `!=`: so sánh khác. Ví dụ:

		>>> 2 != 3
		
		True
		
		>>> 2 != 2
		
		False

* Sử dụng thêm cặp ngoặc `()` để kết hợp nhiều biểu thức logic với nhau, làm rõ các so sánh tránh nhầm lẫn cho người 
viết và đọc kiểm chương trình.

* Toán tử `&` hoặc `and`: Kết hợp nhiều biểu thức logic lại với nhau.
	
	- Chỉ đúng khi tất cả các biểu thức logic ở 2 bên toán tử `&` hoặc `and` đều đúng. 
	
	- Sai khi chỉ cần 1 biểu thức logic sai.
	
	- Ví dụ:

			>>> (2 > 1) & (2 < 3)				# Cả 2 biểu thức đều đúng
		
			True
	
			>>> (4 > 5) & (2 > 3)				# Chỉ có 1 biểu thức đúng
		
			False
		
			>>> (5 > 3) & (6 > 5) & (7 > 6)		# Cả 3 biểu thức đều đúng
		
			True
		
			>>> (5 > 3) & (6 > 5) & (2 > 6)		# Có 1 biểu thức sai
		
			False

* Toán tử `|` hoặc `or`: Kết hợp nhiều biểu thức logic lại với nhau.

	- Chỉ sai khi tất cả các biểu thức đều sai.
	
	- Đúng khi có một biểu thức logic ở 2 bên toán tử `|` hoặc `or` là đúng.
	
	- Ví dụ:
	
			>>> (2 > 1) | (3 > 1)		# Cả 2 biểu thức đều đúng
			
			True
			
			>>> (2 > 3) | (3 < 5)		# Có 1 biểu thức đúng
			
			True
			
			>>> (1 < 0) | ( 2 > 3)		# Cả 2 biểu thức đều sai
			
			False
			
* Toán tử `not`: phủ định giá trị của một biểu thức logic.

	- Chỉ đúng khi biểu thức logic sai.
	
	- Chi sai khi biểu thức logic đúng.
	
	- Ví dụ:
	
			>>> not (2 > 3)
			
			True
			
			>>> not ( 2 < 3)
			
			False
			
* Với các chương trình phức tạp, các biểu thức logic được lồng ghép vào nhau để có biểu thức logic 
phù hợp với mục tiêu. Ví dụ:

		>>> ( (2 > 3) or ((4 > 1) and (5 <= 10)) and (1 > 0) )
		
		True
