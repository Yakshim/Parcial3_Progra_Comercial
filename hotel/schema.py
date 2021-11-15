import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from hotel.models import Hotel, Huesped


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class HotelNode(DjangoObjectType):
    class Meta:
        model = Hotel
        filter_fields = ['name', 'Huesped']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class HuespedNode(DjangoObjectType):
    class Meta:
        model = Huesped
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'direccion': ['exact', 'icontains', 'istartswith'],
            'correo': ['exact', 'icontains', 'istartswith'],
            'telefono': ['exact', 'icontains', 'istartswith'],
            'Hotel': ['exact'],
            'Hotel__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    Hotel = relay.Node.Field(HotelNode)
    all_Hoteles = DjangoFilterConnectionField(HotelNode)

    Huesped = relay.Node.Field(HuespedNode)
    all_Huespedes = DjangoFilterConnectionField(HuespedNode)