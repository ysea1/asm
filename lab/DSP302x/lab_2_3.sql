# Truy vấn A1: Nhập một truy vấn không thành công (khi đó bạn sẽ nhận được một lỗi) để truy xuất tất cả 
# nhân viên có mức lương nhiều hơn mức lương trung bình:
select * from `hr`.`employees` where salary > (select AVG(salary) from `hr`.`employees`);

# Truy vấn A4: Nhập Biểu thức Column (Cột) để truy xuất tất cả bản ghi nhân viên và mức lương trung bình ở mọi hàng 
select *, (select AVG(salary) from `hr`.`employees`) from `hr`.`employees`;

# Truy vấn A5: Nhập Biểu thức Table, biểu thức sẽ chỉ truy xuất các cột có dữ liệu nhân viên không nhạy cảm 



# Truy vấn B1: Chỉ lấy các bản ghi EMPLOYEES tương ứng với các phòng ban trong bảng DEPARTMENTS 
select * from `hr`.`employees` where dep_id in (select dep_id from `hr`.`departments`);

# Truy vấn B2: Chỉ lấy danh sách nhân viên từ vị trí L0002
select * from `hr`.`employees` where dep_id in (select dep_id from `hr`.`departments` where loc_id = 'L0002');


# Truy vấn B3: Truy xuất ID và tên phòng ban cho những nhân viên kiếm được hơn 70.000 đô la
select * from `hr`.`departments` where dept_id_dep in (select dep_id from `hr`.`employees` where salary >= 70000);

#Truy vấn B4: Chỉ định 2 bảng trong mệnh đề FROM 
select * from `hr`.`employees`, `hr`.`departments`;

# Truy vấn B5: Chỉ truy xuất các bản ghi EMPLOYEES tương ứng với các phòng ban trong bảng DEPARTMENTS:
select * from `hr`.`employees`
inner join `hr`.`departments` where employees.DEP_ID = departments.DEPT_ID_DEP; 


# Truy vấn B6: Sử dụng bí danh ngắn hơn cho tên bảng
select * from `hr`.`employees` e
inner join `hr`.`departments` d where e.DEP_ID = d.DEPT_ID_DEP; 

# Truy vấn B7: Chỉ truy xuất Employee ID (ID nhân viên) và Department name (tên phòng ban) trong truy vấn trên 
# Truy vấn B8: Trong truy vấn trên, hãy chỉ định tên cột đủ điều kiện với bí danh trong mệnh đề SELECT 
select e.emp_id, d.DEP_NAME from `hr`.`employees` e
inner join `hr`.`departments` d where e.DEP_ID = d.DEPT_ID_DEP; 
