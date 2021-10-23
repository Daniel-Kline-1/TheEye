from django.urls import path

from .views import (
    EventView,
    SessionView,
    CategoryView,
    TimeView
    )


urlpatterns = [
    path('event/', EventView.as_view(), name='Events'),
    path('session/', SessionView.as_view(), name='session' ),
    path('category/', CategoryView.as_view(), name='category'),
    path('time/', TimeView.as_view(), name='time'),

]