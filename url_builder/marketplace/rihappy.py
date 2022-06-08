from pydantic import AnyHttpUrl

from url_builder.abstractions import Marketplace


class Rihappy(Marketplace):
    def build_sku(self, code: str) -> AnyHttpUrl:
        return AnyHttpUrl(f"https://www.rihappy.com.br/{code}/p")

    def build_query(self, query: str) -> AnyHttpUrl:
        return AnyHttpUrl(f"https://www.rihappy.com.br/{query}")
