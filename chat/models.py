from django.db import models


# Create your models here.


class Chat(models.Model):
    # user1 = models.ForeignKey('users.User', null=True, related_name='chats.1', on_delete=models.SET_NULL)
    # user2 = models.ForeignKey('users.User', null=True, related_name='chats.2', on_delete=models.SET_NULL)

    name = models.CharField('Name', max_length=100, null=True)
    users = models.ManyToManyField('users.User', related_name='chats',  blank=True)
    is_group = models.BooleanField('Is group', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_group:
            return f'{self.name} - {self.id}'
        return f'PRIVATE - {self.id}'


class Message(models.Model):
    text = models.TextField('Text')
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    sender = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    read_date = models.DateTimeField('Read date', auto_now_add=True)

    def __str__(self):
        return f'{self.chat_id}'
