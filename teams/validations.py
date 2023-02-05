from teams.exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError,
)


def validate_team_titles(number: int):
    if number < 0:
        raise NegativeTitlesError('titles cannot be negative')


def validate_amount_titles(number: int, year: int):
    cup_times = (2022 - year) / 4
    if cup_times + 1 < number or cup_times == 0:
        raise ImpossibleTitlesError('impossible to have more titles than disputed cups')


def validate_year(number: int):
    if not number % 4 == 0:
        raise InvalidYearCupError('there was no world cup this year')


def validate_first_year(number: int):
    if number < 1930:
        raise InvalidYearCupError('there was no world cup this year')
