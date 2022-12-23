# nft_arc_sdk

NFT ARC SDK for minting and updating Algorand NFTs using the Python programming language:

First, we will need to install the necessary dependencies:

>pip install algosdk

Next, we can define a function for minting a new NFT on the Algorand blockchain. This function will take several arguments as input, including the NFT metadata (such as the name, description, and image URL), the address of the account that will be minting the NFT, and the private key of the account.

##Code Start From Here##

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
    
    ##Code End Here##
    
We can then define a function for updating the metadata of an existing NFT on the Algorand blockchain. This function will take the same arguments as the minting function, as well as the ID of the NFT that we want to update.

##Code Start From Here##

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
        "image


##Code End Here##

Open The nft_arc_sdk.py to see all the code together.
