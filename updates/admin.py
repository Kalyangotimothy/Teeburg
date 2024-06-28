from django.contrib import admin
from .models import Event, NurseryUpdate, PrimaryUpdate, StaffUpdate, GalleryImage

# Register your models here.
admin.site.register(Event)
admin.site.register(NurseryUpdate)
admin.site.register(PrimaryUpdate)
admin.site.register(StaffUpdate)
admin.site.register(GalleryImage)
