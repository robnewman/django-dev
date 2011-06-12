from django.db import models
from tagging.fields import TagField
from tagging.models import Tag

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique_for_date = 'date',
        help_text       = 'Built from title'
    )
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='assets/images/blog/uploaded_images')
    author = models.ForeignKey(Author)
    date = models.DateField()
    enable_comments = models.BooleanField(default=True)
    tags = TagField()

    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'
        verbose_name_plural = 'articles'

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def get_previous_published(self):
        return self.get_previous_by_date()
         
    def get_next_published(self):
        return self.get_next_by_date()


    def __unicode__(self):
        return u'%s by %s' % (self.title, self.author)

    def get_absolute_url(self):
        return "/%s/%s/" %(self.date.strftime("%Y/%b/%d").lower(), self.slug)
