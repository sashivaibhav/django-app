
# from web_project.bootstrap import TemplateBootstrap
from web_project.template_helpers.theme import TemplateHelper


class TemplateLayout:
    # Initialize the bootstrap files and page layout
    def init(self, context):
        # Init the Template Context using TEMPLATE_CONFIG
        context = TemplateHelper.init_context(context)
        # Set a default layout globally using settings.py. Can be set in the page level view file as well.
        layout = context["layout"]

        # Set the selected layout
        context.update(
            {
                "layout_path": TemplateHelper.set_layout(
                    "layout_blank.html", context
                ),
                # Set default rtl True if the language Arabic else use rtl_mode value from TEMPLATE_CONFIG
                "rtl_mode": True
                if self.request.LANGUAGE_CODE == "ar"
                else TemplateHelper.get_theme_config("rtl_mode"),
            }
        )

        # Map context variables
        TemplateHelper.map_context(context)

        return context