from django.urls import path
from .views import NotificationListView  # To be created

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
]