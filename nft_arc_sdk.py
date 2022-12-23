import base64
import json

import algosdk

def mint_nft(name, description, image_url, address, private_key):
    # Create an instance of the Algorand SDK
    algod_client = algosdk.AlgodClient(
        token="<YOUR_TOKEN>",
        algod_address="<YOUR_ALGOD_ADDRESS>"
    )

    # Encode the NFT metadata as a JSON object
    nft_metadata = {
        "name": name,
        "description": description,
        "image_url": image_url
    }
    metadata_bytes = json.dumps(nft_metadata).encode()
    metadata_b64 = base64.b64encode(metadata_bytes).decode()

    # Get the current round and transaction parameters from the Algorand network
    current_round = algod_client.status().get("last-round")
    txn_params = algod_client.suggested_params(current_round, "").get("lastRound")

    # Create the Algorand transaction to mint the NFT
    txn = algosdk.transaction.AssetConfigTxn(
        sender=address,
        sp=txn_params,
        total_units=1,
        decimals=0,
        default_frozen=False,
        unit_name="",
        asset_name=name,
        asset_url="",
        asset_metadata_hash=metadata_b64
    )

    # Sign the transaction with the private key of the minting account
    signed_txn = txn.sign(private_key)

    # Send the transaction to the Algorand network
    txn_id = algod_client.send_transaction(signed_txn)
    print(f"NFT minted with ID: {txn_id}")

def update_nft_metadata(nft_id, name, description, image_url, address, private_key):
    # Create an instance of the Algorand SDK
    algod_client = algosdk.AlgodClient(
        token="<YOUR_TOKEN>",
        algod_address="<YOUR_ALGOD_ADDRESS>"
    )

    # Encode the updated NFT metadata as a JSON object
    nft_metadata = {
        "name": name,
        "description": description,
        "image_url": image_url
    }
    metadata_bytes = json.dumps(nft_metadata).encode()
    metadata_b64 = base64.b64encode(metadata_bytes).decode()

    # Get the current round and transaction parameters from the Algorand network
    current_round = algod_client.status().get("last-round")
    txn_params = algod_client.suggested_params(current_round, "").get("lastRound")

    # Create the Algorand transaction to update the NFT metadata
    txn = algosdk.transaction.AssetConfigTxn(
        sender=address,
