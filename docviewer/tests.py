from django.test import TestCase


class TestDocviewerForms(TestCase):

    def test_docviewer_documents(self) -> None:
        response = self.client.post(
            "/doc/doc_upload/",
            data={
                "title": "some-title",
                "description": "a long meaningful description",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            "/doc/doc_view",
        )
