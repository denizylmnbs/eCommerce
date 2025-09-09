from rest_framework import routers
from .views import CategoryViewSet, SubCategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
]+router.urls
