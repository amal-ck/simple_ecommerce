from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingItems
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404

class CartItemView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = ShoppingItems.objects.get(id=id)
                serializer = ItemSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except ShoppingItems.DoesNotExist:
                return Response({"status": "error", "message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        items = ShoppingItems.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = ShoppingItems.objects.get(id=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(ShoppingItems, id=id)
        item.delete()
        return Response({"status":"success", "data":"item deleted"})
