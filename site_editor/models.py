from django.db import models

# Create your models here.
class Index(models.Model):
	carousel_image 			 = models.ImageField(upload_to='public/static/media/home/')
	carousel_title 			 = models.CharField(max_length=200)
	carousel_description = models.CharField(max_length=750)
	class Meta:
		unique_together = ('carousel_title', 'carousel_description')
	def __unicode__(self):
		return self.carousel_title

class Media(models.Model):
	IMAGECHOICE = (
			('0', 'FRC'),
			('1', 'VEX'),
		)
	image 			= models.ImageField(upload_to='public/static/media/photos/')
	year 				= models.IntegerField()
	album 			= models.CharField(max_length=200)
	competition = models.CharField(max_length=1, choices=IMAGECHOICE)
	class Meta:
		unique_together = ('album', 'competition')
	def __unicode__(self):
		return self.album
		