from django.urls import path
from .views import CacheExplorerList, CacheExplorerDetail

urlpatterns = [
    path("", CacheExplorerList.as_view(), name="cache_explorer_list"),
    path("<int:pk>/", CacheExplorerDetail.as_view(), name="cache_explorer_detail"),
]
