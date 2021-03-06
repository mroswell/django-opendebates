import urlparse

from django.contrib.sites.models import Site
from django.test import TestCase
from mock import patch, Mock

from opendebates.context_processors import global_vars
from opendebates.tests.factories import SubmissionFactory, SiteFactory, DebateFactory


class NumberOfVotesTest(TestCase):
    def setUp(self):
        self.site = SiteFactory()
        self.debate = DebateFactory(site=self.site)

    def tearDown(self):
        Site.objects.clear_cache()

    def test_number_of_votes(self):
        mock_request = Mock()
        mock_request.debate = DebateFactory(site=self.site)
        with patch('opendebates.context_processors.cache') as mock_cache:
            mock_cache.get.return_value = 2
            context = global_vars(mock_request)
            self.assertEqual(2, int(context['NUMBER_OF_VOTES']))


class ThemeTests(TestCase):
    def setUp(self):
        self.site = SiteFactory()
        self.debate = DebateFactory(site=self.site)

        self.idea = SubmissionFactory()

    def tearDown(self):
        Site.objects.clear_cache()

    def test_email_url(self):
        debate = self.idea.category.debate
        debate.email_subject = 'THE EMAIL SUBJECT'
        debate.email_body = 'THE EMAIL BODY\nAND SECOND LINE'
        debate.save()
        email_url = self.idea.email_url()
        fields = urlparse.parse_qs(urlparse.urlparse(email_url).query)
        self.assertTrue('subject' in fields, fields)
        self.assertEqual('THE EMAIL SUBJECT', fields['subject'][0], fields['subject'][0])
        self.assertEqual('THE EMAIL BODY\nAND SECOND LINE', fields['body'][0], fields['body'][0])
