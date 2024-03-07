from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
    class Django:
        model = Product
        fields = [
            "id",
            "product_id",
            "name",
            "type",
            "size",
            "description",
            "created_time",
            "updated_time",
        ]