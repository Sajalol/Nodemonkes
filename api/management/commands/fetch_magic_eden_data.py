# api/management/commands/fetch_magic_eden_data.py
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Fetch data from Magic Eden API'

    def fetch_collection_data(self):
        url = "https://api-mainnet.magiceden.dev/v2/ord/btc/collections/nodemonkes"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors
            return None

    def fetch_collection_stats(self):
        url = "https://api-mainnet.magiceden.dev/v2/ord/btc/stat?collectionSymbol=nodemonkes"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors
            return None
    
    def fetch_token_data(self, token_ids, collection_symbol, sort_by='priceAsc', show_all=True):
        url = f"https://api-mainnet.magiceden.dev/v2/ord/btc/tokens?tokenIds={token_ids}&collectionSymbol={collection_symbol}&showAll={show_all}&sortBy={sort_by}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print("Token Data Response:", response.text)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors
            return None

    def handle(self, *args, **kwargs):
        collection_data = self.fetch_collection_data()
        collection_stats = self.fetch_collection_stats()

        if collection_data:
            # Process and save your collection data here
            print("Collection Data:", collection_data)
            self.stdout.write(self.style.SUCCESS('Successfully fetched collection data'))

        if collection_stats:
            # Process and save your collection stats here
            print("Collection Stats:", collection_stats)
            self.stdout.write(self.style.SUCCESS('Successfully fetched collection stats'))

        token_data = self.fetch_token_data('7034', 'nodemonkes')
        if token_data:
            print("Token Data:", token_data)
        self.stdout.write(self.style.SUCCESS('Successfully fetched token data'))

