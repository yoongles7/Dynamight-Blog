from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",   
            "first_name",
            "last_name", 
            "password",
            "password2" 
        ]
        extra_kwargs = {"password": {"write_only": True}}
        
    # Validate and confirm password while registration
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        
        if password != password2:
            raise serializers.ValidationError("passwords don't match!")
        return attrs
    
    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            email=validate_data["email"],
            username=validate_data["username"],
            password=validate_data["password"],
            first_name=validate_data.get("first_name", ""),     # get() method for optional feilds
            last_name=validate_data.get("last_name", ""),
        )
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    
    class Meta:
        model = CustomUser
        fields = ["email", "password"]

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        self.token = attrs.get("refresh")
        return attrs
    
    def save(self, **kwards):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")

class UserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]