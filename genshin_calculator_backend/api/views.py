from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

import api.utils as utils
from api.serializers import CharacterSerializer, WeaponSerializer
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
    serializer_class = WeaponSerializer


class CalculationAPIView(APIView):
    """
    Main calculation view.
    """

    def get(self, request):
        get_data = request.query_params
        try:
            character = Character.objects.get(
                short_name=get_data['character_name']
            )
        except Character.DoesNotExist as e:
            return Response(f"Invalid character name! Error: {e}")
        try:
            weapon = Weapon.objects.get(
                short_name=get_data['weapon_name']
            )
        except Weapon.DoesNotExist as e:
            return Response(f"Invalid weapon name! Error: {e}")

        response_data = utils.get_attributes(
            character,
            weapon,
            get_data
        )

        return Response(response_data)
