import datetime

from django.utils import timezone
from django.urlresolvers import reverse
from django.test import TestCase

from polls.models import Question

def create_question(question_text, days):
	time = tiemzone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)
class QuestionViewTests(TestCase):
	def test_index_view_with_no_questions(self):
		"""
		If no questions exist, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_a_past_question(self):
		"""
		Questions with a pub_date in the past should be displayed on the
		index page
		"""
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
			)

	def test_index_view_with_a_future_question(self):
		"""
		Questions with a pub_date in the future should not be displayed on
		the index page.
		"""
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.",status_code=200)
		self.assertQuerysetEqual(response.context['latest_question_list'], [])