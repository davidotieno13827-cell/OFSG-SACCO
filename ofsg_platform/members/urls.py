from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.update_profile, name='profile'),
    path('members/', views.members_list, name='members_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('register/', views.register_member, name='register_member'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('<int:member_id>/files/<str:file_type>/', views.secure_member_file, name='member_file'),
    path('management-summary/', views.management_summary, name='management_summary'),
    path('add-contribution/', views.add_contribution, name='add_contribution'),
    path('add-fine/', views.add_fine, name='add_fine'),
    path('fines/<int:fine_id>/mark-paid/', views.mark_fine_paid, name='mark_fine_paid'),
]
