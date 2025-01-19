from django.urls import path
from rest_framework.routers import DefaultRouter
from service.views.service import ServiceView
from service.views.company import CompanyView


router = DefaultRouter()

router.register(r"service", ServiceView, basename="service")
router.register(r"company", CompanyView, basename="company")


urlpatterns = router.urls