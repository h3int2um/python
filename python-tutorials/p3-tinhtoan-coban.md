# Thực hiện các phép tính cơ bản bằng Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 08 tháng 09 năm 2016

## Biến và lệnh gán

* Tên biến:

	+ Với ngôn ngữ Python, không cần khai báo kiểu dữ liệu cho biến.

	+ Tên biến tuân theo quy tắc:

		- Tên biến phân biệt chữ hoa và chữ thường.
	
		- Bắt đầu bằng chữ cái `A...Z` hoặc `a...z` hoặc `_`.
	
		- Tiếp theo là: chữ cái hoặc số hoặc `_`.
	
		- Hạn chế kết thúc tên biến bằng `_`. Không sử dụng dấu cách `space`, các ký tự đặt biệt trong tên biến.

		- Tên biến không được trùng với tên của từ khóa.
	
		- Ví dụ các tên biến hợp lệ: `abc`, `AbC', `a1b`, `a_1b`, `_ab`,...

		- Ví dụ các tên biến không hợp lệ: `1bc`, `1b c`, `1-bc`, `1@bc`, `for`, `if`,...
		
* Lệnh gán: sử dụng `=` để gán giá trị cho biến, giá trị có thể là số, biểu thức, hoặc giá trị của các biến trước đó. Ví dụ:

		>>> a = 1
		
		>>> b = 2
		
		>>> c = a + b
		
		>>> c

		3
		
* Chú thích trong Python: 

	+ Các ký tự sau dấu `#` được hiểu là phần chú thích, không ảnh hưởng đến chương trình.

			>>> a = 3 # Đây là phần chú thích
		
	+ Hoặc sử dụng `''' ... '''` để chú thích nhiều dòng khi viết `script`. Cách viết `script` sẽ được trình bày riêng ở phần sau, 
	các chương trình viết bằng `Python` được lưu ở dạng `script.py`.			
			
## Kiểu dữ liệu số

* Gồm các phép toán cơ bản `+,-,*,/,%,**`, sử dụng cặp `()` để kết hợp các phép toán phép toán với nhau.

	+ `+`: Phép cộng.
	
	+ `-`: Phép trừ.
	
	+ `*`: Phép nhân.
	
	+ `/`: Phép chia, phép chia lấy phần nguyên.
	
	+ `%`: Phép chia lấy phần dư.
	
	+ `**`: Lấy lũy thừa.
	
	+ `abs`: Lấy giá trị tuyệt đối của một số.
	
	+ `round(n,digit)`: Làm tròn số `n` với `digit` chữ số.
	
	
* Ví dụ: 
		
		>>> 2 + 3 		# Phép cộng 2 số: áp dụng được cho kiểu số nguyên, số thực
		
		5
		
		>>> 9 - 4		# Phép trừ 2 số: áp dụng được cho kiểu số nguyên, số thực
		
		5
		
		>>> 2*3			# Phép nhân 2 số: áp dụng được cho kiểu số nguyên, số thực
		
		6
		
		>>> 5/2			# Phép chia lấy phần nguyên: áp dụng được cho kiểu số nguyên
		
		2
		
		>>> 5/2.0		# Phép chia 2 số: áp dụng được cho kiểu số thực
					
		2.5				# Kết quả tương tự cho 5.0/2
		
		>>> 5 % 2 		# Phép chia lấy phần dư: áp dụng được cho kiểu số nguyên, số thực
		
		1
		
		>>> 5**5		# Lấy lũy thừa a**b = a^b: áp dụng được cho kiểu số nguyên, số thực
		
		25
		
		>>> asb(-3)		# Lấy giá trị tuyệt đối
		
		3
		
		>>> round(1.234567,3)		# Làm tròn 3 số
		
		1.234
		
		
## Kiểu số phức

* Khai báo số phức: Thêm `j` hoặc `J` vào sau phần ảo:

* Các hàm thực hiện trên số phức:

		+ `real`: Lấy phần thực.
		
		+ `imag`: Lấy phần ảo.
		
		+ `abs`:  Lấy module của số phức.

			>>> x = -1 + 1j		# Số phức x = 1 + i
			
			>>> x.real			# Lấy phần thực
			
			-1.0
			
			>>> x.image			# Lấy phần ảo
			
			1.0
			
			>>> abs(x)			# Lấy module số phức
			
			1.4142135623730951
			
## Kiểu dữ liệu chuỗi

