from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Specie, Square, Family, Tree
from .serializers import SpecieSerializer, SquareSerializer, FamilySerializer, TreeSerializer


"""
API V1
"""

class SpeciesAPIView(generics.ListCreateAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

class SpecieAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer



class SquaresAPIView(generics.ListCreateAPIView):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer

class SquareAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer



class FamilysAPIView(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class TreesAPIView(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get_queryset(self):
        if self.kwargs.get('square_pk'):
            return self.queryset.filter(square_id=self.kwargs.get('square_pk'))
        return self.queryset.all()


class TreeAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get_object(self):
        if self.kwargs.get('square_pk'):
            return get_object_or_404(self.get_queryset(), 
            square_id=self.kwargs.get('square_pk'), pk=self.kwargs.get('tree_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('tree_pk'))


    """def get_object(self): #sobrescrevendo método
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))"""