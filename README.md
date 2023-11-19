# The Exercise
The purpose of this exercise is to write a script in Python that takes a crypto address hash and output a CSV. I am using blockchain api in the background to fetch the information for the given address.

### Local build
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Endpoints
## Fetch data for address and create a csv
This endpoint makes a requests to blockchain api and creates a csv with the output data
```
curl http://localhost:8000/fetch-address-data/{address}
```

Blockchain api information can be found here https://www.blockchain.com/explorer/api/blockchain_api

https://blockchain.info/rawaddr/$bitcoin_address
Address can be base58 or hash160
Optional limit parameter to show n transactions e.g. &limit=50 (Default: 50, Max: 50)
Optional offset parameter to skip the first n transactions e.g. &offset=100 (Page 2 for limit 50)
```
{
  "hash160": "660d4ef3a743e3e696ad990364e555c271ad504b",
  "address": "1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F",
  "n_tx": 17,
  "n_unredeemed": 2,
  "total_received": 1031350000,
  "total_sent": 931250000,
  "final_balance": 100100000,
  "txs": [
    "--Array of Transactions--"
  ]
}
```

## Nice to haves
- Processing of individual transactions data for the csv
- Find another api to get more on-chain information
- Caching and rate limiting to make sure we don't get throttled by the api