from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Photo, Reply


# Create your views here.
def index(request):
    photos = Photo.objects.all()
    output = ", ".join([photo.title for photo in photos])
    context = {"photos": photos}
    return render(request, "index.html", context)


def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, "detail.html", {"photo": photo})


def like(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    try:
        selected_reply = photo.reply_set.get(pk=request.POST["reply"])
    except (KeyError, Reply.DoesNotExist):
        return render(request, "detail.html", {"photo": photo, "error_message": "You didn't select a reply."})
    else:
        selected_reply.like += 1
        selected_reply.save()
        return HttpResponseRedirect(reverse("result", args=(photo.id,)))


def result(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'result.html', {"photo": photo})
