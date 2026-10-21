from django.test import TestCase, Client
from django.urls import reverse
from .models import SiteSetting, Question, Quality, Memory, LoveLetter
from datetime import date


class OurLittleWorldTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.setting = SiteSetting.objects.create(
            girlfriend_name="Sarah",
            partner_name="Alex",
            site_title="Our Little World ❤️",
            welcome_heading="A Special Place For Us",
            is_passcode_protected=False,
            passcode="sweetheart",
        )
        self.question = Question.objects.create(
            question_text="What is your favorite memory?",
            answer_text="Our rainy walk in the park.",
            display_order=1,
            is_active=True,
        )
        self.quality = Quality.objects.create(
            title="Your Kindness",
            description="You always bring joy to everyone around you.",
            icon="heart",
            display_order=1,
            is_active=True,
        )
        self.memory = Memory.objects.create(
            title="The Day We Met",
            date_display="A sunny Saturday",
            description="We bumped into each other and talked for hours.",
            display_order=1,
            is_active=True,
        )
        self.letter = LoveLetter.objects.create(
            title="My Heart in Words",
            salutation="Dearest Sarah,",
            content="You mean everything to me.",
            signature="Yours always ❤️",
            is_active=True,
        )

    def test_home_page_renders_successfully(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A Special Place For Us")
        self.assertContains(response, "Open My Heart")

    def test_dashboard_renders_questions(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is your favorite memory?")
        self.assertContains(response, "Our rainy walk in the park.")

    def test_qualities_page_renders(self):
        response = self.client.get(reverse("qualities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Kindness")

    def test_story_page_renders(self):
        response = self.client.get(reverse("story"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Day We Met")
        self.assertContains(response, "A sunny Saturday")

    def test_letter_page_renders(self):
        response = self.client.get(reverse("letter"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Heart in Words")
        self.assertContains(response, "Dearest Sarah,")

    def test_passcode_protection_redirect(self):
        # Enable passcode protection
        self.setting.is_passcode_protected = True
        self.setting.save()

        # Unauthenticated request to home should redirect to unlock page
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("unlock"), response.url)

        # Entering incorrect passcode fails
        post_response = self.client.post(reverse("unlock"), {"passcode": "wrong_code"})
        self.assertEqual(post_response.status_code, 200)
        self.assertContains(post_response, "That passcode didn&#x27;t match")

        # Entering correct passcode unlocks site
        unlock_response = self.client.post(reverse("unlock"), {"passcode": "sweetheart"})
        self.assertEqual(unlock_response.status_code, 302)
        self.assertEqual(unlock_response.url, reverse("home"))

        # Subsequent visit to home should succeed
        home_after_unlock = self.client.get(reverse("home"))
        self.assertEqual(home_after_unlock.status_code, 200)
