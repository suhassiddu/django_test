from rest_framework import serializers
from .models import CrudItem

class CrudItemSerializer( serializers.HyperlinkedModelSerializer):
	url = serializers.ReadOnlyField()
	class Meta:
		model = CrudItem
		fields = ( 'id', 'url', 'text', 'completed')