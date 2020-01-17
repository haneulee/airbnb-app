from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room

# convert python <-> json object


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)
