from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


# class UserSerializer(serializers.ModelSerializer):
#     password_confirm = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         # fields = ('username', 'user_type', 'email', 'password', 'password_confirm', 'gender')
#         fields = ('username', 'user_type', 'email', 'gender')
#         extra_kwargs = {
#             'password': {'write_only': True, 'required': True},
#             'username': {'required': True},
#             'user_type': {'required': True},
#             'email': {'required': True},
#             'password_confirm': {'required': True},
#             # 'cv': {'required': False},
#             'gender': {'required': True},
#         }
#
#     def save(self, **kwargs):
#         user = User(
#             username=self.validated_data.get('username'),
#             email=self.validated_data.get('email'),
#             password=self.validated_data.get('password'),
#             # cv=self.validated_data.get('cv'),
#             # tags
#             gender=self.validated_data.get('gender'),
#
#         )
#
#         if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
#             raise serializers.ValidationError(
#                 {'detail': "Password Didn't Match"}
#             )
#
#         user.set_password(self.validated_data.get('password'))
#         user.save()
#         return user
#

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id' ,'username', 'password', 'password_confirm', 'email', 'user_type', 'gender']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            # 'address': {'required': True},
            'gender': {'required': True},

        }

    def save(self,**kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            user_type = self.validated_data['user_type'],
            gender = self.validated_data['gender'],
            # cv
        )

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "Password Didn't Match"}
            )

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user





#
# class CompanySerializer(serializers.ModelSerializer):
#     password_confirm = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         # fields = ('username', 'user_type', 'email', 'password', 'address', 'history')
#
#         fields = ('username', 'user_type', 'email', 'gender', 'password_confirm')
#         extra_kwargs = {
#             'password': {'write_only': True, 'required': True},
#             'username': {'required': True},
#             'user_type': {'required': True},
#             # 'password_confirm': {'required': True},
#             'email': {'required': True},
#             'address': {'required': True},
#             'history': {'required': True},
#         }
#
#         def save(self, **kwargs):
#             user = User(
#                 username=self.validated_data.get('username'),
#                 email=self.validated_data.get('email'),
#                 password=self.validated_data.get('password'),
#                 address=self.validated_data.get('address'),
#                 history=self.validated_data.get('history'),
#             )
#
#             if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
#                 raise serializers.ValidationError(
#                     {'detail': "Password Didn't Match"}
#                 )
#
#             user.set_password(self.validated_data.get('password'))
#             user.save()
#             return user

#
class CompanySerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','password_confirm','email','user_type','gender']
        extra_kwargs= {
            'password':{'write_only':True},
            'email' : {'required':True},
            'address': {'required': True},
            'history': {'required': True},

        }
    def save(self,**kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            user_type = self.validated_data['user_type'],
            #address
            #history
        )


        if(self.validated_data['password'] != self.validated_data['password_confirm']):
          raise  serializers.ValidationError({'details':'passwords didnt match'})


        user.set_password(self.validated_data['password'])
        user.save()
        return user