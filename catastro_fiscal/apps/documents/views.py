from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Document, Category
from .serializers import DocumentSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['parent']
    ordering_fields = ['id', 'name', 'parent']


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['category']
    ordering_fields = ['id', 'title', 'description', 'type', 'category']
    document_type = None

    def get_queryset(self):
        if self.document_type:
            return self.queryset.filter(type=self.document_type)
        return self.queryset

    def create(self, request, *args, **kwargs):
        request.data['type'] = self.document_type
        return super(DocumentViewSet, self).create(request, *args, *kwargs)

    def update(self, request, *args, **kwargs):
        request.data['type'] = self.document_type
        return super(DocumentViewSet, self).update(request, *args, **kwargs)


class ManualViewSet(DocumentViewSet):
    document_type = Document.DocumentType.USER_MANUAL


class TutorialViewSet(DocumentViewSet):
    document_type = Document.DocumentType.VIDEO_TUTORIAL


class FAQViewSet(DocumentViewSet):
    document_type = Document.DocumentType.FAQ
