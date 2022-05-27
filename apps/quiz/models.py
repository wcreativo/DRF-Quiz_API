from django.db import models
from django.utils.translation import gettext_lazy as _


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name='Last updated', auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length=255, verbose_name='Quiz title')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    TYPE = ((0, _('Multiple Choice')),)

    quiz = models.ForeignKey(Quizzes, on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Question'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.question
