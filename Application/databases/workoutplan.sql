create table workoutplan(
plan_id int primary key not null auto_increment,
plan_name varchar(20) not null,
plan_time time not null,
plan_intensity varchar(20) not null
);

insert into workoutplan (plan_id,plan_name,plan_time,plan_intensity) VALUES 
(1,'PowerFit',25,'Low'),
(2,'Lean and Strong',15,'Moderate'),
(3,'Total Transformation',30,'High'),
(4,'Core Blast',20,'High'),
(5,'Speed Circuit',30,'High'),
(6,'Sports Domination',30,'High');

select * from workoutplan;