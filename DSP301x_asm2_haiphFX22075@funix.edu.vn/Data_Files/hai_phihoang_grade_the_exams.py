import pandas as pd
import numpy as np
import re
import os



def task_1():
	'''
	Task 1:
	1.1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)
	1.2. Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.
	1.3. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ
	'''
		
	filename = input('Enter a filename or exit: ')
	
	# Nếu người dùng nhập exit thì thoát khỏi ứng dụng
	if filename.lower() == 'exit':
		return 'exit'
		
	current_dir = os.path.dirname(os.path.abspath(__file__))	
	filepath = format('{0}\{1}.txt'.format(current_dir, filename))
	print(filepath)

	try:
		with open(filepath, "r") as file:
			print('Successfully opened {0}'.format(filename))
			task_2(file)
	except FileNotFoundError:
		print("File cannot be found. {0}".format(filename))
	except PermissionError:
		print("File don't have permission")
	except Exception as e:
		print("It has error: {0}".format(e))
	else:
		file.close()
		return 'continue'
					
# end def task_1()


def task_2(file):
	'''
		Trả về tổng số dòng được lưu trữ trong file
		Báo cáo tổng số dòng dữ liệu không hợp lệ trong file
			Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
			N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.
		Báo lỗi dòng dữ liệu không hợp lệ
	'''
	
	line_count = 0 # Biến lưu tổng số dòng trong file
	line_invalid_count = 0 # Biến lưu tổng số dòng không hợp lệ trong file
	
	answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
	list_answer_key = answer_key.split(',')
	
	dict_student_score = {}
	count_student_high_score = 0
	max_score = 0
	min_score = 0
	avg_score = 0
	range_score = 0
	
	for line in file:
		if line.strip():
			line_count += 1
			
			# Nếu dòng đang xét có lỗi thì tính số lượng dòng lỗi
			# Nếu dòng không lỗi thì tính điểm
			if is_invalid_data(line):
				line_invalid_count += 1
			else:
				dict_student_score.append(task_3(line, list_answer_key))
	# end for line in file:	
	
	min_score = min(dict_student_score.values())
	max_score = max(dict_student_score.values())
	avg_score = round(sum(dict_student_score.values())/len(dict_student_score),2)
	range_score = max_score - min_score
	
	for item in dict_student_score :
		if dict_student_score[item] >= 80:
			count_student_high_score += 1
	
	print('**** ANALYZING ****')	
	if line_invalid_count == 0:
		print('No errors found!')
	
	print('**** REPORT ****')
	
	#line_count = count_line_file(file)
	print('Total valid lines of data: {0}'.format(line_count))
	print('Total invalid lines of data: {0}'.format(line_invalid_count))
	
		

# end def task_2()

def is_invalid_data(line):
	'''
		Trả về True : dòng bị lỗi
				False : dòng không lỗi
	'''	
	
	# is_set_invalid : Biến mục đích dùng xác định khi lệnh kiểm tra 1 đã xác định dòng không hợp lệ, thì ở lệnh kiểm tra 2 không tăng thêm giá trị tổng số dòng không hợp lệ nữa
	is_invalid = False
	
	if line is None :
		return is_invalid
		
	# Đọc dữ liệu từng dòng trong file
	# Kiểm tra điều kiện hợp lệ :
	#	Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
	#	N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.	
	items = line.split(',')
	if len(items) != 26 :
		print('Invalid line of data: does not contain exactly 26 values: {0}'.format(line.strip()))
		if not is_invalid :			
			is_invalid = True
	
	pattern = 'N[0-9]{8,8}'
	if not re.match(pattern, items[0]):
		print('Invalid line of data: N# is invalid : {0}'.format(items[0]))
		if not is_invalid :			
			is_invalid = True
							
	return is_invalid
		
# end def count_invalid_data(file)

def task_3(line, list_answer_key):
	'''
		Chấm điểm bài thi
		Trả về mã thí sinh và điểm thi của thí sinh
		
		Giải thuật :
			Chuyển các câu trả lời sang dạng list
			Duyệt từng câu trả lời so với đáp án có chính xác không ?
				Đúng : +4 điểm
				Bỏ qua : 0 điểm
				Sai : -1 điểm
	'''
	
	#answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
	#list_answer_key = answer_key.split(',')
	
	score = 0
	list_answer_student = line.split(',')
	for i in range(0, 26):
		if len(list_answer_student[i+1]) > 0 :
			if list_answer_student[i+1] == list_answer_key[i] :
				score += 4
			else:
				score -= 1
	
	#end for i in range(0, 26)	
	
	return {list_answer_student[0], score}
	
# end def task_3()


while True :
	action = task_1()
	
	if action == 'exit':
		break