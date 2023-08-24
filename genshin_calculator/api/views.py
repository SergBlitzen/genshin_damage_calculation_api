from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from api.serializers import CharacterSerializer
from data.models import Character, Weapon


class CharacterViewSet(viewsets.ModelViewSet):
    """
    Viewset for character data.
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class WeaponViewSet(viewsets.ModelViewSet):
    """
    Viewset for weapon data.
    """

    queryset = Weapon.objects.all()
