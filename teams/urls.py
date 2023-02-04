from django.urls import path
from .views import TeamView, TeamDetailsView

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:team_id>/', TeamDetailsView.as_view())
]