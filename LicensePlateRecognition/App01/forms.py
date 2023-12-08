from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']



from .models import WebcamVideo

class WebcamVideoForm(forms.ModelForm):
    class Meta:
        model = WebcamVideo
        fields = ('title', 'video',)