from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='store'),
    path('lapList/', views.lapList, name='lapList'),
    path('add_laptop/', views.add_laptop, name='add_laptop'),
    path('laptop_update/<str:pk>/', views.laptop_update, name='laptop_update'),
    path('delete_laptop/<str:pk>/', views.delete_laptop, name='delete_laptop'),
    path('laptop_detail/<str:laptop_id>/',views.laptop_detail, name='laptop_detail'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('view_images/', views.view_images, name='view_images'),
    path('edit_image/<int:pk>/', views.EditImageView.as_view(), name='edit_image'),
    path('delete_image/<int:pk>/', views.DeleteImageView.as_view(), name='delete_image'),
]
#
