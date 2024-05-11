from rest_framework import serializers
from django.contrib.auth.models import User
from backend.models import Heroes, HeroesAbilities, Bases, Expansions, Cards, Decks, Collections


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class HeroesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heroes
        fields = ['hero_id', 'hero_name', 'hero_description']


class HeroesAbilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeroesAbilities
        fields = ['hero_linked', 'hero_ability_id', 'hero_ability_name', 'hero_ability_description']


class BasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bases
        fields = ['base_id', 'base_name', 'base_description', 'base_hp']


class ExpansionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expansions
        fields = ['expansion_id', 'expansion_name', 'expansion_lore']


class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ['card_id', 'card_name', 'card_lore', 'card_power', 'card_hp', 'is_legendary']


class DecksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decks
        fields = ['cards', 'hero', 'base', 'deck_id', 'deck_name']


class CollectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collections
        fields = ['collection_id', 'card', 'decks', 'user']
