from datetime import datetime
import re

from playwright.sync_api import Page, expect  # type: ignore[import-not-found]
from tests.playwright.consts import FILE_PATH, REGISTRATION_FORM
from registration_page import RegistrationPage


def test_gmail(page: Page, request):