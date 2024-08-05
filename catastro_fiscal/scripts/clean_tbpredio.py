from apps.lands.models import *
from apps.historical.models import HistoricalRecord


def run():
    Domicilio.objects.filter(contribuyente__ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    LandNivelConstruccion.objects.filter(land_owner_detail__land__ubigeo__in= ['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    LandOwnerDetail.objects.filter(land__ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    LandOwner.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()

    # Domicilio.objects.filter(contribuyente__ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    # UploadHistory.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    # TemploralUploadRecord.objects.all().delete()
    # LandOwner.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    # Land.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    # LandOwnerDetail.objects.filter(land__ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()
    # LandAudit.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).delete()

    # # clean Historical
    # HistoricalRecord.objects.all().delete()F
