from django.contrib import admin
from import_export import resources
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



class TicketTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_ticket', 'desc_tipo_ticket', )
    class Meta:
        model = TicketType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_ticket',)

@admin.register(TicketType)
class TicketTypeAdmin(ImportExportModelAdmin):
    resource_class = TicketTypeResource
    list_display = ('cod_tipo_ticket', 'desc_tipo_ticket', )

class TicketWorkStationResource(resources.ModelResource):
    list_display = ('cod_est_trabajo_ticket', 'desc_est_trabajo_ticket', )
    class Meta:
        model = TicketWorkStation
        exclude = ('id',)
        import_id_fields = ('cod_est_trabajo_ticket',)


@admin.register(TicketWorkStation)
class TicketWorkStationAdmin(ImportExportModelAdmin):
    resource_class = TicketWorkStationResource
    list_display = ('cod_est_trabajo_ticket', 'desc_est_trabajo_ticket', )

class TicketSendStationResource(resources.ModelResource):
    list_display = ('cod_est_envio_ticket', 'desc_est_envio_ticket', )
    class Meta:
        model = TicketSendStation
        exclude = ('id',)
        import_id_fields = ('cod_est_envio_ticket',)
        
@admin.register(TicketSendStation)
class TicketSendStationAdmin(ImportExportModelAdmin):
    
    resource_class = TicketSendStationResource
    list_display = ('cod_est_envio_ticket', 'desc_est_envio_ticket', )


class PhotoTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_foto', 'desc_tipo_foto', )
    class Meta:
        model = PhotoType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_foto',)


@admin.register(PhotoType)
class PhotoTypeAdmin(ImportExportModelAdmin,):
    resource_class = PhotoTypeResource
    list_display = ('cod_tipo_foto', 'desc_tipo_foto', )


class OwnerShipTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_tit', 'desc_tipo_tit', )
    class Meta:
        model = OwnerShipType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_tit',)


@admin.register(OwnerShipType)
class OwnerShipTypeAdmin(ImportExportModelAdmin):
    resource_class = OwnerShipTypeResource
    list_display = ('cod_tipo_tit', 'desc_tipo_tit', )


class FacilityTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_inst', 'desc_tipo_inst', )
    class Meta:
        model = FacilityType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_inst',)
    
@admin.register(FacilityType)
class FacilityTypeAdmin(ImportExportModelAdmin):
    resource_class = FacilityTypeResource
    list_display = ('cod_tipo_inst', 'desc_tipo_inst', )
    # exclude = ('id',)
    # import_id_fields = ('cod_tipo_inst',)
    
    
    
class SupplyTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_sumi', 'desc_tipo_sumi', )
    class Meta:
        model = SupplyType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_sumi',)

@admin.register(SupplyType)
class SupplyTypeAdmin(ImportExportModelAdmin):
    resource_class = SupplyTypeResource
    list_display = ('cod_tipo_sumi', 'desc_tipo_sumi', )


class LandInspectionTypeResource(resources.ModelResource):
    list_display = ('cod_tipo_predio', 'desc_tipo_predio', )
    class Meta:
        model = LandInspectionType
        exclude = ('id',)
        import_id_fields = ('cod_tipo_predio',)


@admin.register(LandInspectionType)
class LandInspectionTypeAdmin(ImportExportModelAdmin):
    resource_class = LandInspectionTypeResource
    list_display = ('cod_tipo_predio', 'desc_tipo_predio', )


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cod_ticket', 'cod_usuario')

    # def get_cod_carga(self, obj):
    #     return obj.inspection_upload.cod_carga

    # get_cod_carga.short_description = 'cod_carga'
