from django.shortcuts import render, redirect
from .models import Photo, Video, Audio, Text


# Create your views here.
def change_language(request):
    language = request.GET.get('language', 'kz')  # Получаем выбранный язык
    print("Language: ", language)
    request.session['language'] = language  # Сохраняем выбранный язык в сессии
    return redirect('main')

def text_view(request, key):
    language = request.GET.get('language', 'kz')  # Получаем выбранный язык, по умолчанию 'en'
    print("Language_text: ", language)
    
    try:
        # В зависимости от выбранного языка выбираем соответствующее поле
        if language == 'kz':
            text = Text.objects.get(key=key).content_kz
        elif language == 'ru':
            text = Text.objects.get(key=key).content_ru
        else:
            # Если язык не указан или неизвестен, используем английский по умолчанию
            text = Text.objects.get(key=key).content_kz
    except Text.DoesNotExist:
        text = None
        
    return render(request, 'main.html', {'text': text})

def main(request):
    latest_photos = Photo.objects.order_by('-id')[:10]
    latest_audios = Audio.objects.order_by('-id')[:4]
    latest_videos = Video.objects.order_by('-id')[:3]
    return render(request, 'main.html', {'latest_photos': latest_photos, 'latest_audios': latest_audios, 'latest_videos': latest_videos})


def photo_view(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photos})

def video_view(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def audio_view(request):
    audios = Audio.objects.all()
    return render(request, 'audios.html', {'audios': audios})

def photos_html_view(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photos})

def suhbat_html_view(request):
    videos = Video.objects.all()
    audios = Audio.objects.all()
    return render(request, 'suhbat.html', {'videos': videos, 'audios': audios})