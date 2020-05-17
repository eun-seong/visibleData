import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

from django.conf import settings
from django.urls import path
from .models import DataImage, FileUpload

matplotlib.use('Agg')
matplotlib.style.use('ggplot')
 
def Visualizing():
    file_list = os.listdir(settings.MEDIA_ROOT)

    with open(settings.MEDIA_ROOT+file_list[0], mode='rb') as csv_file:
        file_db = FileUpload.objects.all().order_by('-time')
        file_directory='img/'+file_db[0].title+'.jpg'

        reader = pd.read_csv(csv_file)
        fig = sns.pairplot(reader, hue='Species')
        fig.savefig(settings.MEDIA_ROOT+file_directory)

        img = DataImage(path=file_directory, title=file_db[0].title)
        img.save()


