from django.conf.urls import url

from blog.views import PostLV, PostDV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV

urlpatterns = [
    # /
    url(r'^$', PostLV.as_view(), name='index'),

    # /post/
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # /archive/
    url(r'^archive/$', PostAV.as_view(), name= 'post_archive'),

    # /2017/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # /2017/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # /2017/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # /today/
    url(r'^today/$', PostTAV.as_view(), name='poost_today_archive'),
]