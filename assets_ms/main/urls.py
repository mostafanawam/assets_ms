from django.urls import path
from .views import  *
from django.contrib.auth.views import LogoutView
app_name = "main"
urlpatterns = [
      
      path('login/', login_view, name='login_view'),
      path('logout/', logout_view, name='logout_view'),

      path('assets/', asset_view, name='asset_view'),
      path('asset/<int:asset_id>/',edit_asset, name='edit_asset'),
      path('assets/delete/<int:asset_id>/', delete_asset, name='delete_asset'),
      path('asset/lend/<int:asset_id>/',lend_asset, name='lend_asset'),
      path('asset/return/<int:asset_id>/',return_asset, name='return_asset'),


]
