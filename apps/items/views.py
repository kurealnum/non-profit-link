from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org

from .models import Item
from .serializers import ItemSerializer


def search_items(request):
    return render(request, "search_items.html")


# post and put requests for the model
class RequestDataApiView(APIView):
    def post(self, request):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)

        # accepts a list of this data
        new_item = {
            "item_name": request.data.get("item_name"),
            "want": request.data.get("want"),
            "units_description": request.data.get("units_description"),
            "count": int(request.data.get("count")),
            "org": org.id,  # type: ignore
        }

        new_item_serializer = ItemSerializer(data=new_item)
        new_item_serializer.is_valid()

        if new_item_serializer.errors:
            return Response(
                {
                    "errors": new_item_serializer.errors,
                    "input_id": request.data.get("input_id"),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_item_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    # UNTESTED
    def put(self, request):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        # dont include org_id in this data because that would be redundant
        edited_item = {
            "old_item_name": request.data.get("old_item_name"),
            "new_item_name": request.data.get("new_item_name"),
            "want": request.data.get("want"),
            "units_description": request.data.get("units_description"),
            "count": int(request.data.get("count")),
        }

        serializer_info = {
            "item_name": edited_item["new_item_name"],
            "want": edited_item["want"],
            "units_description": edited_item["units_description"],
            "count": edited_item["count"],
            "org": org_id,
        }

        # just to automatically check for errors
        serializer_for_errors = ItemSerializer(data=serializer_info)
        if not serializer_for_errors.is_valid():
            return Response(
                {
                    "errors": serializer_for_errors.errors,
                    "input_id": request.data.get("input_id"),
                },
                status.HTTP_400_BAD_REQUEST,
            )

        if not Item.objects.filter(
            org=org_id, item_name=edited_item["old_item_name"]
        ).exists():
            return Response(
                {
                    "errors": ["The item that you are trying to edit does not exist"],
                    "input_id": request.data.get("input_id"),
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # if the object does exist, then
        Item.objects.filter(org=org_id, item_name=edited_item["old_item_name"]).update(
            item_name=edited_item["new_item_name"],
            want=edited_item["want"],
            units_description=edited_item["units_description"],
            count=edited_item["count"],
        )

        return Response(status=status.HTTP_200_OK)


# get and delete methods for the item model
class UrlDataApiView(APIView):
    # returns selected item info
    def get(self, request, item_name):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        item = get_object_or_404(Item, org=org_id, item_name=item_name)

        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, item_name):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        # getting and deleting the item
        item = get_object_or_404(Item, org=org_id, item_name=item_name)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
