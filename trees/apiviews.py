from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets  # API V2
from rest_framework.decorators import action #API V2
from rest_framework.response import Response #API V2
from rest_framework import mixins

from rest_framework import permissions

from .models import Specie, Square, Family, Tree
from .serializers import SpecieSerializer, SquareSerializer, FamilySerializer, TreeSerializer, TreedetailSerializer
from .permissions import EhSuperUser


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


"""
 API V2 - Refatoração
 
"""

class SquareViewSet(viewsets.ModelViewSet):
    """
    API Arborização de Monte Alto - Exibindo as Praças
    """
    queryset = Square.objects.all()
    serializer_class = SquareSerializer

    @action(detail=True, methods=['get'])
    def arvores(self, request, pk=None):
        square = self.get_object()
        serializer =  TreedetailSerializer(square.trees.all(), many=True)
        return Response(serializer.data) 


#square = models.ForeignKey(Square, related_name="trees", on_delete=models.CASCADE)#Category

class SpecieViewSet(viewsets.ModelViewSet):
    """
    API Arborização de Monte Alto - Exibindo as espécies das árvores
    """
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    """
    API Arborização de Monte Alto - Exibindo as famílias das árvores
    """
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class TreeViewSet(
    mixins.ListModelMixin,   
    mixins.CreateModelMixin,  #post
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,   #put
    mixins.DestroyModelMixin,  #delete
    viewsets.GenericViewSet
    ):
    """
    API Arborização de Monte Alto - Exibindo as árvores com seus relacionamentos.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
"""
    forma de selecionar recursos da view. O ModelViewSet extende de todos os mixins.
    Reescrevendo dessa forma é possível selecionar qual extender
"""

"""class SquareViewSet(viewsets.ModelViewSet):

    permission_classes = (
        EhSuperUser, 
        permissions.DjangoModelPermissions,
        )
    # EhSuperUser => classe criada no arquivo permissions.py
    # DjangoModelPermissions => permissão local para essa view com DjangoModelPermissions /definidas no admin
    queryset = Square.objects.all()
    serializer_class = SquareSerializer

    @action(detail=True, methods=['get'])
    def trees(self, request, pk=None): #criando rota para trazer avaliações de um curso
        #implementação necessária/ não coberto pela paginção global no settings
        #self.pagination_class.page_size = 2 
        trees = Tree.objects.filter(Square_id=pk)
        page = self.paginate_queryset(trees)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)


        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response (serializer.data)
        

"""
class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer



