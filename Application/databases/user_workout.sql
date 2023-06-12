drop table user_workout;

create table user_workout(
custom_id int primary key auto_increment,
user_id int,
plan_id int,
exercise_id varchar(100),
completion_date date,
completion_time time);

insert into user_workout(user_id,plan_id,exercise_id,completion_date,completion_time) VALUES 
(1,1,'1,2,3,4,5','2023-06-01','11:30:00'),
(1,2,'6,7,8,9,10','2023-06-02','11:30:00'),
(1,3,'11,12,13,14,15','2023-06-03','11:30:00'),
(1,4,'16,17,18,19,20','2023-06-04','11:30:00'),
(1,5,'21,22,23,24,25','2023-06-05','11:30:00'),
(1,6,'26,27,28,29,30','2023-06-06','11:30:00');
truncate user_workout;
select * from user_workout;
alter table user_workout Drop column completion_time;
update user_workout set exercise_id='1,2,3,4,5' where plan_id=1 and user_id=2;

SET SQL_SAFE_UPDATES = 0;
