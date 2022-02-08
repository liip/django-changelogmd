from django.conf import settings
from django.views.generic import TemplateView

n_apps = tuple(list(settings.INSTALLED_APPS) + ['markdownify.apps.MarkdownifyConfig'])

# settings.configure(INSTALLED_APPS=n_apps,
#                    MARKDOWNIFY={
#                     "default": {
#                         "WHITELIST_TAGS": [
#                             "a",
#                             "p",
#                             "h1",
#                             "h2",
#                             "h3",
#                             "h4",
#                             "h5",
#                             "h6",
#                             "h7",
#                             "ul",
#                             "li",
#                             "strong",
#                             "span",
#                         ]
#                     }
#                    })


class ChangelogMDView(TemplateView):
    template_name = "changelogmd/changelog.html"

    def get_context_data(self, **kwargs):
        try:
            with open(settings.CHANGELOG_MD_PATH, "r") as f:
                return {"changelog": f.read()}
        except (AttributeError, FileNotFoundError):
            return {}
