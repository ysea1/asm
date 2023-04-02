import pandas as pd
import numpy as np
import re



def task_1():
	'''
	Task 1:
	1.1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)
	1.2. Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.
	1.3. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ
	'''
	
	filename = input('Enter a filename: ')

	try:
		with open(filename, "r") as file:
			print('Mở file thành công')
			return file
	except FileNotFoundError:
		print("Xin lỗi, tôi không thể tìm thấy file {0}".format(filename))
	except PermissionError:
		print("Bạn không có quyền truy cập file này")
	except Exception as e:
		print("Có lỗi không xác định xảy ra: {0}".format(e))
	#else:
	#	return content
		
	return None
		
# end def task_1()




def task_2(file):
	'''
		Trả về tổng số dòng được lưu trữ trong file
		Báo cáo tổng số dòng dữ liệu không hợp lệ trong file
			Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
			N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.
		Báo lỗi dòng dữ liệu không hợp lệ
	'''
	
	line_count = count_line_file(file)
	print('Total valid lines of data: {0}'.format(line_count))
	
	

# end def task_2()


def count_line_file(file):
	'''
		Trả về tổng số dòng của file
	'''
	
	line_count = 0
	
	if file is None :
		return 0
		
	for line in file:
		if line.strip():
			line_count += 1

	return line_count
# end def count_line_file(file):

def count_invalid_data(file):
	'''
		Trả về tổng số dòng không hợp lệ của file
	'''
	
	# line_invalid_count : Tổng số dòng không hợp lệ
	line_invalid_count = 0
	
	# is_set_invalid : Biến mục đích dùng xác định khi lệnh kiểm tra 1 đã xác định dòng không hợp lệ, thì ở lệnh kiểm tra 2 không tăng thêm giá trị tổng số dòng không hợp lệ nữa
	is_set_invalid = False
	
	if file is None :
		return 0
		
	# Đọc dữ liệu từng dòng trong file
	# Kiểm tra điều kiện hợp lệ :
	#	Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
	#	N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.
	for line in file:
		if line.strip():
			items = line.split(',')
			if len(items) <> 26 :
				print('Invalid line of data: does not contain exactly 26 values: {0}'.format(line))
				if not is_set_invalid :
					line_invalid_count += 1
					is_set_invalid = True
			
			pattern = 'N[0-9]{8,8}'
			if not re.match(pattern, items[0]):
				print('Invalid line of data: N# is invalid : {0}'.format(items[0]))
				if not is_set_invalid :
					line_invalid_count += 1
					is_set_invalid = True
					
	
	return line_invalid_count
		
# end def count_invalid_data(file)
	


def task_3():
	
# end def task_3()