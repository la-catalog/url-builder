from url_builder.abstractions import Marketplace


class MercadoLivreAPI(Marketplace):
    def build_sku_url(self, code: str) -> str:
        return f"https://api.mercadolibre.com/items/{code}"

    def build_query_url(self, query: str) -> str:
        return f""
