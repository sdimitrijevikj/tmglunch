from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'website.views.index', name='home'),
    url(r'^vote/', 'website.views.vote', name='vote'),
    url(r'^upload/', 'website.views.upload_data', name='upload'),
]

