import asyncio

from httpclient.domain.brand.providers import TemplateProvider
from httpclient.http_client_factory import create_async_client, create_client

TILLO_HOST = ''
TILLO_API_KEY = ''
TILLO_SECRET = ''
TILL_HTTP_CLIENT_OPTIONS = {}

def get_brand_template(**kwargs):
    tillo_client = create_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILL_HTTP_CLIENT_OPTIONS,
    )

    query = TemplateProvider.get_template(**kwargs)
    provider = TemplateProvider(tillo_client)
    templates = provider.get_template(query)

    return templates


get_brand_template()


async def get_brand_template_async(**kwargs):
    tillo_async_client = create_async_client(
        TILLO_HOST,
        TILLO_API_KEY,
        TILLO_SECRET,
        **TILL_HTTP_CLIENT_OPTIONS,
    )

    query = TemplateProvider.get_template(**kwargs)
    provider = TemplateProvider(tillo_async_client)
    templates = await provider.get_template_async(query)

    return templates



asyncio.run(get_brand_template_async())
