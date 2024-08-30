from django.urls import path
from . import views
# views import UserListCreate, UerAddressListCreate

urlpatterns = [
    path('users/', views.UserCreateView.as_view(), name='user-create'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:id>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/address', views.UerAddressListCreate.as_view(), name='get_post_user'),
]