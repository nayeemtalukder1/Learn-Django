from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = ImageUpload.objects.all()
    return render(request, 'image_list.html', {'images': images})
