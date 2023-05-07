from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.generics import ListAPIView

from cityApp.models import Place, Category
from cityApp.serializers import PlaceSerializer, CategorySerializer

class PlaceViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class PlacesByCategory(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Place.objects.filter(category_id=category_id)
        return queryset

class PlacesByCity(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        queryset = Place.objects.filter(city_id=city_id)
        return queryset

class PlaceByAdressSearching(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(adress__icontains=search_query)
        return queryset

class PlaceByTitleSearching(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset
