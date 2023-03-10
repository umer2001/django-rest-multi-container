from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import os
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class HelloWorld(APIView):
    def get(self, request):
        return Response({'environment': os.environ.get("ENVIRONMENT", "default value")})

class Connection(APIView):
    def get(self, request):
        try:
            # Try to execute a simple SQL query to check the connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                row = cursor.fetchone()
            if row[0] == 1:
                return Response({
                'environment': os.environ.get("ENVIRONMENT", "default value"),
                'database': "Database connection successfull"
                })
        except:
            return Response({
                'environment': os.environ.get("ENVIRONMENT", "default value"),
                'database': "Database connection failed"
                })
