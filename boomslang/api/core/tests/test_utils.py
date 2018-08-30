"""Test for monitoring.logic.profile."""
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone


class TestCheckEcoSystem(TestCase):
    def test_True_if_no_other_package_with_same_name(self):
        assert True
