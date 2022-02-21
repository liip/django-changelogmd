from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView


class ChangelogMDView(TemplateView):
    template_name = "changelogmd/changelog.html"

    def get_changelog_path(self):
        return settings.CHANGELOG_MD_PATH

    def get_context_data(self, **kwargs):
        try:
            with open(self.get_changelog_path(), "r") as f:
                return {"changelog": f.read()}
        except FileNotFoundError:
            return {}


class AdminProtectedChangelogMDView(UserPassesTestMixin, ChangelogMDView):
    def test_func(self):
        return self.request.user.is_staff
