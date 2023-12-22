import os
import random
import tkinter as tk


def generate_card(card_category):
    category_prefix = {
        "10": random.randint(0, 3),
        "50": random.randint(4, 6),
        "100": random.randint(7, 9),
    }

    prefix = str(category_prefix.get(card_category, 0))
    card_number = prefix + "".join(random.choices("0123456789", k=15))
    return card_number


def save_to_file(card_number, file_path):
    with open(file_path, "a") as file:
        file.write(card_number + "\n")


def generate_card_button_click():
    card_category = card_category_entry.get()

    if card_category not in ["10", "50", "100"]:
        result_label["text"] = "Invalid card category."
        return

    card_number = generate_card(card_category)
    result_label["text"] = f"Card Number: {card_number}"

    file_name = "generated_cards_all.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    save_to_file(card_number, file_path)


window = tk.Tk()
window.title("Card Generator")

card_category_label = tk.Label(window, text="Card Category (10, 50, 100):")
card_category_label.pack()

card_category_entry = tk.Entry(window)
card_category_entry.pack()

generate_card_button = tk.Button(
    window, text="Generate Card", command=generate_card_button_click
)
generate_card_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
