from django.urls import path
from . import views, api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.task_list),
    

    path('edit/<int:id>/', views.edit_task),
    path('delete/<int:id>/', views.delete_task),
    path('toggle/<int:id>/', views.toggle_complete),

    path('login/', views.user_login),
    path('logout/', views.user_logout),

    # API
    path('api/register/', api.register),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/tasks/', api.task_list),
    path('api/add/', api.add_task),
    path('api/update/<int:id>/', api.update_task),
    path('api/delete/<int:id>/', api.delete_task_api),
]