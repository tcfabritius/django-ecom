from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from .models import DeliveryOptions

@login_required
def deliverychoises(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "checkout/delivery_choises.html", {"deliveryoptions": deliveryoptions})

@login_required
def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        delivery_option = request.POST.get("deliveryoption")
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)
        session = request.session
        if "purhace" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True
        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response