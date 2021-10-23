from rest_framework import serializers

from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'id','session_id','category','name',
            'host','path','element','first_name',
            'last_name','timestamp',
        )