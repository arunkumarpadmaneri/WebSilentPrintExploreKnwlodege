from django.urls import path
from web2printer import index_view
urlpatterns = [
    path('',index_view.home),
]
