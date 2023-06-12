create table exercise(
exercise_id int primary key not null auto_increment,
exercise_name varchar(100) not null,
exercise_time time not null,
exercise_intensity varchar(20) not null,
exercise_desc varchar(100),
reps int(3) not null
);

insert into exercise (exercise_id,exercise_name,exercise_time,exercise_intensity,exercise_desc,reps) VALUES 
(1,'Deadlifts','00:05:00','High','Compound exercise targetting the lower body',20),
(2,'Squat Jumps','00:03:00','Moderate','Explosive lower body exercise',50),
(3,'Power cleans','00:02:00','Low','Full-body movememt emphasizing exercise',10),
(4,'Bensh Press','00:04:00','High','Upper body strength exercise',20),
(5,'Medicine ball slams','00:02:00','Moderate','Dynamic core and upper body exercise',30),
(6,'Box jumps','00:03:00','Low','Plyometric exercise for lower body power',40),
(7,'Push Press','00:03:00','High','Upper body and leg power movement',15),
(8,'Kettlebell swings','00:02:00','High','Hip hinging exercise for total body workout',20),
(9,'Lunges','00:05:00','Moderate','Lower body exercise for strength and balance',25),
(10,'Plank Rows','00:04:00','Low','Core and back exercise with rowing motions',30),
(11,'Dumbbell shoulder press','00:05:00','High','Shoulder strength exercise',20),
(12,'Step-ups','00:05:00','High','Lower body exercise using a step or bench',20),
(13,'Renegade rows','00:05:00','High','Core and upper body exercise',20),
(14,'Barbell Hip thrusts','00:05:00','High','Glute-building exercise',20),
(15,'Tricep dips','00:05:00','High','Tricep strengthening exercise',20),
(16,'Lat pulldowns','00:05:00','High','Back and arm exercise',20),
(17,'Burpees','00:05:00','High','Full body exercise for cardiovascular fitness',20),
(18,'Mountain climbers','00:05:00','High','Dynamic core and cardiovuscular exercise',20),
(19,'Russian Twists','00:05:00','High','Abdominal exercise for core strength',20),
(20,'Jmping Lunges','00:05:00','High','Plyometric exercise for lowerbody strength',20),
(21,'Bicycle crunches','00:05:00','High','Abdominal exercise for core stabilities',20),
(22,'Plank with leg lifts','00:03:00','Moderate','Core exercise with leg lift variations',50),
(23,'High knees','00:02:00','Low','Cardiovuscular exercise with knee lifts',10),
(24,'Side plank with hip dips','00:04:00','High','Oblique and core exercise with hip movements',20),
(25,'Plank Variations','00:02:00','Moderate','Core exercise with different plank positions',30),
(26,'V-ups','00:03:00','Low','Abdominal exercise for core strength',40),
(27,'Sprints','00:03:00','High','High intensity running exercise',15),
(28,'Reverse Crunches','00:02:00','High','Abdominal exercise targetting lower abs',20),
(29,'Hanging Leg Raises','00:05:00','Moderate','Core and hip flexor exercise',25),
(30,'Woodchoppers','00:04:00','Low','Core exercise with rotational movements',30);

select * from exercise;


select * from exercise where exercise_id in (2,3,5,6,7);


