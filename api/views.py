from .models import CrudItem
from .serializers import CrudItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class CrudItemViewSet(viewsets.ModelViewSet):
	queryset = CrudItem.objects.all()
	serializer_class = CrudItemSerializer

	def perform_create(self, serializer):
		# Save instance to get primary key and then update URL
		instance = serializer.save()
		instance.url = reverse('cruditem-detail', args=[instance.pk], request=self.request)
		instance.save()

	# Deletes all todo items
	def delete(self, request):
		# CrudItem.objects.all().delete()
		# CrudItem.objects.get( completed=True).delete()
		CrudItem.objects.filter( completed=True).delete()
		return Response(status=status.HTTP_204_NO_CONTENT) 