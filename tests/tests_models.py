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
        self.assertEqual(post_count, 1)

    def test_fixture_language(self):
        post_count = Language.objects.count()
        self.assertEqual(post_count, 1)

    def test_fixture_questions(self):
        post_count = Questions.objects.count()
        self.assertEqual(post_count, 1)


