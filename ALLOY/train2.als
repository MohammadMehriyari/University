abstract sig Person {
 id: one Int,
 name: one String
}

sig Teacher extends Person {
 courses: set Course
}

sig Student extends Person {
 enrolledCourses: set Course
}

sig Course {
 id: one Int,
 name: one String,
 teacher: one Teacher,
 resources: set Resource
}

sig Resource {
 id: one Int,
 name: one String,
 type: one String
}

fact {
 all s: Student | some c: Course | c in s.enrolledCourses
 all t: Teacher | some c: Course | c in t.courses
 all c: Course | some r: Resource | r in c.resources
}

pred enrolledInCourse[s: Student, c: Course] {
 s in c.enrolledCourses
}

pred teachesCourse[t: Teacher, c: Course] {
 t in c.teacher
}

pred hasResource[c: Course, r: Resource] {
 r in c.resources
}

pred courseHasTeacher[c: Course, t: Teacher] {
 t in c.teacher
}

pred studentHasTeacher[s: Student, t: Teacher] {
 t in s.enrolledCourses.teacher
}
run enrolledInCourse for 5
