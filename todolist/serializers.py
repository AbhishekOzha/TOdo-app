from rest_framework import serializers
from .models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = TodoItem
        fields = ['id', 'user', 'title', 'description', 'completed', 'due_date', 'comments', 'created_at']
