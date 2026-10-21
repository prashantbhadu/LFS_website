from django.db import models


class SiteSetting(models.Model):
    """
    Singleton model to hold customizable romantic titles, girlfriend name,
    optional passcode lock, and anniversary countdown.
    """
    girlfriend_name = models.CharField(
        max_length=100,
        default="My Love",
        help_text="Name or nickname of your girlfriend shown in greetings."
    )
    partner_name = models.CharField(
        max_length=100,
        default="Yours Truly",
        help_text="Your name or signature sign-off."
    )
    site_title = models.CharField(
        max_length=150,
        default="Our Little World ❤️",
        help_text="Title shown in browser tab and navbar."
    )
    welcome_heading = models.CharField(
        max_length=200,
        default="A Little World Made Just for You ❤️",
        help_text="Large romantic heading on the home page."
    )
    welcome_subtitle = models.CharField(
        max_length=300,
        default="Every little corner of this world holds a piece of my heart and memories of you.",
        help_text="Subtitle on the home page."
    )
    welcome_message = models.TextField(
        default="Welcome to a safe haven built out of all the smiles, conversations, and butterflies you've given me. Here is our story, the reasons you make my world glow, and the words I hold closest to my heart.",
        help_text="Heartfelt opening message on the landing page."
    )
    featured_photo = models.ImageField(
        upload_to="featured/",
        blank=True,
        null=True,
        help_text="Featured Polaroid photograph for the home page."
    )
    featured_caption = models.CharField(
        max_length=200,
        default="The smile that makes every ordinary day feel extraordinary 🌸",
        blank=True,
        help_text="Caption beneath the featured home Polaroid."
    )
    relationship_start_date = models.DateField(
        blank=True,
        null=True,
        help_text="Optional anniversary date to show a live 'Days of Loving You' counter."
    )
    is_passcode_protected = models.BooleanField(
        default=False,
        help_text="Enable a romantic secret passcode lock before entering the website."
    )
    passcode = models.CharField(
        max_length=50,
        default="love",
        blank=True,
        help_text="Secret password to unlock (e.g., anniversary date, nickname, or special word)."
    )
    passcode_hint = models.CharField(
        max_length=200,
        default="Hint: Our special word or secret ❤️",
        blank=True,
        help_text="Gentle hint displayed on the passcode lock screen."
    )

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Settings for {self.girlfriend_name}"

    @classmethod
    def get_settings(cls):
        try:
            obj, created = cls.objects.get_or_create(id=1)
            return obj
        except Exception:
            return cls(id=1)


class Question(models.Model):
    """
    Questions about the couple, displayed as interactive reveal cards on the Dashboard.
    """
    question_text = models.CharField(
        max_length=300,
        verbose_name="Romantic Question",
        help_text="e.g. 'When did you first become special to me?'"
    )
    answer_text = models.TextField(
        verbose_name="Personal Answer",
        help_text="The heartfelt answer revealed when she clicks the question."
    )
    image = models.ImageField(
        upload_to="questions/",
        blank=True,
        null=True,
        verbose_name="Associated Photograph (Optional)",
        help_text="Displayed alongside or under the answer."
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name="Display Order",
        help_text="Lower numbers appear first."
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active (Visible)",
        help_text="Uncheck to hide this question without deleting it."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "created_at"]
        verbose_name = "Question & Answer"
        verbose_name_plural = "Questions & Answers"

    def __str__(self):
        return self.question_text


class Quality(models.Model):
    """
    Things and qualities you adore about her.
    """
    ICON_CHOICES = [
        ("heart", "Heart (💖)"),
        ("smile", "Warm Smile (✨)"),
        ("flower", "Sweet Flower (🌸)"),
        ("star", "Bright Star (⭐)"),
        ("sun", "Warm Sunshine (☀️)"),
        ("butterfly", "Butterfly (🦋)"),
        ("cloud", "Comforting Softness (☁️)"),
        ("music", "Melody & Laughter (🎵)"),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="Quality Title",
        help_text="e.g. 'Your Beautiful Smile', 'Your Endless Kindness'"
    )
    description = models.TextField(
        verbose_name="Heartfelt Description",
        help_text="Express what this quality means to you."
    )
    icon = models.CharField(
        max_length=20,
        choices=ICON_CHOICES,
        default="heart",
        verbose_name="Decorative Icon"
    )
    image = models.ImageField(
        upload_to="qualities/",
        blank=True,
        null=True,
        verbose_name="Optional Photo",
        help_text="A cute picture that represents this quality."
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name="Display Order",
        help_text="Lower numbers appear first."
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active (Visible)"
    )

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name = "Quality I Love"
        verbose_name_plural = "Qualities I Love"

    def __str__(self):
        return self.title


class Memory(models.Model):
    """
    Chronological relationship timeline milestones and special memories.
    """
    title = models.CharField(
        max_length=250,
        verbose_name="Milestone Title",
        help_text="e.g. 'How We First Met', 'Our First Coffee Walk'"
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Milestone Date (Optional)",
        help_text="If exact date is known."
    )
    date_display = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Custom Date / Period",
        help_text="e.g. 'Autumn 2023' or 'A magical rainy Tuesday' (used if date is empty or for extra flavor)"
    )
    description = models.TextField(
        verbose_name="Story / Memory Details",
        help_text="What happened, what made it special, how you felt."
    )
    image = models.ImageField(
        upload_to="memories/",
        blank=True,
        null=True,
        verbose_name="Memory Photo (Optional)",
        help_text="A snapshot of this precious moment."
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name="Display Order",
        help_text="Order in chronological timeline (e.g. 1, 2, 3...)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active (Visible)"
    )

    class Meta:
        ordering = ["display_order", "date", "id"]
        verbose_name = "Timeline Milestone"
        verbose_name_plural = "Timeline Milestones"

    def __str__(self):
        return self.title

    @property
    def formatted_date(self):
        if self.date_display:
            return self.date_display
        if self.date:
            return self.date.strftime("%B %d, %Y")
        return "A Cherished Moment"


class LoveLetter(models.Model):
    """
    Personal Love Letter page.
    """
    title = models.CharField(
        max_length=200,
        default="What I Feel for You 💌",
        verbose_name="Letter Heading"
    )
    salutation = models.CharField(
        max_length=150,
        default="To My Dearest Love,",
        verbose_name="Salutation",
        help_text="Opening line (e.g. 'To My Dearest Love,')"
    )
    content = models.TextField(
        verbose_name="Love Letter Content",
        help_text="Your sincere letter. Paragraphs and line breaks are supported."
    )
    signature = models.CharField(
        max_length=200,
        default="Forever and always with all my love ❤️",
        verbose_name="Romantic Signature"
    )
    image = models.ImageField(
        upload_to="letters/",
        blank=True,
        null=True,
        verbose_name="Photo Beside Letter (Optional)",
        help_text="A favorite photograph together."
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Love Letter"
        verbose_name_plural = "Love Letters"

    def __str__(self):
        return self.title
