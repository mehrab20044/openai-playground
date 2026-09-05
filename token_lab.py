import tiktoken


encoding = tiktoken.get_encoding("o200k_base")

texts = [
    "Hello, how are you?",
    "سلام، حالت چطوره؟",
    "I love Python programming.",
    "من برنامه نویسی پایتون را دوست دارم.",
]

for text in texts:
    tokens = encoding.encode(text)

    token_pieces = [
        encoding.decode([token_id])
        for token_id in tokens
    ]

    print("Text:")
    print(text)

    print("Tokens:")
    print(tokens)

    print("Token pieces:")
    print(token_pieces)

    print("Token count:")
    print(len(tokens))

    print("-" * 40)