# Truy vấn A1: Nhập một hàm tính tổng chi phí của tất cả những lần cứu hộ động vật trong bảng PETRESCUE.
select sum(cost) from `hr`.`PETRESCUE`;

# Truy vấn A2: Nhập một hàm hiển thị tổng chi phí của tất cả những lần cứu hộ động vật trong bảng PETRESCUE trong cột SUM_OF_COST.
select sum(cost) as SUM_OF_COST from `hr`.`PETRESCUE`;


# Truy vấn A3: Nhập một hàm hiển thị số lượng động vật tối đa được cứu hộ.
select max(quantity) from `hr`.`PETRESCUE`;


# Truy vấn A4: Nhập một hàm hiển thị chi phí trung bình của động vật được cứu hộ.
select avg(cost) from `hr`.`PETRESCUE`;

# Truy vấn A5: Nhập một hàm hiển thị chi phí cứu hộ trung bình cho một chú chó.
select avg(cost) from `hr`.`PETRESCUE` where animal = 'Dog';


# Truy vấn B1: Nhập một hàm hiển thị chi phí làm tròn của mỗi lần cứu hộ.
select id, animal, quantity, round(cost) as cost, rescuedate from `hr`.`PETRESCUE`;


# Truy vấn B2: Nhập hàm hiển thị độ dài của tên từng con vật.
select id, animal, length(animal), quantity, round(cost) as cost, rescuedate from `hr`.`PETRESCUE`;

# Truy vấn B3: Nhập hàm hiển thị tên con vật trong mỗi lần cứu hộ bằng chữ hoa
select id, animal, upper(animal), quantity, round(cost) as cost, rescuedate from `hr`.`PETRESCUE`;

# Truy vấn B4: Nhập hàm hiển thị tên con vật trong mỗi lần cứu hộ bằng chữ hoa và không trùng lặp.
select distinct upper(animal) from `hr`.`PETRESCUE`;


# Truy vấn B5: Nhập một truy vấn hiển thị tất cả các cột từ bảng PETRESCUE, 
# trong đó (các) con vật được cứu hộ là mèo. Sử dụng cat chữ thường trong truy vấn.
select * from `hr`.`PETRESCUE`
where lower(animal) = 'cat';


# Truy vấn C1: Nhập một hàm hiển thị ngày trong tháng mèo được cứu hộ.
select day(Rescuedate) from `hr`.`PETRESCUE`
where lower(animal) = 'cat';

# Truy vấn C2: Nhập hàm hiển thị số lần cứu hộ vào tháng thứ 5.
select * from `hr`.`PETRESCUE`
where month(rescuedate) = 5;


# Truy vấn C3: Nhập hàm hiển thị số lần cứu hộ vào ngày 14 trong tháng
select count(*) from `hr`.`PETRESCUE`
where day(rescuedate) = 14;


# Truy vấn C4: Động vật được cứu hộ nên được đưa tới phòng khám thú y trong vòng ba ngày kể từ ngày được cứu hộ. 
# Nhập một hàm hiển thị ngày thứ ba từ mỗi lần cứu hộ.
select *, date_add(rescuedate, interval 3 day) as nextday from `hr`.`PETRESCUE`;

# Truy vấn C5: Nhập một hàm hiển thị khoảng thời gian các động vật được cứu hộ; sự khác biệt giữa ngày hôm nay và ngày giải cứu.
select *, now() as current, datediff(now(), rescuedate) as rangedate from `hr`.`PETRESCUE`;