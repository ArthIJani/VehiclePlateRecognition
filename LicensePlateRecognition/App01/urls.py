from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('references/', TemplateView.as_view(template_name='references.html'), name='references'),
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('webcam/', views.webcam_view, name='webcam_view'),
    #path('upload-webcam-video/', views.WebcamVideoUploadView.as_view(), name='upload-webcam-video'),
]

