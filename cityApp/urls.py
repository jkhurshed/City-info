from django.urls import path, include
from rest_framework import routers

from cityApp.views import (PlaceViewSet, PlacesByCategory, PlacesByCity, 
    PlaceByAdressSearching, PlaceByTitleSearching)

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, 'places')
# router.register(r'by-category', PlacesByCategory, 'by_category')

urlpatterns = [
    path('', include(router.urls)),

    path('places/category/<int:category_id>', PlacesByCategory.as_view()),
    path('places/city/<int:city_id>', PlacesByCity.as_view()),
    
    path('places/adress/', PlaceByAdressSearching.as_view()),
    path('places/title/', PlaceByTitleSearching.as_view()),
]
