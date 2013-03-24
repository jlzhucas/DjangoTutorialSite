from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^polls/', include('mysite.apps.polls.urls')),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
