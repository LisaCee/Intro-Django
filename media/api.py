from rest_framework import serializers, viewsets
from .models import Book, Reviewer

class BookSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'rating')
    def create(self, validated_data):
        #create Reviewer
        current_user = self.context['request'].user
        current_reviewer = Reviewer.objects.get(user = current_user)
        book = Book.objects.create(reviewer = current_reviewer, **validated_data)
        return book    

class BookViewSet( viewsets.ModelViewSet) :        
    serializer_class = BookSerializer
    #filter by user
    queryset = Book.objects.all()
    # queryset.Book.objects.filter(...)
