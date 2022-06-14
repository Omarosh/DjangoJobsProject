from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'user_type', 'email', 'password', 'password_confirm', 'gender')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'user_type': {'required': True},
            'email': {'required': True},
            'password_confirm': {'required': True},
            # 'cv': {'required': False},
            'gender': {'required': True},
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            password=self.validated_data.get('password'),
            # cv=self.validated_data.get('cv'),
            gender=self.validated_data.get('gender'),

        )

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "Password Didn't Match"}
            )

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    # password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'user_type', 'email', 'password', 'address', 'history')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'user_type': {'required': True},
            # 'password_confirm': {'required': False},
            'email': {'required': True},
            'address': {'required': True},
            'history': {'required': True},
        }

        def save(self, **kwargs):
            user = User(
                username=self.validated_data.get('username'),
                email=self.validated_data.get('email'),
                password=self.validated_data.get('password'),
                address=self.validated_data.get('address'),
                history=self.validated_data.get('history'),
            )

            if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
                raise serializers.ValidationError(
                    {'detail': "Password Didn't Match"}
                )

            user.set_password(self.validated_data.get('password'))
            user.save()
            return user
