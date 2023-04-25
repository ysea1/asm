import pandas as pd
import numpy as np
import re
import os
import io

data_content_report = '' # Biến lưu nội dung hiển thị trên file báo cáo
filename = '' # Biến lưu tên file
file_out_put = '' # Biến lưu tên file hiển thị kết quả

def task_1():
	'''
	Task 1:
	1.1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)
	1.2. Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.
	1.3. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ
	'''
	
	global data_content_report
	global filename
	
	# Nếu len(data_content_report) > 0 có nghĩa trước đó đã có giá trị => bổ sung thêm dòng restart
	if len(data_content_report) > 0:
		data_content_report = ''
		data_content_report = '\n\n>>> ================================ RESTART ================================\n>>>\n'
	
	filename = input('Enter a filename or exit: ')
	
	# Nếu người dùng nhập exit thì thoát khỏi ứng dụng
	if filename.lower() == 'exit':
		return 'exit'
		
	current_dir = os.path.dirname(os.path.abspath(__file__))	
	filepath = format('{0}\{1}.txt'.format(current_dir, filename))
	#print(filepath)

	data_content_report = data_content_report + 'Enter a class to grade: {0}\n'.format(filename)
	try:
		with open(filepath, "r") as file:
			#print('Successfully opened {0}'.format(filename))
			data_content_report = data_content_report + 'Successfully opened {0}\n'.format(filename)			
			data_content_report = data_content_report + get_content_to_pandas(file)
	except FileNotFoundError:
		#print("File cannot be found. {0}".format(filename))
		data_content_report = data_content_report + 'File cannot be found. {0}\n'.format(filename)
	except PermissionError:
		#print("File don't have permission")
		data_content_report = data_content_report + "File don't have permission\n"
	except Exception as e:
		#print("It has error: {0}".format(e))
		data_content_report = data_content_report + "It has error: {0}\n".format(e)
	else:
		file.close()
		#return 'continue'
		
	print(data_content_report)
					
# end def task_1()

