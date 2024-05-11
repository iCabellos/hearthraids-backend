from rest_framework import routers
from viewsets import (UserViewSet, HeroesViewSet, HeroesAbilitiesViewSet, BasesViewSet, ExpansionsViewSet,
                      CardsViewSet, DecksViewSet, CollectionsViewSet)


def routers_main() -> routers:
    router = routers.DefaultRouter()
    router.register(r'users', UserViewSet)
    router.register(r'heroes', HeroesViewSet)
    router.register(r'abilities', HeroesAbilitiesViewSet)
    router.register(r'bases', BasesViewSet)
    router.register(r'expansions', ExpansionsViewSet)
    router.register(r'cards', CardsViewSet)
    router.register(r'decks', DecksViewSet)
    router.register(r'collections', CollectionsViewSet)

    return router
