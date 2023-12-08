from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org
from .models import Item
from .serializers import ItemSerializer


def search_items(request):
    return render(request, "search_items.html")


class ItemListApiView(APIView):
    def get(self, request):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)

        all_items = Item.objects.filter(org=org)
        serializer = ItemSerializer(all_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)

        data = {
            "item_name": request.data.get("item_name"),
            "want": request.data.get("want"),
            "units_description": request.user.id,
            "count": request.data.get("count"),
            "org": org.id,  # type: ignore
        }
        serializer = ItemSerializer(data=data)  # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
