from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import MyUser
from .serializers import LoginSerializer

# Create your views here.


class SignInView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({"error": "Invalid email or password"}, status=401)

        token = AccessToken.for_user(user)

        return Response({"access_token": str(token)})

    serializer_class = LoginSerializer


class UserListView(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            return MyUser.objects.filter(id=self.request.user.id)


class GoogleLogin(
    SocialLoginView
):  # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
