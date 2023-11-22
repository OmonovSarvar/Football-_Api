from django.urls import path

from .views import Email_Sender, GameScheduleView, schedule

urlpatterns = [
    path('remind', Email_Sender.as_view(), name='email'),
    path('', GameScheduleView.as_view(), name='match'),
    path('test', schedule, name='schedule')
]
