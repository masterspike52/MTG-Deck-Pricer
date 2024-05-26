import tkinter as tk
import requests

def calculate_pricing():
    deck_list = deck_entry.get("1.0", tk.END).strip()
    card_prices = {}

    for card_name in deck_list.split("\n"):
        card_data = get_card_data(card_name)
        if card_data is not None and "prices" in card_data:
            card_price = card_data["prices"].get("usd")
            if card_price is not None:
                card_prices[card_data["name"]] = float(card_price)

    total_price = sum(card_prices.values())
    pricing_label.config(text=f"Deck Pricing: ${total_price:.2f}")
    

def get_card_data(card_name):
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)
    data = response.json()
    return data

root = tk.Tk()
root.title("Deck Pricing Tool")

deck_label = tk.Label(root, text="Enter your deck list:")
deck_label.pack()

deck_entry = tk.Text(root, height=10, width=50)
deck_entry.pack()

calculate_button = tk.Button(root, text="Calculate Pricing", command=calculate_pricing)
calculate_button.pack()

pricing_label = tk.Label(root, text="")
pricing_label.pack()

root.mainloop()