import typing

from django.conf import settings
from django.http import HttpRequest
from rest_framework_api_key.permissions import KeyParser, HasAPIKey


class QueryParamKeyParser(KeyParser):
    def get(self, request: HttpRequest) -> typing.Optional[str]:
        custom_header = getattr(settings, "API_KEY_CUSTOM_HEADER", None)
        query_param = getattr(settings, "API_KEY_QUERY_PARAM", None)

        if query_param is not None:
            return self.get_from_query_param(request, query_param)
        if custom_header is not None:
            return self.get_from_header(request, custom_header)

        return self.get_from_authorization(request)

    def get_from_query_param(self, request: HttpRequest, name: str) -> typing.Optional[str]:
        return request.query_params.get(name) or None


class CustomHasAPIKey(HasAPIKey):
    key_parser = QueryParamKeyParser()
