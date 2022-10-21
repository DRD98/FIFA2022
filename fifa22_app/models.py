from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# from fifa2022 import settings 


class Event(models.Model):
    
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    # start_date = models.DateField(max_length=10, null = True)
    # start_date = models.DateField(settings.DATE_INPUT_FORMAT, null = True)
    start_date = models.DateField(null=True)
    # start_date = models.DateTimeField(settings.DATE_INPUT_FORMAT, null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=1000)
    venue = models.CharField(max_length=100)
    status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_event_table'


class Teams(models.Model):

    team_id = models.AutoField(primary_key = True)
    group = models.CharField(max_length = 1) 
    name = models.CharField(max_length = 100)
    coach = models.CharField(max_length = 100)
    status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_team_table'


class Fixture(models.Model):

    # Event_id = models.ForeignKey()
    event_id = models.IntegerField(default = '1', editable = False)
    match_id = models.AutoField(primary_key = True)
    start_time = models.DateTimeField()
    # Team_A = models.ForeignKey(Team, on_delete = models.PROTECT)
    # Team_B = models.ForeignKey(Team, on_delete = models.PROTECT)
    Team_A = models.CharField(max_length = 100)
    Team_B = models.CharField(max_length = 100)
    Venue = models.CharField(max_length = 100)
    # Result_id = models.ForeignKey()
    Result_id = models.CharField(max_length = 100, null = True)

    class Meta:
        db_table = 'fifa_fixture_table'


class Questions(models.Model):

    TEAM = 'T'
    PLAYER = 'P'
    GENERAL = 'G'
    question_type_choices = [
        (TEAM, 'Team'),
        (PLAYER, 'Player'),
        (GENERAL, 'General'),
    ]
    Q_id = models.AutoField(primary_key = True)
    # match_id = models.IntegerField()
    question = models.CharField(max_length = 100)
    op_1 = models.CharField(max_length = 100, null = True)
    op_2 = models.CharField(max_length = 100, null = True)
    op_3 = models.CharField(max_length = 100, null = True)
    op_4 = models.CharField(max_length = 100, null = True)
    q_type = models.CharField(
        max_length = 1,
        choices = question_type_choices,
        default = GENERAL,
    )

    class Meta:
        db_table = 'fifa_question_table'
