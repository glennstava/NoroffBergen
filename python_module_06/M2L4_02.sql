SELECT * 
  FROM students LEFT OUTER JOIN enrollments
    ON (students.student_id = enrollments.student_id)

SELECT * 
  FROM students RIGHT OUTER JOIN enrollments
    ON (students.student_id = enrollments.student_id)

SELECT CONCAT_WS(" ", students.first_name, students.last_name) 
AS Student, courses.course_full_name
FROM students LEFT OUTER JOIN enrollments
ON (students.student_id = enrollments.student_id)
LEFT OUTER JOIN courses 
ON (enrollments.course_code = courses.course_code)


SELECT students.student_id, CONCAT_WS(" ", students.first_name, students.last_name) AS Student,
IFNULL(courses.course_full_name, '-')
FROM students LEFT OUTER JOIN enrollments
ON (students.student_id = enrollments.student_id)
LEFT OUTER JOIN courses ON (enrollments.course_code = courses.course_code)

SELECT e2.course_code, 
	   e2.start_date, 
       s2.first_name, 
       s2.last_name
			FROM students AS s1, 
			     students AS s2, 
				   enrollments AS e1, 
				   enrollments As e2
						WHERE s1.first_name = "Justin"
						  AND s1.last_name = "Case"
						  AND e1.course_code = "SQL1"
						  AND e1.student_id = s1.student_id
						  AND e2.course_code = e1.course_code
						  AND e2.start_date = e1.start_date
						  AND e2.student_id = s2.student_id;

SELECT * FROM people p, companies c 
 WHERE p.companyID = c.id 
   AND p.firstName = 'Daniel'

SELECT * FROM people p 
  JOIN companies c ON p.companyID = c.id
 WHERE p.firstName = 'Daniel'