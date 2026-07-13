from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Item


@require_http_methods(["GET", "POST"])
def item_list(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        quantity = request.POST.get("quantity", 1)
        item = Item.objects.create(name=name, quantity=quantity)
        return JsonResponse({"id": item.id, "name": item.name, "quantity": item.quantity})

    items = list(Item.objects.values("id", "name", "quantity"))
    return JsonResponse(items, safe=False)


@require_http_methods(["GET", "PUT", "DELETE"])
def item_detail(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    if not item:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == "PUT":
        item.name = request.POST.get("name", item.name)
        item.quantity = request.POST.get("quantity", item.quantity)
        item.save()
        return JsonResponse({"id": item.id, "name": item.name, "quantity": item.quantity})

    if request.method == "DELETE":
        item.delete()
        return JsonResponse({"message": "Deleted"})

    return JsonResponse({"id": item.id, "name": item.name, "quantity": item.quantity})
