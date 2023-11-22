from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.core.mail import send_mail
import requests
from bs4 import BeautifulSoup

# Third party packages
from .serializers import SendEmailSerializer, CreateMatchSerializer
from .models import CreateNewMatch, SendMessageToEmail
from football.settings import EMAIL_HOST_USER


def schedule():
    url = "https://www.goal.com/en/live-scores"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    matches = soup.find_all("div", id="__next")
    print(matches)
    for match in matches:
        home_team = match.find("div", class_="team-home")
        away_team = match.find("div", class_="team-away")
        score = match.find("div", class_="match-info")

        print(f"{home_team} vs {away_team}: {score}")


class GameScheduleView(ListAPIView):
    queryset = CreateNewMatch.objects.all()
    serializer_class = CreateMatchSerializer


Email = str


class Email_Sender(APIView):
    queryset = SendMessageToEmail
    serializer_class = SendEmailSerializer

    def post(self, request):
        global Email
        serializer = SendEmailSerializer(data=request.data)
        response = SendEmailSerializer(data=request.data.get('email'))
        Email = response.initial_data
        to_mail = [Email]
        send_mail('New game',
                  'Don\'t forget to watch game! Click the link to watch the game: https://youtu.be/iS6dII37CwM?si=Efyf0FTo7zpwTMWq',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        print(f'Message sent to {Email}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
