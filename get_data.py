import requests
from time import sleep
from datetime import date
import boto3
import csv
import os

def get_cards(data, url):
    print("Getting cards from Scryfall")
    res = requests.get(url)
    res = res.json()
    if "next_page" in res:
        sleep(1/10)
        return get_cards(data + res["data"], res["next_page"])
    return data + res["data"]

def write_prices_to_csv(prices, filename):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=prices[0].keys())
        writer.writeheader()
        for row in prices:
            writer.writerow(row)
        

def upload_to_s3(bucket, filename):
    print("Uploading to S3")
    s3_client = boto3.client('s3')
    s3_client.upload_file(filename, bucket, filename)

def get_image(card):
    image_uris = card.get("image_uris")
    if image_uris:
        return card["image_uris"]["normal"]
    if card.get("card_faces"):
        return card["card_faces"][0]["image_uris"]["normal"]

def nicify_cards(cards):
    return [{
        "uri": card["uri"],
        "name": card["name"],
        "usd": card["prices"]["usd"],
        "usd_foil": card["prices"]["usd_foil"],
        "tix": card["prices"]["tix"],
        "collector_number": card["collector_number"],
        "image": get_image(card),
    } for card in cards]

def main():
    sld_url = "https://api.scryfall.com/cards/search?order=set&q=e%3Asld&unique=prints"
    cards = get_cards([], sld_url)
    print("Found {}".format(len(cards)))
    nice_cards = nicify_cards(cards)
    today = date.today()
    last_updated_date = today.strftime("%Y-%m-%d")
    file_name = f'{last_updated_date}-sld.csv'
    write_prices_to_csv(nice_cards, file_name)
    upload_to_s3('mtgcollector', file_name)

def lambda_handler(event, context):
    os.chdir('/tmp')
    main()

if __name__ == "__main__":
    main()

