from django.urls.conf import include, path
from rest_framework import routers
from .views import ActionViewSet, MovieViewSet, ComedyViewSet

router = routers.SimpleRouter()
router.register('all', MovieViewSet)
router.register('action', ActionViewSet)
router.register('comedy', ComedyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