* Chuỗi được đặt trong cặp `'...'`  hoặc '"..."`. Để thể hiện các ký tự đặt biệt `'`, `\`: thêm `\` vào trước ký tự.
		
		>>> 'Isn\'s, she said'			# Có chứa ký tự đặt biệt
		
		"Isn's, she said"

* Phép toán trên chuỗi:
	
	+ `+`: Ghép nối tiếp các chuỗi với nhau.
	
			>>> str1 = 'Hello'
		
			>>> str2 = 'Python!'
		
			>>> str1 + str2 			# Nối 2 chuỗi lại với nhau.
		
			'HelloPython!'
	
	+ `*`: Ghép nối tiếp một chuỗi lên bội lần.
	
			>>> st = 'Python!'
	
			>>> st*2					# Ghép nối tiếp chuỗi st lên 2 lần
		
			'Python!Python!'
	
* Một số hàm trên chuỗi:

	+ Xác định độ dài của chuỗi: `len(chuoi)`.
	
			>>> chuoi = 'Python'
			
			>>> len(chuoi)				# Tính độ dài của một chuỗi
			
			6
	
	+ In hoa tất cả các phần tử trong chuỗi: `chuoi.upper()`
	
	+ In thường tất cả các phần tử trong chuối: `chuoi.lower()`
			
			>>> chuoia = 'python'
			
			>>> chuoia.upper()
			
			'PYTHON'
			
			>>> chuoib = 'LEARN'
			
			>>> chuoib.lower()
			
			'learn'
			
* Thao tác trên chuỗi:

	+ Vị trí các phần tử trên chuỗi bắt đầu từ:
	
		- `index = 0`: đọc chuỗi theo chiều thuận.
		
		- `index = -1`: đọc chuỗi theo chiều ngược lại.
		
				>>> chuoi = 'Python'
				
				>>> chuoi[0]
				
				'P'
				
				>>> chuoi[-1]
				
				'n'
				
				>>> chuoi[-2]
				
				'o'
				
		- `index` truyền vào có thể là `số âm` hoặc `số dương` tùy theo giải thuật.
		
	+ Truy xuất phần tử của chuỗi: `chuoi[index]` hoặc `chuoi[:index]` hoặc `chuoi[index:]` hoặc `chuoi[index1: index2]`.
	
		- `chuoi[index]`: truy xuất 1 phần tử ở đúng vị trí `index` trong chuỗi.
		
				>>> chuoi = 'Python'
				
				>>> chuoi[1]
		
		- `chuoi[:index]`: truy xuất từ vị trí `index = 0` đến vị trí `index = index - 1` trong chuỗi.
		
				>>> chuoi = 'Python'
				
				>>> chuoi[:2]
				
				'Py'
				
		- `chuoi[index1: index2]`: truy xuất từ vị trí `index = index1` đến vị trí `index = index2 - 1`
		
				>>> chuoi = 'Python!'
				
				>>> chuoi[2:6]
				
				'thon'
				
		- `chuoi[index:]`: truy xuất phần tử từ vị trí `index` đến vị trí cuối cùng của một chuỗi.

* Một số ký tự điều khiển: dùng kết hợp với lệnh `print`.

	+ `\n`: xuống dòng mới.
	
	+ `\t`: tạo khoảng cách bằng phím `tab`.
			
			>>> print 'What your name?\nMy name is Anne.'	# Chứa ký tự điều khiển \n (new line)
		
			What your name?
		
			My name is Anne.
		
			>>> print 'My name is:\tAnne'
		
			My name is:	Anne								# Chứa ký tự điều khiển \t (tab)
		
## Kiểu list

* Về cơ bản, các thao tác trên kiểu `list` gần giống như kiểu `string`. Kiểu `list` có thể gồm các phần tử có kiểu dữ liệu 
giống nhau hoặc khác nhau. Thường là chứa các phần tử có kiểu dữ liệu giống nhau.

* Ví dụ: các thao tác truy xuất cơ bản trong `list`.
		
		>>> x = [1, 2, 3, 4]
		
		>>> len(x)			# Lấy độ dài của list
		
		4
		
		>>> x[0]			# Truy xuất phần tử ở vị trí index = 0
		
		1
		
		>>> x[1:3]			# Truy xuất phần tử ở vị trí index = 1 đến vị trí index = 3 - 1 = 2
		
		[2, 3]
		
		>>> x[1:]			# Truy xuất từ vị trí index = 1 đến cuối danh sách
		
		[2, 3, 4]
		
		>>> x[:2]			# Truy xuất từ vị trí index = 0 đến vị trí index = 3-1 = 2
		
		[1, 2]
		
		>>> x[:]			# Truy xuất toàn bộ danh sách
		
		[1, 2, 3, 4]
		
		>>> x				# Truy xuất toàn bộ danh sách
				
		[1, 2, 3, 4]
		
		
* Các phép toán trên `list`:

	- `[list1, list2,...,listn]`: Lồng ghép các list lại với nhau.
	
			>>> x1 = [1, 2]
			
			>>> x2 = [3, 4]
			
			>>> [x1, x2]		# Lồng các list với nhau
			
			[[1,2], [3,4]]
			
	- `=`: Gán lại các phần tử trong list. Số phần tử được gán lại phải bằng với số phần mới, có sự tương thích về kích thước.
	
			>>> x = [1, 2, 3, 4]
			
			>>> x[0] = 0			# Gán lại giá trị mới cho x[0], kết hợp với ':' để gán nhiều phần tử cùng một lúc
		
			>>> x
		
			[0, 2, 3, 4]
			
			>>> x[1:3] = [5,6]		# Tương thích kích thước của 2 list (kích thước là 2)
			
			>>> x
			
			[0, 5, 6, 4]
		
	- `*`: Ghép nối tiếp list lên bội lần.
	
			>>> x = [1, 2, 3, 4]
	
			>>> x*2					# Ghép nối tiếp list 2 lần
		
			[1, 2, 3, 4, 1, 2, 3, 4]
			
	- `+`: Mở rộng list.
	
			>>> [1, 2, 3] + [4, 5]
			
			[1, 2, 3, 4, 5]
			
	- `append(x)`: Thêm phần tử `x` vào cuối list.
	
			>>> x = [1, 2]
			
			>>> x.append(3)		# Thêm giá trị 3 vào cuối list
			
			>>> x
			
			[1, 2, 3]
			
	- `extend(list_new)`: Mở rộng list bằng cách thêm list mới  `lít_new` vào sau list hiện tại.
	
			>>> x = [1, 2, 3]
			
			>>> x2 = [4, 5, 6]
			
			>>> x.extend(x2)	# Thêm list x2 nối tiếp với list x
			
			>>> x
			
			[1, 2, 3, 4, 5, 6]
			
	- `insert(index, value)`: Chèn một phần tử vào vị trí bất kỳ trong list, chèn `value` vào vị trí `index` trong list.
	
			>>> x = [1, 2, 3]
			
			>>> x.insert(0,4)		# Chèn vào vị trí 0 giá trị 4
			
			>>> x
			
			[4, 1, 2, 3]
	
	- `remove(x)`: Tìm và xóa phần tử `x` đầu tiên theo chiều thuận trong list.
	
			>>> x = [1, 2, 3, 4, 3]
			
			>>> x.remove(3)		# Xóa phần tử có giá trị bằng 3 (đầu tiên) ra khỏi list
			
			>>> x
			
			[1, 2, 4, 3]
			
		Nếu phần tử xóa không có trong mảng, sử dụng lệnh `remove` sẽ báo lỗi.
		
	- `pop(index)`: Xóa phần tử ở vị trí `index` trong list và trả về chính nó.
	
			>>> x = [1, 2, 3, 5]
			
			>>> x.pop(3)				# Xóa phần tử x[3] khỏi list
			
			5
			
			>>> x
			
			[1, 2, 3]
			
		Nếu bỏ qua vị trí `index` trong hàm `pop` thì phần tử cuối cùng trong list bị xóa đi.
		
				>>> x = [1, 2, 3]
				
				>>> x.pop()			# Phần tử cuối cùng được xóa khi bỏ index trong hàm pop
				
				>>> x 
				
				[1, 2]
				
	- `index(x)`: Trả về vị trí của phần tử `x` có trong danh sách.
	
			>>> x = [1, 5, 3]
			
			>>> x.index(2)
			
			3
			
		Nếu không có phần tử `x` trong danh sách thì báo lỗi.
		
	- `count(x)`: Đếm số lần xuất hiện phần tử `x` trong list.
	
			>>> x = [2, 3, 2, 4, 2]
			
			>>> x.count(2)			# Đếm số lần phần tử có giá trị 2 xuất hiện trong list
			
			3
			
			>>> x.count(5)
			
			0
			
	- `sort()`: Sắp xếp các phần tử theo thứ tự tăng.
	
			>>> x = [5, 2, 4, -1, 6]
			
			>>> x.sort()
			
			>>> x
			
			[-1, 2, 4, 5, 6]
			
	- `reverse()`: Đảo ngược thứ tự các phần tử trong danh sách.
	
			>>> x = [1, 2, 3]
			
			>>> x.reverse()
			
			>>> x
			
			[3, 2, 1]
					
## Tài liệu tham khảo

[Using Python as a Calculator](https://docs.python.org/2/tutorial/introduction.html#using-python-as-a-calculator)
