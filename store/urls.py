from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('linkedin', views.linkedin, name='linkedin'),
    path('github', views.github, name='github'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update', views.update, name='update'),
    path('logout', views.logoutPage, name='logout'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
]
