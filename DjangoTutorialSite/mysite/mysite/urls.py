from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import IndexView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^polls/', include('mysite.apps.polls.urls')),
    url(r'^notes/', include('mysite.apps.notes.urls')),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.view.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()
