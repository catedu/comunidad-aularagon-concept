"""
Createable pages used in CodeRed CMS.
"""
from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage,
    CoderedPage,
)
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "coderedcms/pages/article_page.html"
    amp_template = "coderedcms/pages/article_page.amp.html"
    search_template = "coderedcms/pages/article_page.search.html"


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = "Article Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "coderedcms/pages/article_index_page.html"


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """

    class Meta:
        verbose_name = "Form"

    template = "coderedcms/pages/form_page.html"


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """

    page = ParentalKey("FormPage", related_name="confirmation_emails")


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existance.
    """

    class Meta:
        verbose_name = "Web Page"

    template = "coderedcms/pages/web_page.html"


class BookPage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Book Page"

    promote_panels = [FieldPanel("show_in_menus")] + ArticlePage.promote_panels

    parent_page_types = ["website.BookIndexPage", "website.BookPage"]

    subpage_types = ["website.BookPage"]

    template = "coderedcms/pages/book_page.html"


class BookIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of book chapters.
    """

    class Meta:
        verbose_name = "Book index Page"

    promote_panels = [FieldPanel("show_in_menus")] + ArticlePage.promote_panels

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.BookPage"

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.BooksListingPage"]

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.BookPage"]

    template = "coderedcms/pages/book_chapters_index_page.html"


class BooksListingPage(CoderedArticleIndexPage):
    """
    Shows a list of books sub-pages.
    """

    class Meta:
        verbose_name = "Books listing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.BookIndexPage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.BookIndexPage"]

    template = "coderedcms/pages/article_index_page.html"