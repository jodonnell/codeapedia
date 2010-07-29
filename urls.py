from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
                            (r'^$', 'codea.views.index'),
                            (r'^by_author$', 'codea.views.by_author'),
                            (r'^by_tag$', 'codea.views.by_tag'),
                            (r'^by_book$', 'codea.views.by_book'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
