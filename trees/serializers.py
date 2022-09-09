from rest_framework import serializers

from .models import Specie, Square, Family, Tree


class SquareSerializer(serializers.ModelSerializer):
    
    class Meta:
        #extra_Kwargs = { para ocultar algum campo }
        model = Square
        fields = (
            'id',
            'name',
            'address',
            'description'
        )

class SpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specie
        fields = (
            'id',
            'name',
            'description'
        )


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = (
            'id',
            'name',
        )

class TreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        fields = (
            'id',
            'name',
            'specie',
            'family',
            'square',
            'source',
            'description',
            'quantidade'
        )

