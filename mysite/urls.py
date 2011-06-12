# This also imports the include function
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Article
from tagging.views import tagged_object_list

from django.views.generic import list_detail, date_based

articles_info = {
    'queryset'             : Article.objects.all(),
    'date_field'           : 'date',
    'template_name'        : 'blog/list.html',
    'template_object_name' : 'posts',
}

urlpatterns = patterns('mysite',
    (r'^blog/', include('blog.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
