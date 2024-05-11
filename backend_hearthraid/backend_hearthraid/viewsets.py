from rest_framework import viewsets
from serializers import (UserSerializer, HeroesSerializer, HeroesAbilitiesSerializer,
                         BasesSerializer, ExpansionsSerializer, CardsSerializer, DecksSerializer,
                         CollectionsSerializer)
from django.contrib.auth.models import User
from backend.models import Heroes, HeroesAbilities, Bases, Expansions, Cards, Decks, Collections


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HeroesViewSet(viewsets.ModelViewSet):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer


class HeroesAbilitiesViewSet(viewsets.ModelViewSet):
    queryset = HeroesAbilities.objects.all()
    serializer_class = HeroesAbilitiesSerializer


class BasesViewSet(viewsets.ModelViewSet):
    queryset = Bases.objects.all()
    serializer_class = BasesSerializer


class ExpansionsViewSet(viewsets.ModelViewSet):
    queryset = Expansions.objects.all()
    serializer_class = ExpansionsSerializer


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Decks.objects.all()
    serializer_class = DecksSerializer


class CollectionsViewSet(viewsets.ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
