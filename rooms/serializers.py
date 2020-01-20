from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room

# convert python <-> json object


class ReadRoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)


class WriteRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ("user", "modified", "created")

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
