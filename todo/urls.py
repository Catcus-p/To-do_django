from django.urls import path
from . import views
from . import api

urlpatterns = [
    # WEB
    path('', views.task_list),
    path('delete/<int:id>/', views.delete_task),
    path('toggle/<int:id>/', views.toggle_complete),

    # API
    path('api/tasks/', api.api_task_list),
    path('api/add/', api.api_add_task),
    path('api/toggle/<int:id>/', api.api_toggle_task),
    path('api/calculate/', api.api_calculate_completed),
]