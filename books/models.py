from wagtail.admin.edit_handlers import FieldPanel
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
)
from coderedcms.blocks import HTML_STREAMBLOCKS
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from wagtailmarkdown.blocks import MarkdownBlock

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class BookPage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Página de libro"

    show_in_menus_default = True

    body = StreamField([('markdown', MarkdownBlock(icon="code"))] + HTML_STREAMBLOCKS, null=True, blank=True)

    promote_panels = [FieldPanel("show_in_menus")] + CoderedArticlePage.promote_panels

    parent_page_types = ["books.BookIndexPage", "books.BookPage"]

    subpage_types = ["books.BookPage"]

    #template = "books/pages/book_page.html"
    template = "coderedcms/pages/article_page.html"
    amp_template = "coderedcms/pages/article_page.amp.html"
    search_template = "coderedcms/pages/article_page.search.html"


class BookIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of book chapters.
    """

    class Meta:
        verbose_name = "Índice de libro"

    show_in_menus_default = True

    promote_panels = [FieldPanel("show_in_menus")] + CoderedArticlePage.promote_panels

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "books.BookPage"

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["books.BooksListingPage"]

    # Only allow ArticlePages beneath this page.
    subpage_types = ["books.BookPage"]

    template = "books/pages/book_chapters_index_page.html"


class BooksListingPage(CoderedArticleIndexPage):
    """
    Shows a list of books sub-pages.
    """

    class Meta:
        verbose_name = "Listado de libros de CATEDU"

    show_in_menus_default = True

    promote_panels = [FieldPanel("show_in_menus")] + CoderedArticlePage.promote_panels

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "books.BookIndexPage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["books.BookIndexPage"]

    template = "coderedcms/pages/article_index_page.html"