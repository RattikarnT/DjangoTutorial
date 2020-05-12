from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models

#admin.site.register(Post)

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
	list_display=["tutorial_title","tutorial_updated","tutorial_published"]
	list_display_links=["tutorial_updated"]
	list_editable=["tutorial_title"]
	list_filter=["tutorial_updated","tutorial_published"]
	search_fields=["tutorial_title","tutorial_content"]

	'''class Meta:
		model=Tutorial'''
	'''fields=["tutorial_title",
			"tutorial_published",
			"tutorial_content"]'''
	fieldsets=[
		("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
		("URL",{"fields": ["tutorial_slug"]}),
		("Series",{"fields": ["tutorial_series"]}),
		("Image",{"fields":["tutorial_image"]}),
		("Content",{"fields": ["tutorial_content"]})

	]
	formfield_overrides={
		models.TextField:{'widget': TinyMCE()}
	}
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
