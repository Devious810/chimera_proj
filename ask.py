from gpt4all import GPT4All

# Usa QUI il filename esatto
model = GPT4All(model_name="Phi-3-mini-4k-instruct.Q4_0.gguf", allow_download=True)

# Lancia subito la richiesta
resp = model.generate("Spiegami come fare una titolazione base", max_tokens=150)
print(resp)
