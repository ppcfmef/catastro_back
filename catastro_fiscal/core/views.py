from rest_framework.response import Response



class CustomListMixin:
    def custom_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)


class CustomSerializerMixin:
    def get_serializer_class(self):
        serializer_action_class = getattr(self, f'{self.action}_serializer_class', None)
        if serializer_action_class:
            return serializer_action_class
        return super(CustomSerializerMixin, self).get_serializer_class()




