from rest_framework import serializers, viewsets
from .models import News

# News
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'body', 'date')

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    search_fields = ('title', 'body', 'date')
