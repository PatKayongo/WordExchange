from django.conf.urls import patterns, include, url
from django.contrib import admin
from translator import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordexchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/meta/languages/', views.language_list, name='language_list'),
    url(r'^api/meta/wordfunctions/', views.word_functions, name='word_functions'),
)
