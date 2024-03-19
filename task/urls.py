from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.init, name='init'),
    path('add_task/', views.save_task, name='save_task'),
    path('update_task/<int:id>', views.update_task, name='update_task')
]