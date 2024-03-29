from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^events/$', views.Events.as_view()),
    url(r'^register/(?P<event_id>[0-9]+)$',
        views.Compireg.as_view()),
    url(r'^competitions/(?P<fb_id>[0-9]+)/$',
        views.UserCompetitions.as_view()),
]
