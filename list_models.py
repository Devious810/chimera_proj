from gpt4all import GPT4All

def main():
    models = GPT4All.list_models()
    for m in models:
        print(m)      # mostriamo l’intera struttura

if __name__ == "__main__":
    main()
