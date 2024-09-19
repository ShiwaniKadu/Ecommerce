from django.urls import path
from . import views
urlpatterns = [
    path('accounts/login', views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logout, name='logout'),
    path('dashboard/about/', views.about, name='about'),
    path('dashboard/contact/', views.contact, name='contact'),
    path('dashboard/tracker/', views.tracker, name='tracker'),
    path('dashboard/product',views.product, name = "product"),
    path('dashboard/search',views.search, name = "search")
]