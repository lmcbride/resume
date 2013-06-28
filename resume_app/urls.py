from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Views:
    url(r'^$', 'resume_app.views.home', name='home'),
    url(r'^test$', 'resume_app.views.test', name='test'),
    url(r'^admin/', include(admin.site.urls)),
    )