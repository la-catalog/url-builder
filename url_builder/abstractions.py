from pydantic import AnyHttpUrl


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, logger) -> None:
        self._logger = logger

    def build_sku(self, code: str) -> AnyHttpUrl:
        """
        Not every marketplace use the SKU code in the URL.
        While this gives you a potential URL for the SKU,
        it can't be sure as each marketplace can use a
        different code in the URL.

        If you don't have the SKU code but knows the
        text that needs to be used in the URL, you can
        pass it instead.
        """

        return AnyHttpUrl("https://thiagola92.github.io/")

    def build_query(self, query: str) -> AnyHttpUrl:
        """Build the URL for a query in the marketplace"""

        return AnyHttpUrl("https://thiagola92.github.io/")
