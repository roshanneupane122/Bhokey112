from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('listings/', views.listings, name='listings'),
    path('post/', views.post_food, name='post_food'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('pickup/<int:pk>/', views.pickup_view, name='pickup_view'),

   
 
   
]

