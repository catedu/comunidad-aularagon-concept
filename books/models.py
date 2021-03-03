from wagtail.admin.edit_handlers import FieldPanel
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
)

class BookPage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Book Page"

    promote_panels = [FieldPanel("show_in_menus")] + CoderedArticlePage.promote_panels

    parent_page_types = ["books.BookIndexPage", "books.BookPage"]

    subpage_types = ["books.BookPage"]

    template = "books/pages/book_page.html"


class BookIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of book chapters.
    """

    class Meta:
        verbose_name = "Book index Page"

    promote_panels = [FieldPanel("show_in_menus")] + CoderedArticlePage.promote_panels

    # Override to specify custom index ordering choice/default.
    # index_query_pagemodel = "books.BookPage"

    # Only allow this page to be created beneath an ArticleIndexPage.
    # parent_page_types = ["books.BooksListingPage"]

    # Only allow ArticlePages beneath this page.
    # subpage_types = ["books.BookPage"]

    template = "coderedcms/pages/book_chapters_index_page.html"


class BooksListingPage(CoderedArticleIndexPage):
    """
    Shows a list of books sub-pages.
    """

    class Meta:
        verbose_name = "Books listing Page"

    # Override to specify custom index ordering choice/default.
    # index_query_pagemodel = "books.BookIndexPage"

    # Only allow ArticlePages beneath this page.
    # subpage_types = ["books.BookIndexPage"]

    template = "coderedcms/pages/article_index_page.html"