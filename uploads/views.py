from django.shortcuts import render, redirect
import csv

from .modules import Visualizing
from .models import DataImage
from .forms import UploadForm

def index(request):
    return render(request, 'uploads/index.html', {})

def fileVisualize(request):
    Visualizing()   
    dataImage = DataImage.objects.all().order_by('-time')[0]
    print(dataImage.title)
    print(dataImage.path)
    return render(request, 'uploads/visualize.html', {
        'dataImage' : dataImage
    })

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileVisualize')
    else:
        form = UploadForm()
    return render(request, 'uploads/upload.html', {
        'form':form
    })
