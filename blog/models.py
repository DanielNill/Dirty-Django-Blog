import settings
from django.db import models
from django.template.defaultfilters import slugify

class Entry(models.Model):
    title = models.CharField(max_length=200)
    title_slug = models.SlugField(blank=True, null=True, unique=True)
    sub_title = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    teaser_html = models.TextField(default='', blank=True, null=True)
    text_html = models.TextField(default='')
    media = models.ManyToManyField('Media', default=None)
    view_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')
    
    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        
        for media in Media.objects.filter(entry=self):
            if media.name != "None":
                self.teaser_html = self.teaser_html.replace('<img_'+media.name+'>', media.media_html)
                self.text_html = self.text_html.replace('<img_'+media.name+'>', media.media_html)
        super(Entry, self).save(*args, **kwargs)
        
    def create_slug(self):
        title_slug = slugify(self.title)
    
    def __unicode__(self):
        return self.title
    
class Media(models.Model):
    name= models.CharField(max_length=75)
    media_file = models.FileField(upload_to='media/images/')
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    media_html = models.CharField(max_length=200, default="")
    
    def save(self, *args, **kwargs):
        self.media_html = "<img src='"+self.media_file.url+"'/>"
        super(Media, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=35)
    
    def __unicode__(self):
        return self.name
