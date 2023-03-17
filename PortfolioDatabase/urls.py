from . import views
from django.urls import path

urlpatterns = [
    path('home', views.Home, name="home"),
    path('hobbies', views.Hobbies, name="hobbies"),
    path('portfolio', views.Port, name="portfolio"),
    path('contact', views.Contact, name="contact"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
 #   path('portfolio/<int:item_id>', views.detail2, name="item_detail.html"),
    path('portfolio/<int:item_id>', views.item_detail, name="item_detail"),
]
