from django.urls import path

from . import views

urlpatterns = [
    # ex: /webApp/1
    path('<int:lap_id>', views.lap_detail, name='detail'),
   
]