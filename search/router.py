from rest_framework.routers import SimpleRouter
from .views import ProductDocumentView,ProductView

router = SimpleRouter()

router.register(r'product-search', ProductDocumentView, basename='product-search')
router.register(r'product', ProductView, basename='product')
