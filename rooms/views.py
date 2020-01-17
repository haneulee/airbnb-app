from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


class RoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()[:5]
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # "name": "beautiful house",
        # "address": "seoul ",
        # "price": 5,
        # "beds": 5,
        # "lat": 5,
        # "lng": 5,
        # "bedrooms": 5,
        # "bathrooms": 5,
        # "check_in": "14:00",
        # "check_out": "16:00",
        # "instant_book": false


class RoomView(APIView):
    def get(self, request, pk):
        try:
            room = Room.objects.get(pk=pk)
            serializer = ReadRoomSerializer(room).data
            return Response(serializer)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        pass

    def delete(self, request):
        pass
