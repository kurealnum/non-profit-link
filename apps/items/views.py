from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org
from .models import Item
from .serializers import ItemSerializer


def search_items(request):
    return render(request, "search_items.html")


# post and put requests for the model
class SpecificItemApiView(APIView):
    # creates a new item
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


# get and delete methods for the item model
class SingleItemApiView(APIView):
    # returns selected item info
    def get(self, request, item_name):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        if not Item.objects.filter(org=org_id, item_name=item_name).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        item = Item.objects.get(org=org, item_name=item_name)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, item_name):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        # getting and deleting the item
        if Item.objects.filter(org=org_id, item_name=item_name).exists():
            Item.objects.get(org=org_id, item_name=item_name).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
