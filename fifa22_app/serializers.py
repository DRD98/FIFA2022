from .models import Event, Teams, Fixture, UserQuestions
# from django.contrib.auth.hashers import make_password
from rest_framework import serializers


# used in the creation of Event Table
class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        # fields = ('event_name', 'start_date', 'description', 'venue', 'status')
        # fields = '__all__'
        model = Event
        fields = ('event_name', 'start_date', 'end_date', 'description', 'venue', 'status')
        

# used in the creation of Team Table
class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Teams
        fields = ('team_id', 'group', 'name', 'coach', 'status')


#used in the creation of Fixture Table
class FixtureSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Fixture
        fields = ('start_time', 'team_A', 'team_B', 'venue', )


class ViewFixtureSerializer(FixtureSerializer):
    
    class Meta:

        model = Fixture
        fields = ('match_id', 'start_time', 'team_A', 'team_B', 'venue')


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = UserQuestions
        fields = ('match_id', 'question', 'op1', 'op2', 'op3', 'point', 'q_type' )
