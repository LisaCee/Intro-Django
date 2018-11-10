from rest_framework import serializers, viewsets
from .models import Book

class BookSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'rating')
    # def create(self, validated_data):
    #     #create Reviewer
    #     reviewer = self.context['request'].reviewer
    #     book = Book.objects.create(reviewer = reviewer, **validated_data)
    #     return book    

class BookViewSet( viewsets.ModelViewSet) :        
    serializer_class = BookSerializer
    #filter by user
    queryset = Book.objects.all()
    # queryset.Book.objects.filter(...)
