from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CrudItem

# Create your tests here.
def createItem(client):
  url = reverse('cruditem-list')
  data = {'text': 'Walk the dog'}
  return client.post(url, data, format='json')

class TestCreateCrudItem(APITestCase):
  """
  Ensure we can create a new crud item
  """
  def setUp(self):
    self.response = createItem(self.client)

  def test_received_201_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_received_location_header_hyperlink(self):
    self.assertRegexpMatches(self.response['Location'], '^http://.+/tasks/[\d]+$')

  def test_item_was_created(self):
    self.assertEqual(CrudItem.objects.count(), 1)

  def test_item_has_correct_text(self):
    self.assertEqual(CrudItem.objects.get().text, 'Walk the dog')

class TestUpdateCrudItem(APITestCase):
  """
  Ensure we can update an existing crud item using PUT
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(CrudItem.objects.get().completed, False)
    url = response['Location']
    data = {'text': 'Walk the dog', 'completed': True}
    self.response = self.client.put(url, data, format='json')

  def test_received_200_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def test_item_was_updated(self):
    self.assertEqual(CrudItem.objects.get().completed, True)

class TestPatchCrudItem(APITestCase):
  """
  Ensure we can update an existing crud item using PATCH
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(CrudItem.objects.get().completed, False)
    url = response['Location']
    data = {'text': 'Walk the dog', 'completed': True}
    self.response = self.client.patch(url, data, format='json')

  def test_received_200_ok_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def test_item_was_updated(self):
    self.assertEqual(CrudItem.objects.get().completed, True)

class TestDeleteCrudItem(APITestCase):
  """
  Ensure we can delete a crud item
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(CrudItem.objects.count(), 1)
    url = response['Location']
    self.response = self.client.delete(url)

  def test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def test_the_item_was_deleted(self):
    self.assertEqual(CrudItem.objects.count(), 0)

class TestDeleteCompletedItems(APITestCase):
  """
  Ensure we can delete completed crud items
  """
  def setUp(self):
    createItem(self.client)
    createItem(self.client)
    self.assertEqual(CrudItem.objects.count(), 2)
    self.response = self.client.delete(reverse('cruditem-list'))

  def test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def test_completed_items_were_deleted(self):
    self.assertEqual(CrudItem.objects.count(), 0)