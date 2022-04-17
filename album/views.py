from django.views.generic import ListView
from .models import Photo

class PhotoListView(ListView):
    model=Photo
    template_name="album/photo_list.html"
    content_object_name="photos"

