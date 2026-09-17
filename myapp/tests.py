from django.test import TestCase


class SumTestCase(TestCase):
	def test_sum_numbers(self):
		self.assertEqual(sum([1, 2, 3]), 6)

	def test_sum_empty_list(self):
		self.assertEqual(sum([]), 0)
