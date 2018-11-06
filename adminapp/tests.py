# from django.test import TestCase
# from adminapp.models import (Student, Subject, Teacher, Parent,
#     Student_Subject_Relation, Student_Teacher_Relation, Subject_Teacher_Relation)
# from django.forms import DecimalField
# from django.test import Client
# from django.urls import reverse
# from users.models import CustomUser
#
# class ModelTestCase(TestCase):
#     def setUp(self):
#         parent1 = Parent.objects.create(father_name="FatherOne", mother_name="MotherOne")
#         user1 = CustomUser.objects.create(username="stud1", email="stud1@email.com")
#         student1 = Student.objects.create(studentid=1, first_name="StudentA", gpa=3.31, parent=parent1, user=user1)
#         parent2 = Parent.objects.create(father_name="FatherTwo", mother_name="MotherTwo")
#         user2 = CustomUser.objects.create(username="stud2", email="stud2@email.com")
#         student2 = Student.objects.create(studentid=2, first_name="StudentB", gpa=3.22, parent=parent2, user=user2)
#         parent3 = Parent.objects.create(father_name="FatherThree", mother_name="MotherThree")
#         user3 = CustomUser.objects.create(username="stud3", email="stud3@email.com")
#         student3 = Student.objects.create(studentid=3, first_name="StudentC", gpa=2.22, parent=parent3, user=user3)
#
#
#     def test_student_parent_relation_1(self):
#         stud1 = Student.objects.get(studentid=1)
#         self.assertEqual(stud1.parent.father_name, "FatherOne")
#         self.assertEqual(stud1.parent.mother_name, "MotherOne")
#
#         stud2 = Student.objects.get(studentid=2)
#         self.assertEqual(stud2.parent.father_name, "FatherTwo")
#         self.assertEqual(stud2.parent.mother_name, "MotherTwo")
#
#     def test_student_hasmany_subjects_2(self):
#         stud1 = Student.objects.get(studentid=1)
#         subject1 = Subject.objects.create(subjectid=1, title="Bio101")
#         subject2 = Subject.objects.create(subjectid=2, title="Chem101")
#         Student_Subject_Relation.objects.create(student=stud1, subject=subject1, grade='A')
#         Student_Subject_Relation.objects.create(student=stud1, subject=subject2, grade='B+')
#         queryset = stud1.subjects.all().order_by('title')
#         subjects = [subject1, subject2]
#         self.assertQuerysetEqual(queryset,[repr(subject) for subject in subjects])
#         self.assertQuerysetEqual(queryset,[str(subject) for subject in subjects])
#
#     def test_subject_hasmany_students_3(self):
#         stud1 = Student.objects.get(studentid=1)
#         stud2 = Student.objects.get(studentid=2)
#         subject1 = Subject.objects.create(subjectid=100, title="CommonCourse101")
#         Student_Subject_Relation.objects.create(student=stud1, subject=subject1)
#         Student_Subject_Relation.objects.create(student=stud2, subject=subject1)
#         """Notice the pluralized 'subjectS' and also double__underscored
#          'subjects__title' in the following line"""
#
#         students_enrolled_for_subject1 = Student.objects.filter(subjects__title="CommonCourse101").order_by('first_name')
#         queryset = students_enrolled_for_subject1
#         students = [stud1, stud2]
#         self.assertQuerysetEqual(queryset,[repr(student) for student in students])
#
#     def test_student_hasmany_teachers_4(self):
#         stud1 = Student.objects.get(studentid=1)
#         teacher1 = Teacher.objects.create(teacherid=111, first_name="TeacherA")
#         teacher2 = Teacher.objects.create(teacherid=222, first_name="TeacherB")
#         teacher3 = Teacher.objects.create(teacherid=333, first_name="TeacherC")
#         Student_Teacher_Relation.objects.create(student=stud1, teacher=teacher1, teacher_comment='V.Good')
#         Student_Teacher_Relation.objects.create(student=stud1, teacher=teacher2, teacher_comment='Good')
#         Student_Teacher_Relation.objects.create(student=stud1, teacher=teacher3, teacher_comment='Fair')
#
#         queryset = stud1.teachers.all().order_by('first_name')
#         teachers = [teacher1, teacher2, teacher3]
#         self.assertQuerysetEqual(queryset,[repr(teacher) for teacher in teachers])
#         self.assertQuerysetEqual(queryset,[str(teacher) for teacher in teachers])
#
#     def test_teachers_hasmany_students_5(self):
#         # We already created THREE STUDENTS in the setUP function above
#
#         teacher1 = Teacher.objects.create(teacherid=111, first_name="TeacherA")
#
#         stud1 = Student.objects.get(studentid=1)
#         stud2 = Student.objects.get(studentid=2)
#         stud3 = Student.objects.get(studentid=3)
#         Student_Teacher_Relation.objects.create(student=stud1, teacher=teacher1)
#         Student_Teacher_Relation.objects.create(student=stud2, teacher=teacher1)
#         Student_Teacher_Relation.objects.create(student=stud3, teacher=teacher1)
#         """Notice the pluralized 'teacherS' and also double__underscored
#          'teachers__first_name' in the following line"""
#         students_thaught_by_teacher1 = Student.objects.filter(teachers__first_name="TeacherA").order_by('first_name')
#         queryset = students_thaught_by_teacher1
#         students = [stud1, stud2, stud3]
#         self.assertQuerysetEqual(queryset,[repr(student) for student in students])
#         self.assertQuerysetEqual(queryset,[str(student) for student in students])
#
#
# class ViewTestCase_page_existence(TestCase):
#     # client = Client()
#
#     def test_initial_page_existence(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_home_page_existence_7(self):
#
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_logged_student_has_access_grade(self):
#
#         client1 = Client()
#         user1 = CustomUser.objects.create(username='stud1', email="stud1@email.com")
#         user1.set_password('12345')
#         user1.save()
#         p1 = Parent.objects.create(father_name="FatherOne", mother_name="MotherOne")
#         s1 = Student.objects.create(studentid=1, first_name="StudentOne", gpa=3.31, parent=p1, user=user1)
#         client1.user = user1
#         client1.login(username='stud1', password='12345')
#         response = client1.get(reverse('grades', args=[1]))
#         self.assertEqual(response.status_code, 200)
#
#     def test_logged_student_no_access_others_grade(self):
#         """ StudentTwo login and logout """
#         client2 = Client()
#         user2 = CustomUser.objects.create(username='stud2', email="stud2@email.com")
#         user2.set_password('9999')
#         user2.save()
#         p2 = Parent.objects.create(father_name="FatherTwo", mother_name="MotherTwo")
#         s2 = Student.objects.create(studentid=2, first_name="StudentTwo", gpa=2.51, parent=p2, user=user2)
#         user2.student = s2
#         user2.save()
#         client2.user = user2
#         client2.login(username='stud2', password='9999')
#         client2.logout
#         """ StudentOne trying to access StudentTwo information"""
#         client1 = Client()
#         user1 = CustomUser.objects.create(username='stud1', email="stud1@email.com")
#         user1.set_password('12345')
#         user1.save()
#         p1 = Parent.objects.create(father_name="FatherOne", mother_name="MotherOne")
#         s1 = Student.objects.create(studentid=1, first_name="StudentOne", gpa=3.31, parent=p1, user=user1)
#         user1.student = s1
#         s1.save()
#         client1.user = user1
#
#         client1.login(username='stud1', password='12345')
#         response = client1.get(reverse('grades', args=[2]))
#         self.assertEqual(response.status_code, 404)
#
#
#         # response = self.client.get(reverse('grades', args=[2]))
#         # self.assertEqual(response.status_code, 200)
