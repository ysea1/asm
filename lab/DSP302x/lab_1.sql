CREATE SCHEMA `ds_lab` ;


------- TASK 1 ----------------
CREATE TABLE `ds_lab`.`instructor` (
  `ins_id` INT NOT NULL AUTO_INCREMENT,
  `lastname` VARCHAR(100) NOT NULL,
  `firstname` VARCHAR(100) NOT NULL,
  `city` VARCHAR(100) NULL,
  `country` CHAR(2) NULL,
  PRIMARY KEY (`ins_id`));
  
 
 ------- TASK 2A ---------------
 INSERT INTO `ds_lab`.`instructor` (`lastname`, `firstname`, `city`, `country`) VALUES ('Ahuja', 'Rav', 'Toronto', 'CA');
 
  ------- TASK 2B ---------------
 INSERT INTO `ds_lab`.`instructor` (`lastname`, `firstname`, `city`, `country`) VALUES ('Chong', 'Raul', 'Toronto', 'CA');
 INSERT INTO `ds_lab`.`instructor` (`lastname`, `firstname`, `city`, `country`) VALUES ('Vasudevan', 'Hima', 'Chicago', 'US');
 
 ---------- TASK 3 ----------------
 SELECT * FROM `ds_lab`.`instructor`;
 
  ---------- TASK 3B ----------------
 SELECT * FROM `ds_lab`.`instructor` WHERE `city` = 'Toronto';
 
 ---------- TASK 4 ----------------
 update `ds_lab`.`instructor` set `city` = 'Markham' where lastname = 'Ahuja' and firstname = 'Rav';
 
 ---------- TASK 5 ----------------
 delete from `ds_lab`.`instructor` where `ins_id` = 2;
 
  ---------- TASK 5B ----------------
 SELECT * FROM `ds_lab`.`instructor`;