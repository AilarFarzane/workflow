from django.urls import path
from .views import UserList, UserApplyAction, user_action_tree_view

urlpatterns = [
    path('users/', UserList, name='user-list'),
    path('users/<int:user_id>/actions/', UserApplyAction, name='user-actions'),
    path('users/<int:user_id>/action-tree/', user_action_tree_view, name='user-action-tree'),
]
