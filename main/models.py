from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    timestamp= models.DateTimeField("date published",default=datetime.now())
	#stamp_updated= models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title



class TutorialCategory(models.Model):
	tutorial_category=models.CharField(max_length=200)
	category_summary=models.CharField(max_length=200)
	category_slug=models.CharField(max_length=200)

	class Meta:
		verbose_name_plural="Categories"

	def __str__(self):
		return str(self.tutorial_category)

class TutorialSeries(models.Model):
	tutorial_series= models.CharField(max_length=200)
	tutorial_category=  models.ForeignKey(TutorialCategory, default=1, verbose_name="Category",on_delete=models.SET_DEFAULT)
	series_summary= models.CharField(max_length=200)

	class Meta:
		verbose_name_plural="Series"

	def __str__(self):
		return str(self.tutorial_series)


# Create your models here.
class Tutorial(models.Model):
	tutorial_title=models.CharField(max_length=200)
	tutorial_content= models.TextField()
	tutorial_image = models.ImageField(null=True, blank=True,
					 width_field="width_field",
					 height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	tutorial_published= models.DateTimeField("date published",default=datetime.now())
	tutorial_updated= models.DateTimeField(auto_now=True,auto_now_add=False)
	tutorial_series=models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug=models.CharField(max_length=200, default=1)

	def __str__(self):
		return str(self.tutorial_title)

	'''def get_absolute_url(self):
		return reverse()'''
