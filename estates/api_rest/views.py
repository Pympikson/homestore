import django_filters
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from api_rest.serializers import RealtorSerializer, ListingSerializers, ContactSerializer
from realtors.models import Realtor
from listings.models import Listing
from contacts.models import Contact
from rest_framework.decorators import action
from rest_framework.response import Response


class RealtorsViewSet(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class ListingsViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["price", "bedrooms", "bathrooms"]

    # serializer_class = ListingSerializers

    def get_queryset(self):
        qs = self.queryset
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city=city)
        return qs

    def get_serializer_class(self):
        if self.action == "update_realtor_info":
            return RealtorSerializer
        else:
            return ListingSerializers

    @action(methods=['GET'], detail=False)
    def moscow_flats(self, request, *args, **kwargs):
        qs = self.queryset
        qs = qs.filter(Q(city__icontains="Москва") | Q(city__icontains="Moscow"))
        serializer = ListingSerializers(qs, many=True)
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def update_realtor_info(self, request, *args, **kwargs):
        instance = self.get_object().realtor
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
