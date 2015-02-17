from data_api.serializers import ThreadSerializer, DoomMapSerializer
from rest_framework import viewsets
import boto.dynamodb
from boto.dynamodb2.table import Table, Item
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from boto.dynamodb.condition import EQ
from rest_framework.decorators import detail_route
from rest_framework import renderers

class DoomMap(viewsets.ModelViewSet):


    conn=boto.connect_dynamodb()
    table=conn.get_table("doom_map")
    serializer_class = DoomMapSerializer

    def list(self, request, *args, **kwargs):
        items=self.table.scan()
        data=items.response['Items']
        return Response(data)

    def create(self, request, *args, **kwargs):
        """
        Función POST para agregar una nueva entrada en la base de datos
        """

        table= Table('doom_map')
        author = Item(table, data={'episode': int(self.request.data['episode']),'map': int(self.request.data['map']),'name': self.request.data['name'], 'cheats': self.request.data['cheats']})
        author.save()
        result = self.table.query(hash_key=int(self.request.data['episode']), range_key_condition=GT(0))
        data = result.response['Items']
        return  Response(data)

class DoomMapDetails(viewsets.ModelViewSet):


    conn=boto.connect_dynamodb()
    table=conn.get_table("doom_map")
    serializer_class = DoomMapSerializer

    def retrieve(self, request, pk=None):
        """
        Retornar un elemento
        """
        data = self.table.query(hash_key=int(pk), range_key_condition=EQ(3))
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        """
        Eliminar un elemento de base de datos
        """

    def update(self, request, *args, **kwargs):
        """
        Actualizar un elemento en base de datos
        """

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

class Thread(viewsets.ModelViewSet):


    conn=boto.connect_dynamodb()
    table=conn.get_table("Thread")
    serializer_class = ThreadSerializer

    def list(self, request, *args, **kwargs):
        items=self.table.scan()
        data=items.response['Items']
        return Response(data)

    def create(self, request, *args, **kwargs):
        """
        Función POST para agregar una nueva entrada en la base de datos
        """
        tabla= Table('Thread')
        author = Item(tabla, data={'forum_name': self.request.data['forum_name'],'subject': self.request.data['subject'],'views': self.request.data['views'], 'replies': self.request.data['replies']})
        author.save()

        result = self.table.query(hash_key=self.request.data['forum_name'])
        data = result.response['Items']
        print(data)
        return  Response(data)

class ThreadDetails(viewsets.ModelViewSet):


    conn=boto.connect_dynamodb()
    table=conn.get_table("Thread")
    serializer_class = ThreadSerializer

    def retrieve(self, request, pk=None):
        """
        Retornar un elemento
        """
        data = self.table.query(hash_key=pk)
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        """
        Eliminar un elemento de base de datos
        """

    def update(self, request, *args, **kwargs):
        """
        Actualizar un elemento en base de datos
        """
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'doom_map': reverse('doom_map', request=request, format=format),
        'thread': reverse('thread', request=request, format=format)
    })
