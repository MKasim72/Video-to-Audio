from django.shortcuts import render,HttpResponse

# Create your views here.
# views.py
from django.http import HttpResponse,HttpRequest
from moviepy.editor import VideoFileClip


def index(request):
    return render(request,'index.html')

def video_to_audio(request):
    if request.method == 'POST' and request.FILES.get('video_file'):
        video_file = request.FILES['video_file']
        try:
            # Ensure the uploaded file is a video file
            if video_file.content_type.startswith('video'):
                with VideoFileClip(video_file.temporary_file_path()) as video:
                    # Extract audio from the video
                    audio = video.audio
                    # Write the audio to a file
                    audio_file_path = 'output_audio.mp3'
                    audio.write_audiofile(audio_file_path)
                    # Return the audio file as response
                    with open(audio_file_path, 'rb') as f:
                        response = HttpResponse(f, content_type='audio/mpeg')
                        response['Content-Disposition'] = 'attachment; filename="output_audio.mp3"'
                        return response
            else:
                return HttpResponse('Please upload a valid video file', status=400)
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}', status=500)
    else:
        return HttpResponse('Please upload a video file', status=400)
