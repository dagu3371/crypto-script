from fastapi import FastAPI
import requests
import csv

app = FastAPI()

@app.get("/fetch-address-data/{address}")
def get_transaction_by_hash(address: str):
    api_url = f'https://blockchain.info/rawaddr/{address}'
    try:
        response = requests.get(api_url)
        crypto_data = response.json()
        if crypto_data:
            write_to_csv(crypto_data)
            print("CSV file 'crypto_address_info.csv' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_to_csv(data, output_filename='crypto_info.csv'):
    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ["hash160", "address", "n_tx", "n_unredeemed", "total_received", "total_sent", "final_balance", "txs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        data = {
            key: value if key != "txs" else None for key, value in data.items()
        }

        writer.writerow(data)