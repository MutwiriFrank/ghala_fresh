from django.contrib import admin
from .models import NewUser, Farmer, Vendor, Transporter, Employee, Location , Produce_buyer_to_farmer

# Register your models here.

admin.site.register(NewUser)
admin.site.register( Farmer)
admin.site.register( Vendor)
admin.site.register(Transporter)
admin.site.register( Employee)
admin.site.register( Location)
admin.site.register( Produce_buyer_to_farmer )
