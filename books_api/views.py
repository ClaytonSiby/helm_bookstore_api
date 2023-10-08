from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books_list(format=None):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({ "message": "Success", "books": serializer.data }, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "message": "Success", "book": serializer.data }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book_details(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({ "message": "Book not found 404" }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return Response({ "message": "Success", "book": book_serializer.data }, status=status.HTTP_200_OK)

    
@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    book_serializer = BookSerializer(book, data=request.data)
    if book_serializer.is_valid():
        book_serializer.save()
        return Response({ "message": "Success", "book": book_serializer.data }, status=status.HTTP_200_OK)
    return Response({ "message": "Error", "errors": book_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({ "message": "Success" }, status=status.HTTP_204_NO_CONTENT)
