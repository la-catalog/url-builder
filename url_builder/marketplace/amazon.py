from pydantic import AnyHttpUrl

from url_builder.abstractions import Marketplace


class Amazon(Marketplace):
    def build_sku(self, code: str) -> AnyHttpUrl:
        return AnyHttpUrl(f"https://www.amazon.com.br/dp/{code}")

    def build_query(self, query: str) -> AnyHttpUrl:
        return AnyHttpUrl(f"https://www.amazon.com.br/s?k={query}")
