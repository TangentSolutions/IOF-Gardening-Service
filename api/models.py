from __future__ import unicode_literals

from django.db import models

class Garden(models.Model):
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	name = models.CharField(max_length=255, db_index=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Garden'
		verbose_name_plural = 'Gardens'

class Data(models.Model):

	garden = models.ForeignKey(Garden)
	temperature = models.FloatField(null=True)
	humidity = models.FloatField(null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Data Reading'
		verbose_name_plural = 'Data Readings'