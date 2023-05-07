from rest_framework import serializers

from cityApp.models import Category, Contact, City, Place

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"
    
    def to_representation(self, instance, *args, **kwargs):
        data = super(CitySerializer, self).to_representation(instance)
        return data["title"]
    
class ContactSerializer(serializers.ModelSerializer):

    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("phone", "additionalPhone", "work_routine", "email", "image", "custom_field")
    
    def get_custom_field(self, instance):
        return instance.place.title

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
    
    def to_representation(self, instance, *args, **kwargs):
        data = super(CategorySerializer, self).to_representation(instance)
        return data["title"]

class PlaceSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="contact.email")
    phone = serializers.CharField(source="contact.phone")
    additionalPhone = serializers.CharField(source="contact.additionalPhone")
    work_routine = serializers.CharField(source="contact.work_routine")
    image = serializers.CharField(source="contact.image")

    contact = ContactSerializer()
    category = CategorySerializer()
    city = CitySerializer()
    
    class Meta:
        model = Place
        fields = "__all__"
        