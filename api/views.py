from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PetSerializer
from .models import Pet
from api import serializers

# To get all the pet objects in our database.
@api_view(["GET"])
def petList(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

# To get a detailed view of a single pet object in our database.
@api_view(["GET"])
def petDetails(request, pk):
    pet = Pet.objects.get(id=pk)
    serializer = PetSerializer(pet)
    return Response(serializer.data)

# To add a new pet to the database.
@api_view(["POST"])
def addPet(request):
    pet = request.data
    serializer = PetSerializer(data=pet)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# To update a pet object in our database.
@api_view(["POST"])
def updatePet(request, pk):
    pet = Pet.objects.get(id=pk)
    # We are updating the pet instance here with the data from the request.
    serializer = PetSerializer(instance=pet, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# To update a pet object in our database.
@api_view(["DELETE"])
def deletePet(request, pk):
    pet = Pet.objects.get(id=pk)
    pet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)