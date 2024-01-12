from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from corsheaders.signals import check_request_enabled
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookListCreateAPI(ListAPIView, CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        response = Response({"message": "Success", "books": serializer.data}, status=status.HTTP_200_OK)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response({"message": "Success", "book": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            response = Response({"message": "Error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response

class BookDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        response = Response({"message": "Success", "book": serializer.data}, status=status.HTTP_200_OK)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response({"message": "Success", "book": serializer.data}, status=status.HTTP_200_OK)
        else:
            response = Response({"message": "Error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response = Response({"message": "Success"}, status=status.HTTP_204_NO_CONTENT)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response

class CategoryListCreateAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response({"message": "Success", "category": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            response = Response({"message": "Error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response
    
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        response = Response({"message": "Success", "categories": serializer.data}, status=status.HTTP_200_OK)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response
class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response({"message": "Success", "category": serializer.data}, status=status.HTTP_200_OK)
        else:
            response = Response({"message": "Error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        response = Response({"message": "Success", "category": serializer.data}, status=status.HTTP_200_OK)
        check_request_enabled.send(sender=self.__class__, request=request, response=response)
        return response
