from rest_framework import serializers

from users.models import User


class UserSerialaizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



