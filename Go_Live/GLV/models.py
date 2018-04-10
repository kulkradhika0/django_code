# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class USER_MASTER(models.Model):
	USER_ID = models.IntegerField(primary_key=True)
	USERNAME = models.CharField(max_length = 40,null=True)
	PASSCODE = models.IntegerField(null=True)
<<<<<<< HEAD
	ORDER_ID = models.IntegerField(null=True)
=======
	ORDER_ID = models.IntegerField(null=True)
>>>>>>> 8422d38801702f72490835fb656cc79b35fda5fa
