from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSetting, Question, Quality, Memory, LoveLetter


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("girlfriend_name", "partner_name", "site_title", "is_passcode_protected", "preview_featured_photo")
    fieldsets = (
        ("Personalization", {
            "fields": ("girlfriend_name", "partner_name", "site_title", "relationship_start_date")
        }),
        ("Home Page Content", {
            "fields": ("welcome_heading", "welcome_subtitle", "welcome_message", "featured_photo", "featured_caption")
        }),
        ("Privacy & Passcode Lock", {
            "fields": ("is_passcode_protected", "passcode", "passcode_hint"),
            "description": "If enabled, guests must enter this sweet secret passcode to explore the site."
        }),
    )

    def has_add_permission(self, request):
        # Only allow 1 singleton settings instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def preview_featured_photo(self, obj):
        if obj.featured_photo:
            return format_html('<img src="{}" style="height: 45px; border-radius: 6px; object-fit: cover;" />', obj.featured_photo.url)
        return "No photo"
    preview_featured_photo.short_description = "Photo Preview"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "display_order", "is_active", "preview_image", "created_at")
    list_editable = ("display_order", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("question_text", "answer_text")
    ordering = ("display_order", "created_at")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; border-radius: 6px; object-fit: cover;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Photo"


@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "display_order", "is_active", "preview_image")
    list_editable = ("display_order", "is_active", "icon")
    list_filter = ("is_active", "icon")
    search_fields = ("title", "description")
    ordering = ("display_order", "title")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; border-radius: 6px; object-fit: cover;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Photo"


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ("title", "display_date", "display_order", "is_active", "preview_image")
    list_editable = ("display_order", "is_active")
    list_filter = ("is_active", "date")
    search_fields = ("title", "description", "date_display")
    ordering = ("display_order", "date")

    def display_date(self, obj):
        return obj.formatted_date
    display_date.short_description = "Date"

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; border-radius: 6px; object-fit: cover;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Photo"


@admin.register(LoveLetter)
class LoveLetterAdmin(admin.ModelAdmin):
    list_display = ("title", "salutation", "signature", "is_active", "preview_image", "updated_at")
    list_editable = ("is_active",)
    list_filter = ("is_active", "updated_at")
    search_fields = ("title", "content", "salutation", "signature")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 45px; border-radius: 6px; object-fit: cover;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Photo"
