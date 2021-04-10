import pytest

from django.test import TestCase
from docviewer.models import document_files, documents
from http import HTTPStatus


class TestDocviewerForms(TestCase):
  @pytest.mark.parameterize(
    "title, description",
    [
      ("Gone-Teaser", "Rose first single"),
      ("Blackpink", "Is the revolution"),
    ]
  )
  def test_docviewer_documents(self) -> None:
    response = self.client.post(
      '/doc/doc_upload/', data={
        'title': "some-title",
        'description': "a long meaningful description",
      }
    )

    self.assertEqual(response.status_code, 302)
    self.assertEqual(
        response.url, '/doc/doc_view',
    )
