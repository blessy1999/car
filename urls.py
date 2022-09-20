from.import views
from django.urls import path

urlpatterns = [
    
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration.html'),
    path('login/',views.login,name='login.html'),
    path('base/',views.login,name='base.html')
]