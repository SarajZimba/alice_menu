from django.urls import path
from api.views.menu import MenuCreateAPIView, IsPromotional, IsTodaySpecial, ImageByteView

urlpatterns = [
    path("menu-create/", MenuCreateAPIView.as_view(), name="menu-create"),
    path("menu-todayspecial/", IsTodaySpecial.as_view(), name="menu-todayspecial"),
    path("menu-promotional/", IsPromotional.as_view(), name="menu-promotional"),
    path("images/<str:menu_name>", ImageByteView.as_view(), name="menu-imagebyte"),

]