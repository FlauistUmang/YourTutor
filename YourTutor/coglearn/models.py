from __future__ import unicode_literals
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import os

class Student(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.EmailField()
    school = models.CharField(max_length = 100)


class Teacher(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()


class Topic(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    def __str__(self):
        return self.title

class SubTopic(models.Model):
    title = models.CharField(max_length = 100)
    file = models.TextField(blank=True, null=True) # url of the file or content
    #how to link this url with urls.py??
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class AssessmentNode(MPTTModel):
    lock = models.BooleanField(default=False)
    leaf = models.BooleanField(default=False)
    parent = TreeForeignKey('self', null = True, blank = True, related_name = 'children')
    weight = models.PositiveIntegerField(null=True, blank=True)


class Progress(models.Model):
    #Everything we need to model the learning progress
    studentid = models.OneToOneField(
        Student,
        on_delete = models.CASCADE
    )
    root = models.ForeignKey(AssessmentNode, on_delete=models.CASCADE)
    #learningGraph 
    #topic
    #subtopic
    #scoreInCurrentTopic
    #overallScore


