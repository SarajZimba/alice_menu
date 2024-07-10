from django.urls import path

from api.views.order import OrderCreateAPIView, OrderListView

urlpatterns = [
    path('create-order/<str:outlet_name>', OrderCreateAPIView.as_view(), name='create-order'),
    path('give-order/<str:outlet_name>', OrderListView.as_view(), name='give-order')
]