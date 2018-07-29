from rest_framework import serializers
from . import models
from nomad_coders.users import serializers as user_serializers
from nomad_coders.images import serializers as image_serializers



class NotificatinoSerializer(serializers.ModelSerializer):

    creator = user_serializers.ListUserSerializer()
    image = image_serializers.SmallImageSerializer()
    class Meta:
        model = models.Notification
        fields = '__all__'