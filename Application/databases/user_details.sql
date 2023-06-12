create table user_details(
userid int primary key not null auto_increment,
username varchar(20) not null,
email varchar(50) not null,
password varchar(20) not null,
gender varchar(10),
age int(3) not null,
height int(3),
weight int(3)
)

select * from user_details;