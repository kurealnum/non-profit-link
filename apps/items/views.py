from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org

from .models import Item
from .serializers import ItemSerializer

# Templates
ITEM_PAGE = "item_page.html"


def get_item(request, item_name):
    item = Item.objects.get(item_name=item_name)
    return render(request, ITEM_PAGE, context={"item": item})


def search_items_results(request):
    search = request.GET.get("search")
    org_or_item = request.GET.get("org")

    # Logic for search
    is_have = True if request.GET.get("is_want") == "on" else False
    is_need = True if request.GET.get("is_need") == "on" else False
    want = None
    if is_have and not is_need:
        want = False
    elif not is_have and is_need:
        want = True

    # Querysets are lazy so we can do this without querying
    if want is None:
        all_items = Item.objects.all()
    else:
        all_items = Item.objects.filter(want=want)

    if search and org_or_item == "item":
        if want is None:
            all_items = Item.objects.filter(item_name__trigram_similar=search)
        else:
            all_items = Item.objects.filter(
                item_name__trigram_similar=search, want=want
            )
    elif search and org_or_item == "org":
        possible_orgs = Org.objects.filter(username__trigram_similar=search)
        if want is None:
            all_items = Item.objects.filter(org__in=possible_orgs)
        else:
            all_items = Item.objects.filter(want=want, org__in=possible_orgs)

    return render(
        request,
        "search_items_results.html",
        context={"all_items": all_items, "search": search, "org": org_or_item},
    )


def search_items(request):
    all_items = Item.objects.all()
    return render(request, "search_items.html", context={"all_items": all_items})


# Any endpoints that take information from the request itself
class RequestDataApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method.lower() != "get":  # type: ignore
            permissions.append(IsAuthenticated())  # type: ignore
        return permissions

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
