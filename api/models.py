# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Students(models.Model):
	first_name = models.Charfield(max_length=255)
	last_name = models.Charfield(max_length=255)
