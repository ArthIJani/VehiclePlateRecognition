from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WebcamVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='webcam_videos/')
    created_at = models.DateTimeField(auto_now_add=True)