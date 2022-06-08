from url_builder.abstractions import Marketplace


class Amazon(Marketplace):
    def build_sku_url(self, code: str) -> str:
        return f"https://www.amazon.com.br/dp/{code}"

    def build_query_url(self, query: str) -> str:
        return f"https://www.amazon.com.br/s?k={query}"
