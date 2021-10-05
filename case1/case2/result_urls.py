from django.contrib import admin
from django.urls import path

from . import result_views, views

urlpatterns = [
   path('resultdetails/',result_views.resultdetails,name='resultdetails'),
   path('results/',result_views.results,name='results'),
   path('add_subject/',result_views.add_subject,name='add_subject'),
   path('edit_subject/<str:k_id>/',result_views.edit_subject,name='edit_subject'),
    path('search_result/',result_views.search_result,name='search_result'),
]
