from django.urls import path
from . import views #. means from this directory

urlpatterns = [
    path('', views.home, name="Blog-Home"),#default as no path added
    path('About/', views.About, name="Blog-About"),# appears after we add /About to the path
    # path('Contact/', views.contact, name="Blog-Contact"),
] 