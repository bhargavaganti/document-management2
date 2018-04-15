from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name', 'org_role', 'last_login', 'password')
        read_only_fields = ('last_login',)
        extra_kwargs = {'password': {'write_only': True}}
        
        lookup_value = 'user_id'
        
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            org_role = validated_data['org_role'],
            )
        # TO DO: move password serialization to a dedicated serializer
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # Does not include the password in the scope; password to be changed via separate process
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != 'password':
                setattr(instance, attr, value)
        instance.save()
        return instance