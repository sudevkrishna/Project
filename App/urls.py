from django.urls import path,include
from . views import views
urlpatterns = [
    path('test',views.test,name='test')
]