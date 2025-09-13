def tell_joke():
    joke_text = (
        "Here's something funny for you: Sophia went to the store. "
        "Her programmer friend said, 'Buy a liter of milk, and if they have eggs, pick up a dozen.' "
        "She comes back with 13 liters of milk. When asked why, she says, 'They had eggs!'"
    )
    return joke_text

def main():
    prompt = "Type 'joke' if you want to hear something funny: "
    response = input(prompt)
    if response.strip().lower() == 'joke':
        print(tell_joke())
    else:
        print("I can only share jokes, sorry!")

if __name__ == "__main__":
    main()