from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict
from teams.exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
import ipdb
# Create your views here.


class TeamView(APIView):
    def post(self, request):
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        ipdb.set_trace()

        first_year = int(team_dict['first_cup'][0:4])
        first_cup_difference = 2022 - first_year
        cup_times = (2022 - first_year) / 4

        if not team_dict['titles'] > 0:
            return NegativeTitlesError({'error': 'titles cannot be negative'}, status.HTTP_400_BAD_REQUEST)
        
        if not first_cup_difference % 4 == 0 or first_year < 1930 :
            return InvalidYearCupError({'error': 'there was no world cup this year'}, status.HTTP_400_BAD_REQUEST)

        if cup_times + 1 < team_dict['titles']:
            return ImpossibleTitlesError({'error': 'impossible to have more titles than disputed cups'}, status.HTTP_400_BAD_REQUEST)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request):
        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]

        return Response(teams_dict)