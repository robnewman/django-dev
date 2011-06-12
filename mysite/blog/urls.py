# This also imports the include function
from django.conf.urls.defaults import *
from mysite.blog.models import Article
from tagging.views import tagged_object_list
from django.views.generic import date_based

articles_info = {
    'queryset'             : Article.objects.all(),
    'date_field'           : 'date',
    'template_name'        : 'blog/list.html',
    'template_object_name' : 'posts',
}

urlpatterns = patterns('',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[^.*]+)/$', date_based.object_detail, dict(articles_info, slug_field='slug', template_name='blog/detail.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', date_based.archive_day, articles_info),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', date_based.archive_month, articles_info),
    (r'^(?P<year>\d{4})/$', date_based.archive_year, dict(articles_info, make_object_list=True)),
    (r'^$', date_based.archive_index, articles_info),
    (r'^tag/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'blog.tag_views.tag_detail'),
)
