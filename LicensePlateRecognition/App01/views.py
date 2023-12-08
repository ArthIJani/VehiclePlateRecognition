from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from django.views.decorators.csrf import csrf_protect




@csrf_protect
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})



from .forms import WebcamVideoForm

def webcam_view(request):
    if request.method == 'POST':
        form = WebcamVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the video recording to the database
            return redirect('webcam_view')  # Redirect to the same page after submission
    else:
        form = WebcamVideoForm()

    return render(request, 'webcam.html', {'form': form})



