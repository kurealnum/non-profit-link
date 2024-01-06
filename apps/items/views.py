from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org

from .models import Item
from .serializers import ItemSerializer


def search_items(request):
    # if all of these parameters exist, then we need to do something different
    search = request.GET.get("search")
    org = request.GET.get("org")
    is_want = True if request.GET.get("is_want") == "on" else False
    is_need = True if request.GET.get("is_need") == "on" else False
    # querysets are lazy so we can do this without querying :0
    all_items = Item.objects.all()

    if not is_want and not is_need:
        all_items = None
    elif search and org == "item" and is_want and is_need:
        if is_want and is_need:
            all_items = Item.objects.filter(item_name__trigram_similar=search)
        elif is_want:
            all_items = Item.objects.filter(
                item_name__trigram_similar=search, want=True
            )
        elif is_need:
            all_items = Item.objects.filter(
                item_name__trigram_similar=search, want=False
            )
    elif search and org == "org":
        # return items related to the search
        possible_orgs = Org.objects.filter(username__trigram_similar=search)
        all_items = Item.objects.filter(org__in=possible_orgs)
    return render(
        request,
        "search_items.html",
        context={"all_items": all_items, "search": search, "org": org},
    )


# any endpoints that take information from the request itself
class RequestDataApiView(APIView):
    def post(self, request):
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        # accepts a list of this data
        new_item = {
            "item_name": request.data.get("item_name"),
            "want": request.data.get("want"),
            "units_description": request.data.get("units_description"),
            "count": int(request.data.get("count")),
            "org": org_id,
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

    def put(self, request):
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore
        old_item_name = request.data.get("old_item_name")

        serializer_info = {
            "item_name": request.data.get("new_item_name"),
            "want": request.data.get("want"),
            "units_description": request.data.get("units_description"),
            "count": int(request.data.get("count")),
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

        if not Item.objects.filter(org=org_id, item_name=old_item_name).exists():
            return Response(
                {
                    "errors": ["The item that you are trying to edit does not exist"],
                    "input_id": request.data.get("input_id"),
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        Item.objects.filter(org=org_id, item_name=old_item_name).update(
            item_name=serializer_info["item_name"],
            want=serializer_info["want"],
            units_description=serializer_info["units_description"],
            count=serializer_info["count"],
        )

        return Response(status=status.HTTP_200_OK)


# any endpoints that take information from the URL
class UrlDataApiView(APIView):
    def get(self, request, item_name):
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        item = get_object_or_404(Item, org=org_id, item_name=item_name)
        # no need to check for errors, because the item in our database should
        # be valid already
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, item_name):
        user = request.user
        org = Org.objects.get(username=user.username)
        org_id = org.id  # type: ignore

        item_to_delete = get_object_or_404(Item, org=org_id, item_name=item_name)
        item_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
