from django.shortcuts import render
from .models import Event, NurseryUpdate, PrimaryUpdate, StaffUpdate, GalleryImage
import datetime
# Create your views here.

def index(request):
    return render(request, "updates/index.html", {
    })


def gallery(request):
    return render(request, "updates/gallery.html", {
    })
    


def update_list(request):
    events = Event.objects.all()
    nursery_updates = NurseryUpdate.objects.all()
    primary_updates = PrimaryUpdate.objects.all()
    staff_updates = StaffUpdate.objects.all()

    context = {
        'events': events,
        'nursery_updates': nursery_updates,
        'primary_updates': primary_updates,
        'staff_updates': staff_updates,
    }
    return render(request, 'updates/update_list.html', context)


def gallery(request):
    images = GalleryImage.objects.all()
    context = {
        'images': images
    }
    return render(request, 'updates/gallery.html', context)