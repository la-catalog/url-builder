from structlog.stdlib import BoundLogger

from url_builder.abstractions import Marketplace
from url_builder.exceptions import UnknowMarketplaceError
from url_builder.marketplaces.amazon import Amazon, AmazonPT
from url_builder.marketplaces.rihappy import Rihappy

options: dict[Marketplace] = {
    "rihappy": Rihappy,
    "amazon": Amazon,
    "amazon_pt": AmazonPT,
}


def get_marketplace_builder(marketplace: str, logger: BoundLogger) -> Marketplace:
    try:
        log = logger.bind(marketplace=marketplace)
        return options[marketplace](log)
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in url_builder"
        ) from e
