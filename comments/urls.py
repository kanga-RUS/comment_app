from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^comment/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^view/$', views.CommentListView.as_view(), name='comment_list'),
    url(r'^view/(?P<comment_id>[0-9]+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^view/(?P<comment_id>[0-9]+)/$', views.comment_detail, name='comment_detail'),
    url(r'^stat/$', views.stat, name='statistic'),
    url(r'^stat/(?P<region_id>[0-9]+)/$', views.stat_region, name='statistic'),
    path('ajax_load_cities/', views.load_cities, name='ajax_load_cities'),
]
