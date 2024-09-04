from django.contrib import admin  # noqa: F401
from import_export.admin import ImportExportModelAdmin
from .models import (
    MasterTypeUrbanUnit, MasterSide, MasterCodeStreet, MasterTipoPredio, MasterResolutionType, Institution,MasterTipoDocumentoIdentidad,MasterTipoContribuyente,
    MasterTipoPropiedad,MasterTipoTransferencia,MasterTipoNivel, MasterTipoMaterial,MasterTipoEstadoConservacion, MasterClaseUso, MasterSubClaseUso,MasterTipoUsoPredio
)


class MasterAdminMixin:
    list_display = ('id', 'name')


@admin.register(MasterTypeUrbanUnit)
class MasterTypeUrbanUnitAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterSide)
class MasterSideAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterCodeStreet)
class MasterCodeStreetAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoPredio)
class MasterPropertyTypeAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterResolutionType)
class MasterResolutionTypeAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoDocumentoIdentidad)
class MasterTipoDocumentoIdentidadAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoContribuyente)
class MasterTipoContribuyenteAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoPropiedad)
class MasterTipoPropiedadAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoTransferencia)
class MasterMasterTipoTransferenciaAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoUsoPredio)
class MasterTipoUsoPredioAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass






@admin.register(MasterTipoNivel)
class MasterTipoNivelAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoMaterial)
class MasterTipoMaterialAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterTipoEstadoConservacion)
class MasterTipoEstadoConservacionAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass



@admin.register(MasterClaseUso)
class MasterClaseUsoAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterSubClaseUso)
class MasterSubClaseUsoAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass