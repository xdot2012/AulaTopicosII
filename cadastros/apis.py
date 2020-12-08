import requests
from rest_framework import generics, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


from cadastros.models import Pessoa
from cadastros.serializers import PessoaSerializer, PessoaCreateSerializer, PessoaDeleteSerializer


class PrincipalAPI(generics.ListAPIView):

    queryset = Pessoa.objects.filter()
    serializer_class = PessoaSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):

        
        try:
            queryset = self.get_queryset().filter()
            serializer = PessoaSerializer(queryset, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PessoaPostAPI(generics.CreateAPIView):

    queryset = Pessoa.objects.filter()
    serializer_class = PessoaCreateSerializer


    def post(self, request, *args, **kwargs):

        nome = request.data.get('nome', None)
        profissao = request.data.get('profissao', None)
        endereco = request.data.get('endereco', None)
        numero = int(request.data.get('numero', None))
        date = request.data.get('date')

        try:
            obj = Pessoa.objects.create(
                nome = nome,
                profissao = profissao,
                endereco = endereco,
                numero = int(numero),
                date = date,
            )
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)



class PessoaDeleteAPI(generics.DestroyAPIView):

    queryset = Pessoa.objects.filter()
    serializer_class = PessoaDeleteSerializer
    permission_classes = (permissions.AllowAny,)


    def delete(self, request, *args, **kwargs):

        id = request.data.get('id', None)
        pessoa_delete = Pessoa.objects.get(pk=int(id))
        
        try:
            pessoa_delete.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)
        
        

