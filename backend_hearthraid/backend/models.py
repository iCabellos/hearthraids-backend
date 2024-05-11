from django.db import models
from django.contrib.auth.models import User


class Heroes(models.Model):
    hero_id = models.AutoField(primary_key=True)
    hero_name = models.CharField(max_length=128, blank=True, null=True)
    hero_description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{name}({id})".format(name=self.hero_name, id=self.hero_id)


class HeroesAbilities(models.Model):
    hero_linked = models.ForeignKey(
        Heroes,
        on_delete=models.CASCADE,
        verbose_name="Hero active ability",
    )
    hero_ability_id = models.AutoField(primary_key=True)
    hero_ability_name = models.CharField(max_length=128, blank=True, null=True)
    hero_ability_description = models.TextField(max_length=255, blank=True, null=True)

    def _do_hero_ability(self):
        pass

    def __str__(self):
        return "{name}({id}) - {hero_name}({hero_id})".format(
            name=self.hero_ability_name,
            id=self.hero_ability_id,
            hero_name=self.hero_linked.hero_name,
            hero_id=self.hero_linked.hero_id,
        )


class Bases(models.Model):
    base_id = models.AutoField(primary_key=True)
    base_name = models.CharField(max_length=128, blank=True, null=True)
    base_description = models.TextField(max_length=255, blank=True, null=True)
    base_hp = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{name}({id})".format(
            name=self.base_name,
            id=self.base_id,
        )


class Expansions(models.Model):
    expansion_id = models.AutoField(primary_key=True)
    expansion_name = models.CharField(max_length=128, blank=True, null=True)
    expansion_lore = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{name}({id})'.format(name=self.expansion_name, id=self.expansion_id)


class Cards(models.Model):
    expansion = models.ForeignKey(
        Expansions,
        on_delete=models.CASCADE,
        verbose_name="Expansion card",
        blank=True,
        null=True
    )
    card_id = models.AutoField(primary_key=True)
    card_name = models.CharField(max_length=128, blank=True, null=True)
    card_lore = models.TextField(max_length=255, blank=True, null=True)
    card_power = models.IntegerField(blank=True, null=True)
    card_hp = models.IntegerField(blank=True, null=True)
    is_legendary = models.BooleanField(default=False)

    def _do_card_ability(self):
        pass

    def __str__(self):
        if self.is_legendary:
            return '{name}({id}) - Legendary'.format(name=self.card_name, id=self.card_id)
        else:
            return '{name}({id})'.format(name=self.card_name, id=self.card_id)


class Decks(models.Model):
    cards = models.ManyToManyField(
        Cards,
        blank=True,
        null=True
    )
    hero = models.ForeignKey(
        Heroes,
        on_delete=models.CASCADE,
        verbose_name="Main Hero deck",
        blank=True,
        null=True
    )
    base = models.ForeignKey(
        Bases,
        on_delete=models.CASCADE,
        verbose_name="Main Base deck",
        blank=True,
        null=True
    )
    deck_id = models.AutoField(primary_key=True)
    deck_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return '{name}({id})'.format(name=self.deck_name, id=self.deck_id)


class Collections(models.Model):
    card = models.ManyToManyField(
        Cards,
        blank=True,
        null=True
    )
    decks = models.ManyToManyField(
        Decks,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User collection owner",
        blank=True,
        null=True
    )
    collection_id = models.AutoField(primary_key=True)

    def __str__(self):
        return '{collection_id} - {owner_name}'.format(collection_id=self.collection_id, owner_name=self.user)
