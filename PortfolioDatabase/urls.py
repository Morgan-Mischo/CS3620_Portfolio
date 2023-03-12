from . import views
from django.urls import path

urlpatterns = [
    path('home', views.Home, name="home"),
    path('hobbies', views.Hobbies, name="hobbies"),
    path('portfolio', views.Portfolio, name="portfolio"),
    path('contact', views.Contact, name="contact"),
    path('hobbies/<int:hobby_id>', views.detail, name="detail"),
    path('portfolio/<int:item_id>', views.detail2, name="detail2"),
    # path('portfolio/<int:item_id>', views.detail, name="detail"),
]
