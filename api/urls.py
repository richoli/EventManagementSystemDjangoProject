from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'events', EventViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'supports', SupportViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'registrations', RegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
