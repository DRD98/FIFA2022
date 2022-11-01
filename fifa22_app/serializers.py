from .models import Event, Teams, UserQuestions, temp#, Fixture
# from django.contrib.auth.hashers import make_password
from rest_framework import serializers


# used in the creation of Event Table
class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        # fields = ('event_name', 'start_date', 'description', 'venue', 'status')
        # fields = '__all__'
        model = Event
        fields = ('eventName', 'startDate', 'endDate', 'description', 'venue', 'eStatus')
        

# used in the creation of Team Table
class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Teams
        fields = ('teamId', 'group', 'name', 'coach', 'tStatus')


#used in the creation of Fixture Table
# class FixtureSerializer(serializers.ModelSerializer):
    
#     class Meta:

#         model = Fixture
#         fields = ('startTime', 'teamA', 'teamB', 'venue', )


# class ViewFixtureSerializer(FixtureSerializer):
    
#     class Meta:

#         model = Fixture
#         fields = ('matchId', 'startTime', 'teamA', 'teamB', 'venue')


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = UserQuestions
        fields = ('matchId', 'question', 'op1', 'op2', 'op3', 'point', 'qType' )


class TempSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = temp
        fields = ('question', 'grade' )
