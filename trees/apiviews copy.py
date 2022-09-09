from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from .models import Specie, Square, Family, Tree
from .serializers import SpecieSerializer, SquareSerializer, FamilySerializer, TreeSerializer


class SpecieAPIView(APIView):
    """
    API Arborização = Espécies cadastradas
    """
    def get(self, request):
        species = Specie.objects.all()
        serializer = SpecieSerializer(species, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = SpecieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FamilyAPIView(APIView):
    """
    API Arborização = Famílias de espécies cadastradas
    """

    def get(self, request):
        family = Family.objects.all()
        serializer = FamilySerializer(family, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = FamilySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SquareAPIView(APIView):
    """
    API Arborização = Praças Cadastradas
    """

    def get(self, request):
        square = Square.objects.all()
        serializer = SquareSerializer(square, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SquareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    


class TreeAPIView(APIView):
    """
    API Arborização = Árvores cadastradas
    """

    def get(self, request):
        tree = Tree.objects.all()
        serializer =  TreeSerializer(tree, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TreeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)