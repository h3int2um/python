# Cài đặt Python

Thực hiện: Thi Minh Nhưt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 07 tháng 09 năm 2016

## Python trên Linux

Trên hệ điều hành `Linux`: Python được cài đặt sẵn khi cài đặt hệ điều hành. Phiên bản cài đặt có thể 
không phải là phiên bản mới nhất.

* Kiểm tra phiên bản của Python: 

		$ python -V
		
		Python 2.7.6

* Cài đặt phiên bản mới cho hệ điều hành `Linux`:

	- Bước 1: Cài đặt các gói lệnh yêu cầu.
	
			$ sudo apt-get install build-essential checkinstall
				
			$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
			
	- Bưới 2: Tải phiên bản mới nhất của Python: [Download Python](https://www.python.org/downloads/), 
	ví dụ: `Python-2.7.12.tar.xz`
		
	- Bước 3: Chuẩn bị để cài đặt, di chuyển đến thư mục chứa file `Python-2.7.12.tar.xz`, thực hiện các lệnh dưới.
		
			$ tar xf Python-2.7.12.tar.xz
			
			$ sudo mv Python-2.7.12 /usr/src
				
	- Bước 4: Cài đặt Python từ mã nguồn.
		
			$ cd /usr/src/Python-2.7.12
				
			$ sudo ./configure
				
			$ sudo make altinstall
		
	Lệnh `altinstall`: ngăn không thay thế python được cài đặt mặc định trong `/usr/bin/python`
				
	- Bước 5: Kiểm tra phiên bản của Python.
		
			$ python2.7 -V
				
			Python 2.7.12
				
* Làm việc với phiên bản mới của Python:

		$ python2.7

## Tài liệu tham khảo

[How to Install Python 2.7.12 on Ubuntu & LinuxMint](http://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/#)
