from rest_framework import serializers
from places.models import Place, PlaceComment
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class PlaceSerializer (serializers. ModelSerializer):
    
    class Meta:
        model = Place
        fields = ('name', 'description', 'place_image')

class UserSerializer (serializers. ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'profile_image')

class CommentSerializer (serializers. ModelSerializer):
    user = UserSerializer()
    place = PlaceSerializer()

    class Meta:
        model = PlaceComment
        fields = ('user', 'place', 'comment', 'stars_given', 'created_at')

class LoginSerializer (serializers.Serializer):
    password = serializers.CharField(max_length=50, write_only=True)
    username = serializers.CharField(max_length=255)
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError({"status": False, "message": "user not found"})
        return user
    
    def to_representation (self, user):
        refresh = RefreshToken.for_user(user)
        data = {
            "email": user.email,
            'username': user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data