from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict
from teams.validations import (
    validate_team_titles,
    validate_year,
    validate_amount_titles,
    validate_first_year,
)
from teams.exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError
)


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        n_titles = request.data["titles"]
        first_year = int(request.data["first_cup"][0:4])

        try:
            validation_one = validate_team_titles(n_titles)
        except NegativeTitlesError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        try:
            validation_two = validate_first_year(first_year)
        except InvalidYearCupError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        try:
            first_cup_difference = 2022 - first_year
            validation_three = validate_year(first_cup_difference)
        except InvalidYearCupError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        try:
            validation_four = validate_amount_titles(n_titles, first_year)
        except ImpossibleTitlesError as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]

        return Response(teams_dict)


class TeamDetailsView(APIView):
    def get(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)
        
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist as err:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
