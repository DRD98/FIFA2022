from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# from fifa2022 import settings 


class Event(models.Model):
    
    event_id = models.AutoField(primary_key = True)
    event_name = models.CharField(max_length = 100)
    # start_date = models.DateField(max_length=10, null = True)
    # start_date = models.DateField(settings.DATE_INPUT_FORMAT, null = True)
    start_date = models.DateField(null = True)
    # start_date = models.DateTimeField(settings.DATE_INPUT_FORMAT, null=True)
    end_date = models.DateField(null = True)
    description = models.CharField(max_length = 1000)
    venue = models.CharField(max_length = 100)
    e_status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_event_table'


class Teams(models.Model):

    team_id = models.AutoField(primary_key = True)
    group = models.CharField(max_length = 1) 
    name = models.CharField(max_length = 100)
    coach = models.CharField(max_length = 100)
    t_status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_team_table'


class Fixture(models.Model):

    # Event_id = models.ForeignKey()
    event_id = models.IntegerField(default = '1', editable = False)
    match_id = models.AutoField(primary_key = True)
    start_time = models.DateTimeField()
    # Team_A = models.ForeignKey(Team, on_delete = models.PROTECT)
    # Team_B = models.ForeignKey(Team, on_delete = models.PROTECT)
    team_A = models.CharField(max_length = 100)
    team_B = models.CharField(max_length = 100)
    venue = models.CharField(max_length = 100)
    # Result_id = models.ForeignKey()
    result_id = models.CharField(max_length = 100, default = 'NA', null = True)
    f_status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_fixture_table'


class UserQuestions(models.Model):

    Q_id = models.AutoField(primary_key = True)
    match_id = models.IntegerField(null = True)
    question = models.CharField(max_length = 1000)
    op1 = models.CharField(max_length = 100, null = True)
    op2 = models.CharField(max_length = 100, null = True)
    op3 = models.CharField(max_length = 100, null = True)
    # op4 = models.CharField(max_length = 100, null = True)
    point = models.IntegerField(null = True)
    q_type = models.CharField(max_length = 8, null = True)
    q_status = models.BooleanField(default = '1', editable = False)

    class Meta:
        db_table = 'fifa_quizquestions_table'