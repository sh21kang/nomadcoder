from rest_framework.views import APIView
from rest_framework.response import Response
from . import models,serializers
from rest_framework import status


class Notification(APIView):
    

    
    def get(self, request, format=None):
        user =  request.user

        notification =  models.Notification.objects.filter(to=user)

        serializer = serializers.NotificatinoSerializer(notification, many=True)

        return Response(data= serializer.data, status=status.HTTP_200_OK)

        



def create_notification(creator, to,notification_type, image=None,comment=None ):
    notification = models.Notification.objects.create(
        creator = creator,
        to = to,
        notification_type = notification_type,
        image = image,
        comment= comment
    )
    notification.save()