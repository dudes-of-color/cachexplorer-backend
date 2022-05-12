from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CacheExplorer
from .permissions import IsOwnerOrReadOnly
from .serializers import CacheExplorerSerializer


class CacheExplorerList(ListCreateAPIView):
    queryset = CacheExplorer.objects.all()
    serializer_class = CacheExplorerSerializer

class CacheExplorerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CacheExplorer.objects.all()
    serializer_class = CacheExplorerSerializer
