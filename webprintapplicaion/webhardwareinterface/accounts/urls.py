from django.urls import path,include
from accounts import views 
urlpatterns = [
 	path(r'signup',views.signup,name="signup"),
    path(r'', include('django.contrib.auth.urls')),
    path(r'',views.signup,name="signup")
]

