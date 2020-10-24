from rest_framework import serializers

from core.models import List, Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "list", "url", "done"]


class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ["name", "owner", "url", "item_set"]
