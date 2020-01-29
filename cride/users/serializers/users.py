from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token 

from cride.users.models import User, Profile

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User 
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )

class ProfileModelSerializer(serializers.ModelSerializer):

    user = UserModelSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        profile = Profile(user=user)
        return profile        
    '''
     def valiate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation'] 

        if not password == password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        return data  
    '''

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        profile = Profile(user=user)
        profile.save()
        return profile 




class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        print("entro validate")
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data


    def create(self, data):
        print("entro create")
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


