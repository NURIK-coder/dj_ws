from django.core.exceptions import BadRequest
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from chat.models import Chat
from users.models import User



class ChatSerializer(serializers.ModelSerializer):
    user_id = serializers.ImageField(write_only=True)
    class Meta:
        model = Chat
        fields = ['id', 'user_id']

    def create(self, validated_data):

        user = get_object_or_404(User, id=validated_data['user_id'])
        if not user.is_active:
            raise PermissionDenied
        request_user = self.context['request'].user
        if Chat.objects.filter(Q(users=user.id)&Q(users=request_user.id)&Q(is_group=False)).exists():
            raise BadRequest

        chat = Chat.objects.create()
        chat.users.add()