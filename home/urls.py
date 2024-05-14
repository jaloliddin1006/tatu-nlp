from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ner-technology/', views.ner_technology, name='ner_technology'),
    path('sinonim/', views.sinonim, name='sinonim'),
    path('short_name/', views.short_name, name='short_name'),
    path('sentence/', views.sentence, name='sentence'),
    path('add_name/', views.add_name, name='add_name'),
    path('antonim/', views.antonim, name='antonim'),
]