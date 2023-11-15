from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def test_instance_attributes_with_courses(self):
        student = Student('Vera',
                          {'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']})
        self.assertEqual('Vera', student.name)
        self.assertEqual({'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']},
                         student.courses)

    def test_instance_attributes_without_courses(self):
        student = Student("Vera")
        self.assertEqual("Vera", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_in_course_when_already_enrolled(self):
        student = Student('Vera',
                          {'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']})

        self.assertEqual("Course already added. Notes have been updated." ,
                         student.enroll('python oop', ['submit last exercise', 'watch final lectures']))
        self.assertEqual(["testing exercise", "mock exam", 'submit last exercise', 'watch final lectures'],student.courses['python oop'])

    def test_enroll_in_coursse_and_add_notes(self):
        student = Student('Vera')
        self.assertEqual("Course and course notes have been added.",student.enroll('python oop', ["testing exercise", "mock exam"]))
        self.assertEqual(["testing exercise", "mock exam"], student.courses['python oop'])

        self.assertEqual("Course and course notes have been added.",student.enroll('python web', ['start project',], 'Y'))

        self.assertEqual(['start project',],student.courses['python web'])


    def test_enroll_in_coursse_and_not_add_notes(self):
        student = Student('Vera')
        self.assertEqual("Course has been added.",student.enroll('JS Advanced', 'learn frontend', 'NO'))
        self.assertEqual([], student.courses['JS Advanced'])


    def test_add_notes_in_existing_course(self):
        student = Student('Vera',
                          {'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']})
        self.assertEqual("Notes have been updated", student.add_notes('python web', 'task 3'))
        self.assertEqual(['watch lectures', 'start project', 'task 3'],student.courses["python web"])
        self.assertEqual("Notes have been updated", student.add_notes('python web', ['task 4', 'task 5']))
        self.assertEqual(['watch lectures', 'start project', 'task 3', ['task 4', 'task 5']],student.courses["python web"])

    def test_raise_exception_adding_notes_to_non_existent_course(self):
        student = Student('Vera')
        with self.assertRaises(Exception) as ex:
            student.add_notes('python oop', 'task 1')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        student = Student('Vera',
                          {'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']})
        self.assertEqual( {'python oop': ["testing exercise", "mock exam"],
                           'python web': ['watch lectures', 'start project']},
                          student.courses)
        self.assertEqual("Course has been removed",student.leave_course('python oop'))
        self.assertEqual({'python web': ['watch lectures', 'start project'],}, student.courses)

    def test_raise_exception_when_leaving_non_existent_course(self):
        student = Student('Vera')
        with self.assertRaises(Exception) as ex:
            student.leave_course('python web')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
if __name__ == '__main__':

    main()