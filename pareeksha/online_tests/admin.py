# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject, Topic, OnlineTest, Problem, Option

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(OnlineTest)
admin.site.register(Problem)
admin.site.register(Option)
