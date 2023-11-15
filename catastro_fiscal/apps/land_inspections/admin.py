from django.contrib import admin

from .models import TicketType, TicketWorkStation,TicketSendStation,Ticket,PhotoType,LocationPhoto,RecordOwnerShip,OwnerShipType,Location,LandCharacteristic,FacilityType,LandFacility,LandSupply,SupplyType,LandInspectionType,LandInspection,LandOwnerInspection,LandOwnerDetailInspection,LandInspectionUpload


@admin.register(LandInspectionUpload)
class LandInspectionUploadAdmin(admin.ModelAdmin):
    pass

@admin.register(TicketWorkStation)
class TicketWorkStationAdmin(admin.ModelAdmin):
    pass

@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('cod_ticket', 'cod_est_trabajo_ticket')
   

@admin.register(TicketSendStation)
class TicketSendStationAdmin(admin.ModelAdmin):
    pass

@admin.register(PhotoType)
class PhotoTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(LocationPhoto)
class LocationPhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(RecordOwnerShip)
class RecordOwnerShipAdmin(admin.ModelAdmin):
    list_display = ('cod_tit', 'status')

@admin.register(OwnerShipType)
class OwnerShipTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('cod_ubicacion', 'status')
    


@admin.register(LandCharacteristic)
class LandCharacteristicAdmin(admin.ModelAdmin):
    pass

@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(LandFacility)
class LandFacilityAdmin(admin.ModelAdmin):
    pass

@admin.register(LandSupply)
class LandSupplyAdmin(admin.ModelAdmin):
    pass

@admin.register(SupplyType)
class SupplyTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(LandInspectionType)
class LandInspectionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(LandInspection)
class LandInspectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_tit','ubigeo','cod_cpu','cod_pre')

@admin.register(LandOwnerInspection)
class LandOwnerInspectionAdmin(admin.ModelAdmin):
    pass

@admin.register(LandOwnerDetailInspection)
class LandOwnerDetailInspectionAdmin(admin.ModelAdmin):
    pass
