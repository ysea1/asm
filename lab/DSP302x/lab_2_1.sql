#CREATE SCHEMA `hr` ;

# Truy vấn 1: Truy xuất tất cả nhân viên có địa chỉ ở Elgin, IL
select * from `hr`.`employees` where `address` like '%Elgin,IL%';

# Truy vấn 2: Truy xuất tất cả nhân viên sinh vào những năm 1970.
select * from `hr`.`employees` where year(b_date)  = 1972;

# Truy vấn 3: Truy xuất tất cả nhân viên trong phòng ban 5 có mức lương từ 60000 đến 70000.
select * from `hr`.`employees` where dep_id = 5 and salary between 60000 and 70000;

# Truy vấn 4A: Truy xuất danh sách nhân viên được sắp xếp theo ID phòng ban.
select * from `hr`.`employees` order by dep_id;


# Truy vấn 4B: Truy xuất danh sách nhân viên được sắp xếp theo thứ tự giảm dần theo ID phòng ban và trong mỗi phòng ban, 
# những nhân viên này được sắp xếp theo họ với thứ tự giảm dần của bảng chữ cái.
select * from `hr`.`employees` order by dep_id desc, l_name desc;


# Truy vấn 5A: Đối với mỗi ID phòng ban, truy xuất số lượng nhân viên trong phòng ban.
select dep_id, count(*) from `hr`.`employees`
group by dep_id;

# Truy vấn 5B: Đối với mỗi phòng ban, truy xuất số lượng nhân viên trong phòng ban và mức lương trung bình của nhân viên 
# trong phòng ban.
select dep_id, count(*), avg(salary) from `hr`.`employees`
group by dep_id;

# Truy vấn 5C: Gắn nhãn các cột đã tính trong tập hợp kết quả của Truy vấn 5B là NUM_EMPLOYEES và AVG_SALARY.
select dep_id, count(*) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY from `hr`.`employees`
group by dep_id;


# Truy vấn 5D: Trong Truy vấn 5C, hãy sắp xếp tập hợp kết quả Mức lương trung bình.
select dep_id, count(*) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY from `hr`.`employees`
group by dep_id
order by AVG_SALARY;


# Truy vấn 5E: Trong Truy vấn 5D, giới hạn kết quả thành ít hơn 4 nhân viên cho các phòng ban.
select dep_id, count(*) as NUM_EMPLOYEES, avg(salary) as AVG_SALARY from `hr`.`employees`
group by dep_id
having count(*) < 4
order by AVG_SALARY;