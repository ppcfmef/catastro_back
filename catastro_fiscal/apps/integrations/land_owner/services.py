from django.conf import settings
from rest_framework.exceptions import APIException


class LandOwnerIntegrateService:

    url_api_env = None

    def get_url_api(self):
        if self.url_api_env is None:
            raise APIException({"error": "se require el url_api"})

        return getattr(settings, self.url_api_env)

    def get_key_api(self):
        return ""

    def clean_str(self, data):
        return data.capitalize() if isinstance(data, str) else None

    def exception(self, msg=""):
        if msg == "":
            msg = "No se encontraron resultados para esta busqueda"
        return APIException({"error": msg})
