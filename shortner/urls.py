

from django.urls import path

from . import views


urlpatterns = [

    path('',views.list,name="list"),

    path('<public_id>',views.search,name="search"),
]