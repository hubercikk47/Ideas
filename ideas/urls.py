from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .chat.consumers import ChatConsumer

urlpatterns = [
    path('idea/', views.idea, name='idea'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='idea'), name='logout'),
    path('create_post/', views.make_post, name='post'),
    path('create_comm/', views.make_comment, name='comm'),
    path('idea/<int:idea_id>/', views.detail, name='detail_view'),
    path('ws/chat/<room_name>/', ChatConsumer.as_asgi())
]
