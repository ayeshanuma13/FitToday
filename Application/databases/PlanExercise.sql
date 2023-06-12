drop table PlanExercise;

create table PlanExercise(
plan_id int,
exercise_id int,
sequence int,
FOREIGN KEY (plan_id) REFERENCES workoutplan(plan_id),
FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id));

select * from PlanExercise;

insert into PlanExercise (plan_id,exercise_id,sequence) VALUES 
(1,1,1),
(1,2,2),
(1,3,3),
(1,4,4),
(1,5,5),
(2,6,1),
(2,7,2),
(2,8,3),
(2,9,4),
(2,10,5),
(3,11,1),
(3,12,2),
(3,13,3),
(3,14,4),
(3,15,5),
(4,16,1),
(4,17,2),
(4,18,3),
(4,19,4),
(4,20,5),
(5,21,1),
(5,22,2),
(5,23,3),
(5,24,4),
(5,25,5),
(6,26,1),
(6,27,2),
(6,28,3),
(6,29,4),
(6,30,5);

SELECT workoutplan.*,exercise.* FROM exercise 
INNER JOIN PlanExercise ON exercise.exercise_id = PlanExercise.exercise_id 
INNER JOIN workoutplan ON workoutplan.plan_id = PlanExercise.plan_id
WHERE PlanExercise.plan_id = 1;

SELECT e.*
        FROM exercise e
        INNER JOIN PlanExercise pe ON pe.exercise_id=e.exercise_id
        WHERE pe.plan_id =2
        ORDER BY pe.sequence;
select * from PlanExercise;