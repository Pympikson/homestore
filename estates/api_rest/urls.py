from rest_framework import routers

from api_rest.views import (
    RealtorsViewSet,
    ContactsViewSet,
    ListingsViewSet,
)

app_name = "api"

router = routers.DefaultRouter()
router.register(r"realtors", RealtorsViewSet)
router.register(r"contacts", ContactsViewSet)
router.register(r"listings", ListingsViewSet)
urlpatterns = [
]

urlpatterns += router.urls