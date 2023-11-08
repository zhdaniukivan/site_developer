from django.test import TestCase
from quiz.models import Level, Questions, Language


class QuizModelsTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        Level.objects.create(title='junior')
        Level.objects.create(title='midl')
        Level.objects.create(title='senor')

    def test_first_name_label(self):
        level = Level.objects.get(id=1)
        field_label = level._meta.get("title").verbose_name
        self.assertEqual(field_label, 'title')

    def test_object_fields(self):
        level = Level.objects.get(id=1)
        print(level)
        expected_object_title = level.title
        self.assertEqual(expected_object_title, str(level))
        print("**************************")
        print(expected_object_title)
        print("**************************")

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)


    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1*2, 2)

