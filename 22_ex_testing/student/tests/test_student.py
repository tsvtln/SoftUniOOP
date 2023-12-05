import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.test_student = Student('Gery', courses={})

    def test_init(self):
        self.assertIsInstance(self.test_student.name, str)
        self.assertIsInstance(self.test_student.courses, dict)

    def test_adding_course_with_notes(self):
        course_name = 'Python'
        notes = ['Basics']
        rez = self.test_student.enroll(course_name, notes, add_course_notes='Y')
        self.assertEqual(self.test_student.courses, {'Python': ['Basics']})
        self.assertEqual(rez, 'Course and course notes have been added.')

    def test_adding_already_added_course(self):
        course_name = 'Python'
        notes = ['Basics']
        notes_new = ['OOP', 'Advanced']
        self.test_student.enroll(course_name, notes)
        add_course_again = self.test_student.enroll(course_name, notes_new)
        self.assertEqual(add_course_again, 'Course already added. Notes have been updated.')

    def test_add_course_without_course_notes(self):
        course_name = 'Python'
        add_notes_to_course = self.test_student.enroll(course_name, '', add_course_notes='N')
        self.assertEqual(add_notes_to_course, 'Course has been added.')
        self.assertEqual(self.test_student.courses, {'Python': []})

    def test_add_notes(self):
        # if course in courses
        course_name = 'Python'
        notes = ['Basics']
        notes_to_add = ['OOP', 'Advanced']
        self.test_student.enroll(course_name, notes)
        rez = self.test_student.add_notes(course_name, notes_to_add)
        self.assertEqual(rez, 'Notes have been updated')
        # if course not in courses
        course_not_in_courses = 'Java'
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes(course_not_in_courses, notes_to_add)
        self.assertEqual(str(ex.exception), 'Cannot add notes. Course not found.')

    def test_leave_course(self):
        # test removing course
        course_name = 'Python'
        notes = ['Basics']
        self.test_student.enroll(course_name, notes)
        rez = self.test_student.leave_course(course_name)
        self.assertEqual(rez, 'Course has been removed')
        # test removing non existent
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course(course_name)
        self.assertEqual(str(ex.exception), 'Cannot remove course. Course not found.')
        non_existent_course = 'Java'
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course(non_existent_course)
        self.assertEqual(str(ex.exception), 'Cannot remove course. Course not found.')

    def test_enroll_empty_notes(self):
        course_name = 'Python'
        notes = []
        rez = self.test_student.enroll(course_name, notes, add_course_notes='N')
        self.assertEqual(rez, 'Course has been added.')
        self.assertEqual(self.test_student.courses, {'Python': []})

    def test_enroll_empty_course_name(self):
        course_name = ''
        notes = ['Basics']
        rez = self.test_student.enroll(course_name, notes)
        self.assertEqual(rez, 'Course and course notes have been added.')
        self.assertEqual(self.test_student.courses, {'': ['Basics']})

    def test_add_notes_empty_course_name(self):
        course_name = ''
        notes = ['Advanced']
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes(course_name, notes)
        self.assertEqual(str(ex.exception), 'Cannot add notes. Course not found.')

    def test_leave_course_empty_course_name(self):
        course_name = ''
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course(course_name)
        self.assertEqual(str(ex.exception), 'Cannot remove course. Course not found.')

    def test_leave_course_none_course_name(self):
        course_name = None
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course(course_name)
        self.assertEqual(str(ex.exception), 'Cannot remove course. Course not found.')


if __name__ == '__main__':
    unittest.main()
