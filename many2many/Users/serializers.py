from rest_framework import serializers
from .models import User, UserAddress



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'home', 'address', 'city', 'state', 'pincode']



class UserSerializer(serializers.ModelSerializer):
    addresses = UserAddressSerializer(many=True, required = False)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile', 'addresses']

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        user = User.objects.create(**validated_data)

        for address_data in addresses_data:
            address, created = UserAddress.objects.get_or_create(**address_data)
            user.addresses.add(address)

        return user
    
    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.save()

        if addresses_data:
            instance.addresses.clear()
            for address_data in addresses_data:
                address, created = UserAddress.objects.get_or_create(**address_data)
                instance.addresses.add(address)

        return instance