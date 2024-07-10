from django.urls import path
from api.views.menu import MenuCreateAPIView, IsPromotional, IsTodaySpecial, ImageByteView, MenuListView

urlpatterns = [
    path("menu-create/<str:outlet_name>", MenuCreateAPIView.as_view(), name="menu-create"),
    path("menu-list/<str:outlet_name>", MenuListView.as_view(), name="menu-create"), 
    path("menu-todayspecial/", IsTodaySpecial.as_view(), name="menu-todayspecial"),
    path("menu-promotional/", IsPromotional.as_view(), name="menu-promotional"),
    path("images/<str:menu_name>", ImageByteView.as_view(), name="menu-imagebyte"),

]