from django.conf.urls import url
from .views import ListVideo
from . import views
urlpatterns = [
    url(r'^videos/', ListVideo.as_view(), name='lista-video'),
    url(r'^videos-cbo/', views.test , name='lista-video'),
]