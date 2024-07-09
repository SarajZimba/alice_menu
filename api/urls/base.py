# from .order import urlpatterns as order_urlpatterns
# from .user import urlpatterns as user_urlpatterns
from .menu import urlpatterns as menu_urlpatterns

urlpatterns = (
    []  + menu_urlpatterns #+ order_urlpatterns + user_urlpatterns +
)