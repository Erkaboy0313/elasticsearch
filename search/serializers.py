from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import ProductDocument,Product
from rest_framework.serializers import ModelSerializer

class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'