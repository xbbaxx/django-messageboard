#coding:utf-8

from django.db import models
from django.utils import timezone



class Message(models.Model):
    author = models.CharField(u'姓名', max_length=200)
    text = models.TextField(u'内容')
    create_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.author


