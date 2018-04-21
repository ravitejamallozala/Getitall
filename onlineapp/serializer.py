from rest_framework import serializers
from models import Card, Tag

class CardSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(read_only=True,many=True)
    user_name=serializers.StringRelatedField(read_only=True,source="created_by.username")
    user_email=serializers.StringRelatedField(read_only=True,source="created_by.email")
    class Meta:
        model = Card
        fields = ('id', 'title', 'description','created_by','modified_time','tags','user_name','user_email')
class TagSerializer(serializers.ModelSerializer):
    card_title=serializers.StringRelatedField(read_only=True,source="card")
    class Meta:
        model=Tag
        fields=('id', 'tagname','card','card_title')