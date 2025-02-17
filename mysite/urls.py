from django.conf.urls import patterns, include, url
from bookstore import views
from django.contrib import admin
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('bookstore.url')),
    url(r'^password_change$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
     #Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    
)



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^/static/$','django.views.static.serve', kwargs=settings.STATIC_ROOT),
        url(r'^/media/$','django.views.static.serve', kwargs=settings.MEDIA_ROOT),
    )  

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                   
    
                            

    