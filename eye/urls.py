from django.urls import path

from .views import EventView,SessionView


urlpatterns = [
    path('event/', EventView.as_view(), name='Events'),
    path('session/', SessionView.as_view(), name='session' ),
    
]