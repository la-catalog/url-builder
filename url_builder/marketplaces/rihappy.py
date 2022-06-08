from url_builder.abstractions import Marketplace


class Rihappy(Marketplace):
    def build_sku_url(self, code: str) -> str:
        return f"https://www.rihappy.com.br/{code}/p"

    def build_query_url(self, query: str) -> str:
        return f"https://www.rihappy.com.br/{query}"
