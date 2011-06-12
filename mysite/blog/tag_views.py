from django.views.generic.list_detail import object_list

from tagging.models import Tag,TaggedItem
from models import Article

def tag_detail(request, slug):
    clean_slug = slug.replace('-', ' ')
    tag = Tag.objects.get(name=clean_slug)
    query = TaggedItem.objects.get_by_model(Article, tag)
    return object_list(request, queryset=query, extra_context={'tag':slug}, template_name='tags/list.html')


