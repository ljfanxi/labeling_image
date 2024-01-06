from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
import os
from django.conf import settings
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_image')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload/upload_image.html', {'form': form})


def display_image(request):
    # Specify the directory path
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')  # Adjust the path as needed

    # Get the list of file paths (images) in the specified directory
    image_paths = [file for file in os.listdir(upload_dir) if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    # Create a list of dictionaries containing information about each image
    images = [{'file_name': file, 'url': os.path.join(settings.MEDIA_URL, 'uploads', file)} for file in image_paths]

    # Pass the list of images to the template
    return render(request, 'image_upload/display_image.html', {'images': images})
