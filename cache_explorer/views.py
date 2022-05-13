from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cache
from .permissions import IsOwnerOrReadOnly
from .serializers import CacheSerializer


class CacheExplorerList(ListCreateAPIView):
    queryset = Cache.objects.all()
    serializer_class = CacheSerializer

class CacheExplorerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cache.objects.all()
    serializer_class = CacheSerializer
