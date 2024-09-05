from apps.lands.models import *
from apps.historical.models import HistoricalRecord


def run():
    


    Domicilio.objects.filter(contribuyente__ubigeo__in=['220901']).delete()
    Contacto.objects.filter(contribuyente__ubigeo__in=['220901']).delete()
    UploadHistory.objects.filter(ubigeo__in=['220901']).delete()
    
    LandNivelConstruccion.objects.filter(land_owner_detail__land__ubigeo__in= ['220901']).delete()
    LandOwnerDetail.objects.filter(land__ubigeo__in=['220901']).delete()
    LandOwner.objects.filter(ubigeo__in=['220901']).delete()
    
    Land.objects.filter(ubigeo__in=['220901']).delete()
    
    LandAudit.objects.filter(ubigeo__in=['220901']).delete()

    # clean Historical
    # HistoricalRecord.objects.filter(ubigeo__in=['220901']).delete()
    # TemploralUploadRecord.objects.filter(ubigeo__in=['220901']).delete()



    # Domicilio.objects.filter(contribuyente__ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    # Contacto.objects.filter(contribuyente__ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    # UploadHistory.objects.filter(ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    
    # LandNivelConstruccion.objects.filter(land_owner_detail__land__ubigeo__in= ['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    # LandOwnerDetail.objects.filter(land__ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    # LandOwner.objects.filter(ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    
    # Land.objects.filter(ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()
    
    # LandAudit.objects.filter(ubigeo__in=['240303','120421','060905','021401','020108','240104','050405','250401','240105','220303','061201','170301','190206','040515','050911','010523','020601','130201','040701','220705','060105','140102','040703','100507']).delete()

    # # clean Historical
    # HistoricalRecord.objects.all().delete()
    # TemploralUploadRecord.objects.all().delete()
