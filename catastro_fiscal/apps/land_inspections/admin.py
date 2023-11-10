from django.contrib import admin
from .models import (
    TicketType, TicketWorkStation, TicketSendStation, PhotoType, OwnerShipType, FacilityType, SupplyType,
    LandInspectionType
)


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_ticket', 'desc_tipo_ticket', )


@admin.register(TicketWorkStation)
class TicketWorkStationAdmin(admin.ModelAdmin):
    list_display = ('cod_est_trabajo_ticket', 'desc_est_trabajo_ticket', )


@admin.register(TicketSendStation)
class TicketSendStationAdmin(admin.ModelAdmin):
    list_display = ('cod_est_envio_ticket', 'desc_est_envio_ticket', )


@admin.register(PhotoType)
class PhotoTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_foto', 'desc_tipo_foto', )


@admin.register(OwnerShipType)
class OwnerShipTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_tit', 'desc_tipo_tit', )


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_inst', 'desc_tipo_inst', )


@admin.register(SupplyType)
class SupplyTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_sumi', 'desc_tipo_sumi', )


@admin.register(LandInspectionType)
class LandInspectionTypeAdmin(admin.ModelAdmin):
    list_display = ('cod_tipo_predio', 'desc_tipo_predio', )
