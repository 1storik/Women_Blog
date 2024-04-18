from django.urls import path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('contact/', contact, name='contact'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('logout/', logout_user, name='logout'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', WomenCategory.as_view(), name='category'),
]
