from django.urls import path

from api.views.order import OrderCreateAPIView

urlpatterns = [
    path('create-order/', OrderCreateAPIView.as_view(), name='create-order')


]