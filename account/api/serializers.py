import email
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    user_name = serializers.CharField(max_length=40, min_length=3)
    password = serializers.CharField(max_length=68, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filter_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled, contact an Admin')

        # return {
        #     'email': user.email,
        #     'username': user.user_name,
        # }
        return super().validate(attrs)