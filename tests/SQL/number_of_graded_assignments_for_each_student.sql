-- Write query to get number of graded assignments for each student:
SELECT students.id AS Student, COUNT(*) as Graded_Assignment FROM students, assignments WHERE students.id=assignments.student_id GROUP BY students.id;