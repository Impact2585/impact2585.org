from django.db import models
import os
# Create your models here.
def getListOfImages(path):
	media_images = [];
	for dirpath, dirname, files in os.walk(path):
		media_images.extend(files)
	return [(media_images[i], media_images[i]) for i in range(0, len(media_images))]

class IndexVideo(models.Model):
	media_type = '1'
	carousel_title = models.CharField(max_length=200)
	carousel_description = models.CharField(max_length=200)
	carousel_media_file_name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.carousel_title

class IndexImage(models.Model):
	media_type = '0'
	carousel_title = models.CharField(max_length=200)
	carousel_description = models.CharField(max_length=200)
	carousel_media_file_name = models.CharField(max_length=200, choices=getListOfImages('public/static/media/photos'))
	def __unicode__(self):
		return self.carousel_title

class Media(models.Model):
	IMAGECHOICE = (
			('0', 'FRC'),
			('1', 'VEX'),
		)

	image = models.ImageField(upload_to='public/static/media/photos/')
	year = models.IntegerField()
	album = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.album;

class Robot(models.Model):
	ROBOTCHOICE = (
			('0', 'FRC'),
			('1', 'VEX'),
		)

	ROBOTIMAGECHOICE = getListOfImages('public/static/media/photos')
	robot_name = models.CharField(max_length=100)
	game_name = models.CharField(max_length=100)
	game_year = models.IntegerField()
	description = models.CharField(max_length=500)
	robot_image_file_name = models.CharField(max_length=200, choices = ROBOTIMAGECHOICE)
	competition = models.CharField(max_length=1, choices=ROBOTCHOICE)
	def __unicode__(self):
		return self.robot_name

class Sponsor(models.Model):
	TIERCHOICE = (
			('0', 'Platinum'),
			('1', 'Gold'),
			('2', 'Bronze')
		)
	sponsor_image = models.ImageField(upload_to='public/static/media/sponsors')
	sponsor_tier = models.CharField(max_length=1, choices=TIERCHOICE)
	def __unicode__(self):
		return self.sponsor_tier

class Link(models.Model):
	name = models.CharField(max_length = 100);
	url = models.CharField(max_length = 100);
	def __unicode__(self):
		return self.name;
