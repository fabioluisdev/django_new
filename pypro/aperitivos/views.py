from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivacao', 'vimeo_id': 688843510}
    return render(request, 'aperitivos/video.html', context={'video': video})
