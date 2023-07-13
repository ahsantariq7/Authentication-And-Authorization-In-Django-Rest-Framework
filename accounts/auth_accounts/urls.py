from django.urls import path,include
from .views import SignInView,UserListView,GoogleLogin


urlpatterns = [
    path('login/',SignInView.as_view()),
    path('users/',UserListView.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('google/', GoogleLogin.as_view(), name='google_login')
]