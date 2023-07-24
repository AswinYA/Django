from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Serializers in Django REST Framework are responsible for converting objects into data types understandable
# by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to 
# be converted back into complex types, after first validating the incoming data.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


        