def  get_content_to_pandas(file):
	'''
		Đọc từng dong trong file
		Xác định các dòng không hợp lệ
		Đối với các dòng dữ liệu hợp lệ đưa vào pandas để thực hiện thống kê:
			- Số lượng học sinh đạt điểm cao
			- Điểm cao nhất
			- Điểm thấp nhất
			- Điểm trung bình
			- Miền giá trị của điểm
			- Câu hỏi mà thí sinh bỏ qua nhiều nhất, số lượng, tỷ lệ
			- Câu hỏi mà thí sinh trả lời sai nhiều nhất, số lượng, tỷ lệ
		- Ghi ra file thống kê tổng quát
		- Ghi ra file điểm của từng thí sinh của từng lớp
		
	'''
	#global file_out_put
	global filename
	data_content_report = ''
	
	line_count = 0 # Biến lưu tổng số dòng trong file
	line_invalid_count = 0 # Biến lưu tổng số dòng không hợp lệ trong file
	
	data_content_invalid = '' # Biến lưu nội dung của các dòng không hợp lệ
	
	answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
	list_answer_key = answer_key.split(',')
	data_student_score = ''
			
	try:
		for line in file:
			if line.strip():			
				
				#print('line count : {0}'.format(line_count))
				
				# Nếu dòng đang xét có lỗi thì tính số lượng dòng lỗi
				# Nếu dòng không lỗi thì tính điểm
				is_invalid, content_invalid = is_invalid_data(line)
				
				#print('is_invalid : {0} - conten invalid : {1}'.format(is_invalid, content_invalid))
				
				if is_invalid:
					line_invalid_count += 1
					data_content_invalid = data_content_invalid + content_invalid
				else:
					line_count += 1
					str_answer = line.strip()	
													
					str_answer = str_answer.replace(',,',',0,')
					str_answer = str_answer.replace(',,',',0,')
					
					# Nếu câu trả lời cuối cùng không có đáp án thì thay bằng giá trị 0
					if str_answer[len(str_answer)-1] == ',' :
						str_answer += '0'
						
					# Tính điểm từng thí sinh
					str_answer, score = task_3(str_answer, list_answer_key)
					
					# Thêm tổng điểm vào cột cuối cùng
					str_answer += '{0}\n'.format(score)
					
					# Nối danh sách bài thi và điểm thí sinh để đưa vào pandas
					data_student_score += str_answer
					#print('data_student_score : \n', data_student_score)
														
		# end for line in file:	
		
		#Tạm thời replace hết 
		
		# Đọc vào pandas
		df = pd.read_csv(io.StringIO(data_student_score), header=None, names=['ID', 'A1', 'A2','A3','A4','A5', 'A6', 'A7','A8','A9','A10', 'A11', 'A12','A13','A14','A15','A16', 'A17','A18','A19','A20', 'A21', 'A22','A23','A24','A25','SCORE'])				
		
		# Biến df_count chỉ lấy ra các cột trả lời của học sinh để xác định câu bị bỏ qua/trả lời sai nhiều nhất
		df_count = df[['A1', 'A2','A3','A4','A5', 'A6', 'A7','A8','A9','A10', 'A11', 'A12','A13','A14','A15','A16', 'A17','A18','A19','A20', 'A21', 'A22','A23','A24','A25']]
		
		df_score = df[['ID','SCORE']]
		#print('df_count:\n', df_count)
		#df = pd.read_csv(pd.compat.StringIO(data_student_score), header=None, names=['ID', 'A1', 'A2','A3','A4','A5', 'A6', 'A7','A8','A9','A10', 'A11', 'A12','A13','A14','A15','A16', 'A17','A18','A19','A20', 'A21', 'A22','A23','A24','A25','SCORE'])
																						
	
		data_content_report = data_content_report + '\n\n**** ANALYZING ****\n\n'
		#print('\n**** ANALYZING ****\n')	
		if line_invalid_count == 0:
			#print('No errors found!')
			data_content_report = data_content_report + 'No errors found!\n'				
		
		#print('\n**** REPORT ****\n')
		data_content_report = data_content_report + data_content_invalid
		
		data_content_report = data_content_report + '\n\n**** REPORT ****\n\n'
		
		#line_count = count_line_file(file)
		#print('Total valid lines of data: {0}'.format(line_count))
		#print('Total invalid lines of data: {0}'.format(line_invalid_count))
		data_content_report = data_content_report + 'Total valid lines of data: {0}\n'.format(line_count)
		data_content_report = data_content_report + 'Total invalid lines of data: {0}\n'.format(line_invalid_count)
		
		data_content_report = data_content_report + 'Total students of high scores: {0}\n'.format(df['SCORE'][df['SCORE'] >= 80].count())
		data_content_report = data_content_report + 'Mean (average) score: {0}\n'.format(round(df['SCORE'].mean(),2))
		data_content_report = data_content_report + 'Highest score: {0}\n'.format(df['SCORE'].max())
		data_content_report = data_content_report + 'Lowest  score: {0}\n'.format(df['SCORE'].min())
		data_content_report = data_content_report + 'Range  score: {0}\n'.format(df['SCORE'].max() - df['SCORE'].min())
		data_content_report = data_content_report + 'Median  score: {0}\n'.format(round(df['SCORE'].median(),2))
				
				
		# Câu hỏi không có câu trả lời (giá trị 0)
		search_value_skip = 0 # giá trị cần tìm
		
		# Lấy tổng số các câu hỏi không có câu trả lời
		counts_skip = (df_count == search_value_skip).sum() # List các cột và số lượng giá trị == search_value		
		#print('counts_skip : ', counts_skip)
				
		# Step 3: Lấy cột có số lần xuất hiện nhiều nhất
		top_cols_skip = counts_skip.nlargest(1).index.tolist()
		#print('top_cols_skip : ', top_cols_skip)
		#print('counts_skip[top_cols_skip[-1]] : ',counts_skip[top_cols_skip[-1]])	
		
		# Step 4: Duyệt từng cột, lấy tất cả các cột mà có số lần xuất hiện bằng top_cols_skip
		data_question_skip = ''
		rate_question_skip = round((counts_skip[top_cols_skip[-1]])/line_count,2)	
		for col in df_count.columns:
			#if (col not in top_cols_skip) and (counts[col] == counts_skip[top_cols_skip[-1]]):
			if (counts_skip[col] == counts_skip[top_cols_skip[-1]]):
				if search_value_skip in df_count[col].tolist():
					#print('col : {0}'.format(col))
					data_question_skip += '{0} - {1} - {2}, '.format(col, counts_skip[top_cols_skip[-1]], rate_question_skip)				
		
		data_content_report = data_content_report + 'Question that most people skip: {0}\n'.format(data_question_skip)
		
		
		# Lấy câu hỏi mà nhiều học sinh trả lời sai nhất
		search_value_incorrect = -1
		counts_incorrect = (df_count == search_value_incorrect).sum() # List các cột và số lượng giá trị == search_value		
		#print('counts_incorrect : ', counts_incorrect)
		
		top_cols_incorrect = counts_incorrect.nlargest(1).index.tolist()
		#print('top_cols_incorrect : ', top_cols_incorrect)
		
		#print('top_conls_incorrect : {0} - counts_incorrect[top_cols_incorrect[-1]] : {1}'.format(top_cols_incorrect, counts_incorrect[top_cols_incorrect[-1]]))
		data_question_incorrect = ''
		rate_question_incorrect = round((counts_incorrect[top_cols_incorrect[-1]])/line_count,2)	
		for col in df_count.columns:
			#if (col not in top_cols) and (counts[col] == counts[top_cols[-1]]):
			if (counts_incorrect[col] == counts_incorrect[top_cols_incorrect[-1]]):
				if search_value_incorrect in df_count[col].tolist():
					#print('col : {0}'.format(col))
					data_question_incorrect += '{0} - {1} - {2}, '.format(col, counts_incorrect[top_cols_incorrect[-1]], rate_question_skip)	
					
		data_content_report = data_content_report + 'Question that most people answer incorrectly: {0}\n'.format(data_question_incorrect)
		
	except Exception as e:
		print("pd.read_csv has error: {0}".format(e))		
	
	
	#print('Finish : {0}'.format(data_content_report))
	#write_file(data_content_report, file_out_put, 'a+')
	
	current_dir = os.path.dirname(os.path.abspath(__file__))	
	file = '{0}\haiph_output\{1}_grades.txt'.format(current_dir, filename)
	df_score.to_csv(file, sep=',', index=False)
	
	return data_content_report
