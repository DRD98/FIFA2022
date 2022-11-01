from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# from fifa2022 import settings 


class Event(models.Model):
    
    eventId = models.AutoField(primary_key = True)
    eventName = models.CharField(max_length = 100)
    # start_date = models.DateField(max_length=10, null = True)
    # start_date = models.DateField(settings.DATE_INPUT_FORMAT, null = True)
    startDate = models.DateField(null = True)
    # start_date = models.DateTimeField(settings.DATE_INPUT_FORMAT, null=True)
    endDate = models.DateField(null = True)
    description = models.CharField(max_length = 1000)
    venue = models.CharField(max_length = 100)
    eStatus = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_event_table'


class Teams(models.Model):

    teamId = models.AutoField(primary_key = True)
    group = models.CharField(max_length = 2) 
    name = models.CharField(max_length = 100)
    coach = models.CharField(max_length = 100)
    tStatus = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_team_table'


class Fixture(models.Model):

    # Event_id = models.ForeignKey()
    eventId = models.IntegerField(default = '1', editable = False)
    matchId = models.AutoField(primary_key = True)
    # matchId = models.AutoField(primary_key = False)
    startTime = models.DateTimeField(null = True)
    teamA = models.ForeignKey(Teams, related_name = 'teamA', on_delete = models.PROTECT, null = True)
    teamB = models.ForeignKey(Teams, related_name = 'teamB', on_delete = models.PROTECT, null = True)
    # team_A = models.CharField(max_length = 100)
    # team_B = models.CharField(max_length = 100)
    venue = models.CharField(max_length = 100)
    # Result_id = models.ForeignKey()
    resultId = models.CharField(max_length = 100, default = 'NA', null = True)
    published = models.BooleanField(default = '1')
    fStatus = models.BooleanField(default = '1', editable = False)
    status = models.BooleanField(default = '1')

    class Meta:
        db_table = 'fifa_fixture_table'


class UserQuestions(models.Model):

    qId = models.AutoField(primary_key = True)
    matchId = models.IntegerField(null = True)
    question = models.CharField(max_length = 1000)
    op1 = models.CharField(max_length = 100, null = True)
    op2 = models.CharField(max_length = 100, null = True)
    op3 = models.CharField(max_length = 100, null = True)
    # op4 = models.CharField(max_length = 100, null = True)
    point = models.IntegerField(null = True)
    qType = models.CharField(max_length = 8, null = True)
    qStatus = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_quizquestions_table'

class temp (models.Model):

    tId = models.AutoField(primary_key = True)
    question = models.CharField(max_length = 10)
    grade = models.CharField(max_length = 2, null = True)
    point = models.IntegerField(default = '0')
    totpoints = models.IntegerField(default = '0')

    class Meta:
        db_table = 'aaaaaaq'
