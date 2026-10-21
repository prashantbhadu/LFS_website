import os
from django.core.management.base import BaseCommand
from love_site.models import SiteSetting, Question, Quality, Memory, LoveLetter
from datetime import date


class Command(BaseCommand):
    help = "Seeds romantic placeholder data for Our Little World"

    def handle(self, *args, **options):
        self.stdout.write("Seeding romantic data...")

        # 1. Site Setting
        setting, _ = SiteSetting.objects.get_or_create(id=1)
        setting.girlfriend_name = "My Sweetheart"
        setting.partner_name = "Yours Forever"
        setting.site_title = "Our Little World ❤️"
        setting.welcome_heading = "A Little World Made Just for You ❤️"
        setting.welcome_subtitle = "Every little corner of this world holds a piece of my heart and memories of you."
        setting.welcome_message = "Welcome to our special place. I made this little corner of the internet just for you—to remind you of how deeply you are loved, to celebrate the moments we cherish, and to give you a smile whenever you need one."
        setting.featured_caption = "The sweetest smile in my entire universe 🌸"
        if os.path.exists(os.path.join("media", "featured", "sample_couple.jpg")):
            setting.featured_photo = "featured/sample_couple.jpg"
        setting.relationship_start_date = date(2023, 10, 14)  # Sample anniversary
        setting.is_passcode_protected = False  # Disabled by default so it's instantly browsable
        setting.passcode = "love"
        setting.passcode_hint = "Hint: Our secret word (default is 'love') ❤️"
        setting.save()

        # 2. Questions
        sample_questions = [
            (
                "When did you first become special to me?",
                "It wasn't just a single grand thunderbolt—it was a series of gentle moments. The way you listened so attentively when I talked about things I cared about, and that effortless laugh you gave that made everything else fade into the background. That was the moment I knew my heart was in your hands.",
                1
            ),
            (
                "What is my favorite memory with you?",
                "One of my absolute favorites is that quiet evening when we sat together talking about everything and nothing at all. Time felt like it had completely stopped, and for the first time in forever, I felt completely at home.",
                2
            ),
            (
                "What makes your smile so special?",
                "Your smile has this genuine, radiant warmth that immediately softens any hard day. It reaches all the way to your eyes and creates little crinkles that I find endlessly adorable. It's my favorite view in the world.",
                3
            ),
            (
                "What do I miss most when you're not around?",
                "I miss your gentle presence—your spontaneous laughter, the way you reach for my hand, and how even silence feels comfortable and sweet whenever you're beside me.",
                4
            ),
            (
                "Which moment with you would I love to relive?",
                "I would love to relive the very first time we realized we both had feelings for each other. That electric mix of nervousness, joy, and butterflies is something I will treasure forever.",
                5
            ),
            (
                "What is something about you that always makes me happy?",
                "How genuinely you care about the people around you, and how your eyes light up whenever you talk about something you're excited about. Seeing you genuinely happy is my favorite feeling.",
                6
            ),
        ]

        for q_text, a_text, order in sample_questions:
            Question.objects.update_or_create(
                question_text=q_text,
                defaults={
                    "answer_text": a_text,
                    "display_order": order,
                    "is_active": True,
                }
            )

        # 3. Qualities
        sample_qualities = [
            (
                "Your Beautiful Smile",
                "It lights up any room you walk into and has this comforting way of making whatever stress I have instantly disappear.",
                "smile",
                1
            ),
            (
                "Your Endless Kindness",
                "You treat everyone with so much warmth, empathy, and patience. Your heart is one of the purest things I have ever known.",
                "heart",
                2
            ),
            (
                "Your Contagious Laugh",
                "Your laugh is genuine and musical. Hearing you laugh is honestly the quickest shortcut to making my whole day better.",
                "music",
                3
            ),
            (
                "The Way You Understand Me",
                "You have a rare ability to understand what I'm feeling even before I find the right words to say it out loud.",
                "star",
                4
            ),
            (
                "Your Caring Nature",
                "The thoughtful questions you ask, the way you check in on me, and how deeply you look after the things and people you love.",
                "flower",
                5
            ),
            (
                "The Happiness You Bring Into My Life",
                "Before you, life was good; with you, life is vibrant, rich, and full of color. You make every day something to look forward to.",
                "sun",
                6
            ),
            (
                "The Little Things You Do",
                "The sweet expressions you make, the little habits you have when you're thinking, and all the quiet moments you make special without even trying.",
                "butterfly",
                7
            ),
        ]

        for title, desc, icon, order in sample_qualities:
            Quality.objects.update_or_create(
                title=title,
                defaults={
                    "description": desc,
                    "icon": icon,
                    "display_order": order,
                    "is_active": True,
                }
            )

        # 4. Memories / Timeline
        sample_memories = [
            (
                "How We First Met",
                "The day our paths crossed for the very first time. I had no idea back then that you were about to become the most important part of my everyday life.",
                "The First Hello",
                1
            ),
            (
                "Our First Conversation",
                "We started talking, and an hour felt like two minutes. I remember walking away with this silly grin on my face, wondering how someone could be so effortlessly charming.",
                "Where the Spark Began",
                2
            ),
            (
                "When We Started Talking Regularly",
                "Checking my phone became my favorite hobby because seeing your name on my screen never failed to make my heart skip a beat.",
                "Everyday Magic",
                3
            ),
            (
                "The Moment We Became Closer",
                "We shared stories, vulnerabilities, and things we don't easily tell others. In that moment, comfort turned into a deep, unbreakable trust.",
                "A Turning Point",
                4
            ),
            (
                "Our Funniest Memory Together",
                "That time we couldn't stop laughing until our stomachs hurt over something that probably wouldn't make sense to anyone else. Those pure moments are my treasures.",
                "Pure Joy & Laughter",
                5
            ),
            (
                "Important Milestones in Our Journey",
                "All the small steps: our first official date, celebrating small victories together, and learning each other's favorite coffee orders and quirks.",
                "Growing Together",
                6
            ),
            (
                "Where We Are Today",
                "Looking back at how far we have come makes me so grateful. You are my best friend, my confidante, and my favorite part of every tomorrow.",
                "Forever & Always",
                7
            ),
        ]

        for title, desc, date_disp, order in sample_memories:
            Memory.objects.update_or_create(
                title=title,
                defaults={
                    "description": desc,
                    "date_display": date_disp,
                    "display_order": order,
                    "is_active": True,
                }
            )

        # 5. Love Letter
        sample_content = (
            "If someone asked me to describe you in a few words, I would tell them that you are the gentlest sunlight on a cloudy morning, and the calmest harbor in a stormy sea.\n\n"
            "From the moment you came into my life, you brought a softness and a warmth that I didn't even realize I was missing. You have this magical gift of making everything feel lighter, kinder, and full of hope. When you laugh, the entire world seems to stop and smile along with you.\n\n"
            "Thank you for being my peace, my partner in laughter, and my favorite thought before falling asleep. No matter where life takes us, I promise to always listen to you, stand by you, and remind you every single day of how extraordinary you are.\n\n"
            "This little world is just a small token of all the love and admiration I hold for you in my heart."
        )

        LoveLetter.objects.update_or_create(
            id=1,
            defaults={
                "title": "What I Feel for You 💌",
                "salutation": "To My Dearest Love,",
                "content": sample_content,
                "signature": "With all my love, forever & always ❤️",
                "is_active": True,
            }
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded romantic data for Our Little World!"))
