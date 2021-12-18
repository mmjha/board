
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from board.serializers import PostSerializer

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """
        https://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer
        https://hoorooroob.tistory.com/entry/DRF-Validation
        cycle : is_valid -> initial_data -> validated_data -> errors
    """
    username = serializers.CharField(required=True, help_text='아이디')
    password = serializers.CharField(required=True, help_text='비밀번호')

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def is_valid(self, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def validate_username(self, username):
        """
            username validation
        """
        if username == 'admin':
            raise serializers.ValidationError('This ID:admin cannot be used')
        return username

    def validate_password(self, password):
        """
            password validation
        """
        return password

    def create(self, validated_data):
        """
            https://stackoverflow.com/questions/29746584/django-rest-framework-create-user-with-password/29748569
        """
        # return User.objects.create(**validated_data)
        print(validated_data)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
    # fields = '__all__'
        fields = (
            'id',
            'username',
            'first_name',
            'date_joined',
            'last_login',
            'is_staff',
            'is_active',
        )


class MyPostSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'post_set')
