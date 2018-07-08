# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User

class Standard(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def get_online_tests(self):
        return self.online_tests.all()

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_topics(self):
        return self.topics.all()

class Topic(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, related_name="topics", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class OnlineTest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    standard = models.ForeignKey(Standard, related_name="online_tests", on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, related_name="online_tests", on_delete=models.SET_NULL, null=True, blank=True)
    creator = models.ForeignKey(User, related_name="online_tests", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    duration_hours = models.IntegerField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Problem(models.Model):
    test = models.ForeignKey(OnlineTest, related_name="problems", on_delete=models.CASCADE)
    statement = models.TextField()
    score = models.IntegerField(default=1)
    multiple_choices_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.statement

class Option(models.Model):
    problem = models.ForeignKey(Problem, related_name="options", on_delete=models.CASCADE)
    statement = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.statement
