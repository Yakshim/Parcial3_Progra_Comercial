import graphene
from graphene_django import DjangoObjectType

#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual

import sys
sys.path.append("..")
from hotel.models import Hotel, Huesped


class HotelNode(DjangoObjectType):

    class Meta:
        model = Hotel
        fields = ("id", "name", "huesped")


class HuespedNode(DjangoObjectType):
    class Meta:
        model = Huesped
        fields = ("id", "name", "direccion", "correo", "telefono")


class Query(graphene.ObjectType):
    all_Huespedes = graphene.List(HuespedNode)
    Hotel_by_name = graphene.Field(HotelNode, name=graphene.String(required=True))

    def resolve_all_Huespedes(root, info):
      # We can easily optimize query count in the resolve method

        return Huesped.objects.select_related("Hotel").all()

    def resolve_HOtel_by_name(root, info, name):
        try:
            return Hotel.objects.get(name=name)
        except Hotel.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)