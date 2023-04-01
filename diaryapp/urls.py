from django.urls import path
from . import views 


urlpatterns=[
    path('',views.index, name='index'),
    path('story/<str:id>', views.story, name='story'),
    path('complete/<str:id>', views.complete, name='complete'),
    path('delete/<str:id>', views.deletediary, name='delete'),
    path('update/<str:id>', views.updatediary, name='update' ),
    path('about/', views.about, name='about'),
     
    
    
]