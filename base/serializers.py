#When you have data from different models, you can create a file for serializers and store all serializers.py files in the folder
from rest_framework.serializers import ModelSerializer
from .models import UInfo

class UInfoSerializer(ModelSerializer):
    class Meta:
        model = UInfo
        fields = '__all__' #serializes every attribute (alternatively could serialize specific like -> ("one", "two", "etc."))
        