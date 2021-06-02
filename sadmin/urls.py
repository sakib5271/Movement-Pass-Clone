from fuser.models import MovementReason
from django.urls import path
from . import views

urlpatterns = [
    path('dasboard',views.Dashboard.as_view(), name='dashboard'),
    path('movement-pass/all/search/query/',views.SearchAdmin.as_view(), name='search'),

    path('all/movement-pass/', views.AllPassView.as_view(), name='allpass'),
    path('view/movement-pass/<str:id>/', views.SinglePass.as_view(), name='single_pass'),

    path('movement-pass/view/all/approved',views.ViewApprovedPass.as_view(),name='approved_pass'),
    path('movement-pass/view/all/disapproved',views.ViewDisapprovedPass.as_view(),name='disapproved_pass'),
    path('movement-pass/view/all/expired',views.ViewExpiredPass.as_view(),name='expired_pass'),

    path('view/all-users/movementpass/', views.AllUsers.as_view(),name='all_users'),
    path('movement-pass/view/user/<str:id>',views.SingleUser.as_view(), name='single_user'),
    
    path('movement-pass/<str:id>/approved/', views.MakeApprove.as_view(), name='approved'),
    path('movement-pass/<str:id>/disapproved/',views.MakeDisapprove.as_view(), name='disapproved'),
    path('movement-pass/<str:id>/expired/',views.MakeExpire.as_view(), name='expired'),
    path('movement-pass/<str:id>/Delete/', views.DeletePass.as_view(), name='deleted'),

    path('movement-pass/view/movement-reasons/',views.MovementReasonView.as_view(), name='reason'),
    path('movement-pass/view/movement-reasons/delete/<str:id>/', views.DeleteMovementReasonView.as_view(), name='delete_reason'),

    path('movement-pass/view/district/', views.DistrictView.as_view(), name='district'),
    path('movement-pass/delete/district/<str:id>',views.DeleteDistrict.as_view(),name='delete_district'),

    path('movement-pass/view/time-hours/', views.TimeSpendsView.as_view(), name='time'),
    path('movement-pass/delete/time-hours/<str:id>', views.DeleteTime.as_view(), name='delete_time'),
]