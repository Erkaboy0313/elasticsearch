from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ProductDocument,Product
from .serializers import ProductDocumentSerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet
from elasticsearch_dsl import Q


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDocumentView(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    filter_backends = [
        SearchFilterBackend,
    ]
    search_fields = (
        'name',
        'product_id',
    )

    def filter_queryset(self, queryset):

        def get_query(self):
            search_query = self.request.query_params.get('search', None)
            if search_query:
                if not search_query.isdigit():
                    return Q("match", name={
                        'query': search_query,
                        'fuzziness': 'AUTO'  # Or specify the level of fuzziness (e.g., '2')
                    })
                else:
                    return Q("match", product_id = search_query)  
            return None
        
        search_query = get_query(self)

        if search_query:
            queryset = queryset.query(search_query)

        return queryset