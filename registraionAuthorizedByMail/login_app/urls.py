
from django.urls import include, path 
from login_app import views
app_name = "login_app"
urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login_attemp, name = "login_attemp"),
    path('register/',views.rigister_attemp, name="rigister_attemp"),
    path('token/',views.token_send,name='token_send'),
     path('success/',views.success,name='success'),
]
