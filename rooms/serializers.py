from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room

# convert python <-> json object


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ("modified",)

    read_only_fields = ("user", "id", "created", "updated")

    def validate(self, data):
        # 처음 room을 생성할 때만 체크하도록 변경, instance가 있으면 이미 생성된 room
        # update (self.instance.check_in > default 값)
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            # create
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError(
                "Not enough time between changes")
        return data

    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

    def create(self, validated_data):
        request = self.context.get("request")
        room = Room.objects.create(**validated_data, user=request.user)
        return room
