from rest_framework import serializers

from realtors.models import Realtor
from listings.models import Listing
from contacts.models import Contact


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = (
            "name",
            "photo",
            "description",
            "phone",
            "email",
            "is_mvp",
            "hire_date",
        )

    def validate(self, attrs):
        phone = attrs["phone"]
        list_symbols = list(phone)
        if list_symbols[0] != "7" and list_symbols[0] != "8":
            raise serializers.ValidationError(
                {"phone": "Введите номер телефона, принадлежащий российскому оператору"}
            )
        if len(list_symbols) != 11:
            raise serializers.ValidationError(
                {"phone": "Номер телефона должен содержать 11 символов"}
            )

        return attrs


class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "listing",
            "listing_id",
            "name",
            "email",
            "phone",
            "message",
            "contact_date",
            "user_id",
        )
