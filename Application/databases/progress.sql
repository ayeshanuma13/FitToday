use fittoday;

create table progress(
progress_id int primary key auto_increment,
user_id int,
plan_id int,
completion_date date,
completion_time time);

insert into progress(user_id,plan_id,completion_date,completion_time) VALUES 
(1,1,'2023-06-01','11:30:00');

select * from progress;

select workoutplan.plan_name,progress.completion_date,progress.completion_time from progress inner join workoutplan on workoutplan.plan_id=progress.plan_id where user_id=1;
select user_id,(select COUNT(completion_date) from progress group by user_id) as count from progress;

select count from (select user_id,COUNT(completion_date) as count from progress group by user_id) userDayCount where user_id=7;
select user_id,COUNT(completion_date) as count from progress group by user_id;

select COUNT(*) from progress where user_id=3;