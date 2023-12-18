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
class PostPutItemApiView(APIView):
    # creates a new item
    def post(self, request):
        # getting the current user
        user = request.user
        org = Org.objects.get(username=user.username)

        # want is a singular value, makes user feedback on frontend simpler
        want = request.data.get("want")

        # all of this because no default error message :(
        all_serializer_errors = []
        serialzers_to_save = []

        for item in request.data.get("needsPOSTRequest"):
            # accepts a list of this data
            new_item = {
                "item_name": item["item_name"],
                "want": want,
                "units_description": item["units_description"],
                "count": item["count"],
                "org": org.id,  # type: ignore
            }
            new_serializer = ItemSerializer(data=new_item)
            if new_serializer.is_valid():
                # we dont want to save if there's one serializer that isn't valid
                serialzers_to_save.append(new_serializer)
            else:
                # we have to do all of this just to get the input_id into the errors
                errors = dict(new_serializer.errors)
                all_serializer_errors.append([errors, {"input_id": item["input_id"]}])

        if all_serializer_errors:
            return Response(all_serializer_errors, status=status.HTTP_400_BAD_REQUEST)

        # saving all of the new items
        for ser in serialzers_to_save:
            ser.save()

        return Response([], status=status.HTTP_201_CREATED)

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
            "count": request.data.get("count"),
        }

        if not Item.objects.filter(
            org=org_id, item_name=edited_item["old_item_name"]
        ).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        # if the object does exist, then
        Item.objects.filter(org=org_id, item_name=edited_item["old_item_name"]).update(
            item_name=edited_item["new_item_name"],
            want=edited_item["want"],
            units_description=edited_item["units_description"],
            count=edited_item["count"],
        )

        return Response(status=status.HTTP_200_OK)


# get and delete methods for the item model
class GetDeleteItemApiView(APIView):
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
