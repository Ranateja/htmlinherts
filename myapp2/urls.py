from django.urls import path
from myapp2 import views
app_name='myapp2'


urlpatterns =[
    path('child/',views.child,name='child'),
]