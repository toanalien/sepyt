from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Question model
# question_text : char
# pub_date : datetime

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # fix objects representations
    def __str__(self):
        return self.question_text

    # return true if pub_date in recent 7 days
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model
# question : foreignkey
# choice_text : char
# votes : integer

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # fix objects representations
    def __str__(self):
        return self.choice_text