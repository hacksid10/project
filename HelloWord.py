def fancy_hello():
    message = "Hello, World!"
    border = '*' * (len(message) + 4)
    print(border)
    print(f"* {message} *")
    print(border)

fancy_hello()