import json
import requests
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def parse_Popular():
    try:
        url = "https://popularenlinea.com/_api/web/lists/getbytitle('Rates')/items"
        headers = {"Accept": "application/json; odata=verbose"}
        response = requests.get(url, headers=headers, timeout=10)
        json_data = json.loads(response.text)
        tasas = json_data["d"]["results"][0]

        EURCompra = tasas["EuroBuyRate"]
        EURVenta = tasas["EuroSellRate"]
        USDCompra = tasas["DollarBuyRate"]
        USDVenta = tasas["DollarSellRate"]
        print(EURVenta, end='\n')
        print(EURCompra, end='\n')
        print(USDVenta, end='\n')
        print(USDCompra, end='\n')
    except Exception:
        pass


def parse_Banreservas():
    try:
        url = "https://www.banreservas.com/_layouts/15/SharePointAPI/ObtenerTasas.ashx"
        response = requests.get(url, timeout=10)
        json_data = json.loads(response.text)
        EURCompra = json_data["compraEU"]
        EURVenta = json_data["ventaEU"]
        USDCompra = json_data["compraUS"]
        USDVenta = json_data["ventaUS"]
        print(EURVenta, end='\n')
        print(EURCompra, end='\n')
        print(USDVenta, end='\n')
        print(USDCompra, end='\n')
    except Exception:
        pass


def parse_BHD():
    try:
        url = "https://backend.bhd.com.do/api/modal-cambio-rate?populate=deep"
        response = requests.get(url, verify=False, timeout=10)
        json_data = json.loads(response.text)
        tasas = json_data["data"]["attributes"]["exchangeRates"]

        EURCompra = tasas[1]["buyingRate"]
        EURVenta = tasas[1]["sellingRate"]
        USDCompra = tasas[0]["buyingRate"]
        USDVenta = tasas[0]["sellingRate"]
        print(EURVenta, end='\n')
        print(EURCompra, end='\n')
        print(USDVenta, end='\n')
        print(USDCompra, end='\n')
    except Exception:
        pass


def parse_SantaCruz():
    try:
        url = "https://bsc.com.do/api/gql"
        transport = AIOHTTPTransport(url=url)
        client = Client(transport=transport, fetch_schema_from_transport=False, execute_timeout=10)

        query = gql("""
    query getCalculators {
        calculators {
            other {
                foreign_exchange {
                    usd {
                        buy
                        sale
                        title
                    }
                    eur {
                        buy
                        sale
                        title
                    }
                }
            }
        }
    }""")

        result = client.execute(query)
        tasas = result["calculators"]["other"]["foreign_exchange"]
        EURCompra = tasas["eur"]["buy"]
        EURVenta = tasas["eur"]["sale"]
        USDCompra = tasas["usd"]["buy"]
        USDVenta = tasas["usd"]["sale"]
        print(EURVenta, end='\n')
        print(EURCompra, end='\n')
        print(USDVenta, end='\n')
        print(USDCompra, end='\n')
    except Exception:
        pass


if __name__ == '__main__':
    # parse_Popular()
    # parse_Banreservas()
    # parse_BHD()
    parse_SantaCruz()
