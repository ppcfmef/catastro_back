from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    TicketType, TicketWorkStation, TicketSendStation, Ticket, PhotoType, LocationPhoto, RecordOwnerShip, OwnerShipType,
    Location, LandCharacteristic, FacilityType, LandFacility, LandSupply, SupplyType ,LandInspectionType,
    LandInspection, LandOwnerInspection, LandOwnerDetailInspection, LandInspectionUpload
)


@admin.register(LandInspectionUpload)
class LandInspectionUploadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass


@admin.register(LocationPhoto)
class LocationPhotoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(RecordOwnerShip)
class RecordOwnerShipAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tit', 'status')



@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_ubicacion', 'status')
    


@admin.register(LandCharacteristic)
class LandCharacteristicAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass



@admin.register(LandFacility)
class LandFacilityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(LandSupply)
class LandSupplyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass



@admin.register(LandInspection)
class LandInspectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id', 'cod_tit','ubigeo','cod_cpu','cod_pre')

@admin.register(LandOwnerInspection)
class LandOwnerInspectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(LandOwnerDetailInspection)
class LandOwnerDetailInspectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(TicketType)
class TicketTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_ticket', 'desc_tipo_ticket', )



@admin.register(TicketWorkStation)
class TicketWorkStationAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_est_trabajo_ticket', 'desc_est_trabajo_ticket', )


@admin.register(TicketSendStation)
class TicketSendStationAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_est_envio_ticket', 'desc_est_envio_ticket', )


@admin.register(PhotoType)
class PhotoTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_foto', 'desc_tipo_foto', )


@admin.register(OwnerShipType)
class OwnerShipTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_tit', 'desc_tipo_tit', )


@admin.register(FacilityType)
class FacilityTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_inst', 'desc_tipo_inst', )


@admin.register(SupplyType)
class SupplyTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_sumi', 'desc_tipo_sumi', )


@admin.register(LandInspectionType)
class LandInspectionTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_tipo_predio', 'desc_tipo_predio', )


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_ticket', 'cod_usuario')

    # def get_cod_carga(self, obj):
    #     return obj.inspection_upload.cod_carga

    # get_cod_carga.short_description = 'cod_carga'
