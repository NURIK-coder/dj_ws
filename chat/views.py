from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from chat.models import Chat
from chat.serializers import ChatSerializer


# Create your views here.


class CreateChatAPiView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer