from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def cache_blog():
    if settings.CACHE_ENABLED:
        key = 'post'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Blog.objects.all()
            cache.set(key, subject_list)
    else:
        subject_list = Blog.objects.all()
    return subject_list
