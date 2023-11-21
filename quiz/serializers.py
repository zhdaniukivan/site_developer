from rest_framework import serializers

from quiz.models import Questions, Language, Level


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['title']


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['title']


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ['title', 'text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'true_answer',
                  'comment_to_right_answer']