# end def  get_content_to_pandas(file)


def is_invalid_data(line):
	'''
		Trả về True : dòng bị lỗi và nội dung lỗi
				False : dòng không lỗi, nội dung lỗi trắng
	'''	
	
	# is_set_invalid : Biến mục đích dùng xác định khi lệnh kiểm tra 1 đã xác định dòng không hợp lệ, thì ở lệnh kiểm tra 2 không tăng thêm giá trị tổng số dòng không hợp lệ nữa
	is_invalid = False
	content_invalid = ''
	
	if line is None :
		return is_invalid, content_invalid
		
	# Đọc dữ liệu từng dòng trong file
	# Kiểm tra điều kiện hợp lệ :
	#	Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy
	#	N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số.	
	items = line.split(',')
	if len(items) != 26 :
		#print('Invalid line of data: does not contain exactly 26 values: {0}'.format(line.strip()))
		content_invalid = 'Invalid line of data: does not contain exactly 26 values: {0}\n'.format(line.strip())
		if not is_invalid :			
			is_invalid = True
	
	pattern = 'N[0-9]{8,8}'
	if not re.match(pattern, items[0]):
		#print('Invalid line of data: N# is invalid : {0}'.format(items[0]))
		content_invalid = content_invalid +  'Invalid line of data: N# is invalid : {0}\n'.format(items[0])
		if not is_invalid :			
			is_invalid = True
							
	return is_invalid, content_invalid
		
# end def count_invalid_data(file)

def task_3(line, list_answer_key):
	'''
		Chấm điểm bài thi
		Chuyển từ câu trả lời của thí sinh sang kết quả : -1 - trả lời sai, 0 - bỏ qua, 4 - trả lời đúng để đưa vào pandas thuận tiện cho việc thống kê
		Trả về chuỗi kết quả trả lời của thí sinh và tổng điểm của thí sinh đó
		
		
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
	str_answer_student = ''
	str_answer_student += '{0},'.format(list_answer_student[0])
	for i in range(0, 25):
		if len(list_answer_student[i+1]) > 0 :
			if list_answer_student[i+1] != '0' : 
				if list_answer_student[i+1] == list_answer_key[i] :
					str_answer_student += '4,'
					score += 4
				else:
					str_answer_student += '-1,'
					score -= 1
			else:
				str_answer_student += '0,'
	
	#end for i in range(0, 26)	
		
	return str_answer_student, score
	
# end def task_3()

def write_file(str_content, filename, mode):
	'''
		str_content : Nội dung ghi ra file
		filename : tên file
		mode : Chế độ ghi
			'w' : ghi file mới
			'a+' : 
		
	'''
	
	#global file_out_put
	current_dir = os.path.dirname(os.path.abspath(__file__))	
	file = '{0}\haiph_output\{1}_grades.txt'.format(current_dir, filename)
		
	try:		
		with open(file, 'a+') as writefile:
			writefile.write(str_content)
	except FileNotFoundError:
		print("File cannot be found. {0}".format(file_out_put))
	except PermissionError:
		print("File don't have permission")
	except Exception as e:
		print("It has error: {0}".format(e))
	else:
		writefile.close()		
	
#end def write_file(str_content)


	
#file_out_put = input('Enter a filename : ')
	
while True :
	action = task_1()
	
	if action == 'exit':
		break