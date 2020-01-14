from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Room

# convert python <-> json object


class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Room
        fields = ("name", "price", "instant_book", "user")
