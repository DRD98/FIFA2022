from .models import Event, Teams, Fixture
# from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('event_name', 'start_date', 'end_date', 'description', 'venue', 'status')
        # fields = ('event_name', 'start_date', 'description', 'venue', 'status')
        # fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Teams
        fields = ('team_id', 'group', 'name', 'coach', 'status')


class FixtureSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Fixture
        fields = ('start_time', 'Team_A', 'Team_B', 'Venue', )


class ViewFixtureSerializer(FixtureSerializer):
    
    class Meta:

        model = Fixture
        fields = ('match_id', 'start_time', 'Team_A', 'Team_B', 'Venue')
