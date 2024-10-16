from django.urls import path

from chat.views import CreateChatAPiView

urlpatterns= [
    path('create/', CreateChatAPiView.as_view())
]