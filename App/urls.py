from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test,name='test'),
    path('test1',views.test1,name='test1'),
    path('calc',views.calc,name='calc'),
    path('final',views.final,name='final'),
    path('adminside',views.finaladmin,name='adminside'),
    path('userside',views.finaluser,name='userside')
]