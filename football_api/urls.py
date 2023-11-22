from django.urls import path

from football_api.views import Email_Sender, GameScheduleView
urlpatterns = [
    path('remind/', Email_Sender.as_view(), name='email'),
    path('', GameScheduleView.as_view(), name='match'),
]
