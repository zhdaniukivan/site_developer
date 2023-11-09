from django.test import TestCase
from quiz.models import Level, Language, Questions

# python manage.py dumpdata [app_name.ModelName] --output=[filename]
# python manage.py dumpdata blog.Post --output=post_fixture.xml --format=xml --exclude=blog.Post.author --indent 2
# https://docs.djangoproject.com/en/4.2/topics/db/queries/
#  https://vegibit.com/what-are-django-fixtures-and-how-to-use-them-for-data-loading-and-testing/


class QuizModelsTest(TestCase):
    fixtures = ["level_fixture.json", "language_fixture.json", "questions_fixture.json"]

    def test_fixture_level(self):
        post_count = Level.objects.count()
        self.assertEqual(post_count, 2)

    def test_fixture_language(self):
        post_count = Language.objects.count()
        self.assertEqual(post_count, 2)

    def test_fixture_questions(self):
        post_count = Questions.objects.count()
        self.assertEqual(post_count, )



    # @classmethod
    # def setUpTestData(cls):
    #     Level.objects.create(title='Junior')
    #     Language.objects.create(title='Python')
    #     Questions.objects.create(language='1', level='1', tetle='best questions', text='what is lambda?',
    #                              answer_1='func', answer_2='anonymous func', answer_3='log', answer_4='bob',
    #                              true_answer='2', comment_to_right_answer='it is not difficult questions')
    #
    # def setUp(self):
    #     fixtures = ['language.json']
    #     Level.objects.create(title='Middle')
    #     Level.objects.create(title='Senor')

    # def test_first_name_label(self):
    #     level = Level.objects.get(id=1)
    #     field_label = level._meta.get("title").verbose_name
    #     self.assertEqual(field_label, 'title')
    #
    # def test_object_fields_model_level(self):
    #     level = Level.objects.get(id=1)
    #     expected_object_title = level.title
    #     self.assertEqual(expected_object_title, str(level))
    #
    # def test_object_fields_model_language(self):
    #     language = Language.objects.get(id=1)
    #     expected_object_title = language.title
    #     self.assertEqual(expected_object_title, str(language))
    #
    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)
    #
    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(True)
    #
    #
    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1*2, 2)

#
# import unittest
# from django.test import Client
#
#
# class SimpleTest(unittest.TestCase):
#     def setUp(self):
#         # Every test needs a client.
#         self.client = Client()
#
#     def test_details(self):
#         # Issue a GET request.
#         response = self.client.get("/customer/details/")
#
#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the rendered context contains 5 customers.
#         self.assertEqual(len(response.context["customers"]), 5)

# import unittest
# from django.test import Client


# class SimpleTest(unittest.TestCase):
#     def test_details(self):
#         client = Client()
#         response = client.get("http://127.0.0.1:8000/")
#         self.assertEqual(response.status_code, 404)

    # def test_index(self):
    #     client = Client()
    #     response = client.get("/customer/index/")
    #     self.assertEqual(response.status_code, 200)

