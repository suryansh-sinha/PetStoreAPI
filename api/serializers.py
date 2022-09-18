from rest_framework import serializers
from .models import Pet

# Converts our model data to JSON object.

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        # fields = ['name', 'owner_name', 'age', 'type', 'gender']
        fields = '__all__'