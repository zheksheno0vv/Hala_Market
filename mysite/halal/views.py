# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics, viewsets, status
# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import generics, viewsets, status,permissions
# from rest_framework.filters import SearchFilter, OrderingFilter
# from .models import *
# from .serializer import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import *
#
# class CartCreateAPIView(generics.CreateAPIView):
#     serializer_class = CartSerialize
#
#
# class CartListAPIView(generics.ListAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     search_fields = ['clothes_name']
#     ordering_fields = ['price']
#
#
#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)
#
#     def retrieve(self, request, *args, **kwargs):
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         serializer = self.get_serializer(cart)
#         return Response(serializer.data)
#
#
# class CartItemCreateAPIView(generics.CreateAPIView):#?
#     serializer_class = CartItemSerializer
#
#     def get_queryset(self):
#         return CartItem.objects.filter(cart__user=self.request.user)
#
#     def perform_create(self, serializer):
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         serializer.save(cart=cart)
#
#
# class CartItemUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#
#     def get_queryset(self):
#         return Order.objects.all()
