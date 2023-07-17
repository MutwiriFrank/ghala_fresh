from django.shortcuts import render
from django.db import transaction

from users.models import Farmer
# from .models import Produce,   Purchase_produce
# @transaction.atomic


def purchase_produce(request, id):
    user = request.user
    farmer = Farmer.objects.filter(user_id = id)
    # produces = Produce.objects.all()
    # units = Unit.objects.all()

    context={
        "user": user,
        # "farmer": farmer,
        # "produces": produces
    }
    return render(request, 'cms/purchase_produce.html', context)




#purchase products




#Shipping_from_farm




#repackage products




#Repackaged_produce_to_services



#Received_products
