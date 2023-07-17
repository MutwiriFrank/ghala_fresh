from django.urls import path
from .views import purchase_produce

app_name = 'cms'

urlpatterns = [
   
    path('purchase-produce/<str:id>/', purchase_produce, name="purchase_produce")

    # path('farmer-details', update_farmer, name="update_farmer")

]