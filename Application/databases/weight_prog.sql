drop table weight_prog;

create table weight_prog(
user_id INT,
weight_date DATE,
weight VARCHAR(100)
);

INSERT into weight_prog(user_id,weight_date,weight) VALUES(1,'2023-06-01','61.2');

select weight_arr from (SELECT group_concat(weight) as weight_arr FROM weight_prog group by user_id) weighttable where user_id=2;
select * from weight_prog;
SELECT group_concat(weight),group_concat(weight_date) FROM weight_prog where user_id=1 group by user_id;
SELECT group_concat(weight) as weight_arr FROM weight_prog where user_id=2 group by user_id;
SELECT weight from weight_prog WHERE user_id=1 and weight_date=(select max(weight_date) from weight_prog where user_id=1)