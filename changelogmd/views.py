from django.conf import settings
from django.views.generic import TemplateView


class ChangelogMDView(TemplateView):
    template_name = "changelogmd/changelog.html"

    def get_changelog_path(self):
        return settings.CHANGELOG_MD_PATH

    def get_context_data(self, **kwargs):
        try:
            with open(self.get_changelog_path(), "r") as f:
                return {"changelog": f.read()}
        except (AttributeError, FileNotFoundError):
            return {}
