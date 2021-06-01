from django.urls import path
from . import views

urlpatterns = [
    path('movement-pass/apply/', views.PassApply.as_view(), name="apply"),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
     
    path('edit/profile/', views.EditProfile.as_view(), name='edit_profile'),
    
    path('movement-pass/collect/',views.CollectPass.as_view(), name='collect'),
    path('movement-pass/view/<str:id>/', views.ViewPass.as_view(), name='single'),
]