from . import views
from django.urls import path

urlpatterns = [
    path('home', views.Home, name="home"),
    path('hobbies', views.Hobbies, name="hobbies"),
    path('portfolio', views.Port, name="portfolio"),
    path('contact', views.Contact, name="contact"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
    # path('item_index', views.item_index, name="item_index"),
    path('portfolio/<int:item_id>', views.item_detail, name="item_detail"),
    path('add_item', views.create_item, name="create_item"),
    path('update/<int:id>', views.update_item, name="update_item"),
    path('delete/<int:id>', views.delete_item, name="delete_item"),

   # path('add_contact', views.create_contact, name="create_contact"),
]
