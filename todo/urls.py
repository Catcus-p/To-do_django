from django.urls import path
from . import views, api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #  html
    path('', views.task_list),
     path('register/', views.register),
    path('login/', views.user_login),
    path('edit/<int:id>/', views.edit_task),
    path('delete/<int:id>/', views.delete_task),
    path('toggle/<int:id>/', views.toggle_complete),

    path('login/', views.user_login),
    path('logout/', views.user_logout),

    # JWT auth
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),


    path('api/tasks/', api.task_list),              # get all tasks
    path('api/tasks/add/', api.add_task),          # post create task
    path('api/tasks/<int:id>/', api.update_task),  # put update
    path('api/tasks/<int:id>/delete/', api.delete_task),  # delete task
]