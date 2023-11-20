from django.db import models



class Language(models.Model):
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title


class Level(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Questions(models.Model):
    language = models.ManyToManyField(Language, related_name='language')
    leve = models.ManyToManyField(Level, related_name='leve')
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=800)
    answer_1 = models.CharField(max_length=800)
    answer_2 = models.CharField(max_length=800)
    answer_3 = models.CharField(max_length=800)
    answer_4 = models.CharField(max_length=800)
    true_answer = models.IntegerField()
    comment_to_right_answer = models.CharField(max_length=400)

    def __str__(self):
        return f'Вопрос: {self.title} | язык: {self.language} | уровень: {self.leve}'







