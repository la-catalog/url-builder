from url_builder.abstractions import Marketplace


class AmazonPT(Marketplace):
    def build_sku_url(self, code: str) -> str:
        return f"https://www.amazon.es/-/pt/dp/{code}"

    def build_query_url(self, query: str) -> str:
        return f"https://www.amazon.es/s?k={query}"
