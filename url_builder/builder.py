from pydantic import AnyHttpUrl
from structlog.stdlib import BoundLogger, get_logger

from url_builder.options import get_marketplace_builder


class Builder:
    """
    TODO
    """

    def __init__(self, logger: BoundLogger = get_logger()) -> None:
        self._logger = logger

    def build_sku_url(self, code: str, marketplace: str) -> str:
        builder = get_marketplace_builder(marketplace=marketplace, logger=self._logger)
        url = builder.build_sku_url(code=code)

        return url

    def build_query_url(self, query: str, marketplace: str) -> str:
        builder = get_marketplace_builder(marketplace=marketplace, logger=self._logger)
        url = builder.build_query_url(query=query)

        return url
