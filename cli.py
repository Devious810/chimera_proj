import os
import pickle
from sklearn.metrics.pairwise import linear_kernel
from gpt4all import GPT4All

# --- Caricamento indice TF‑IDF ---
with open("faiss_index.pkl", "rb") as f:
    idx = pickle.load(f)
vectorizer = idx["vectorizer"]
matrix     = idx["matrix"]
chunks     = idx["chunks"]
sources    = idx["sources"]

# --- Caricamento modello offline ---
model = GPT4All(model_name="Phi-3-mini-4k-instruct.Q4_0.gguf", allow_download=False)

def clear_screen():
    """Pulisce lo schermo del terminale."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_from_file(lang, fname):
    path = os.path.join("prompts", lang, fname)
    try:
        with open(path, encoding="utf-8") as f:
            prompt = f.read().strip()
            print("[DEBUG] Prompt letto:", prompt)
    except FileNotFoundError:
        print(f"File non trovato: {path}")
        return
    resp = model.generate(prompt, n_predict=200)
    print("\n→ " + resp + "\n")
    # ———> aggiungi questa riga per mettere in pausa
    input("Premi Invio per tornare al menu..." if lang=="it" else "Press Enter to return to menu...")

def choose_language():
    print("Scegli la lingua / Choose language:")
    print("1) Italiano")
    print("2) English")
    choice = input("Digita 1 o 2: ").strip()
    return "it" if choice == "1" else "en"

def menu(lang):
    if lang == "it":
        print("1) Titolazione base")
        print("2) Montare un distillatore")
        print("3) Analisi proteine")
        print("4) Primo soccorso (ferita)")
        print("5) Cerca nei PDF")
        print("6) Esci")
        return input("Scegli: ").strip()
    else:
        print("1) Basic titration")
        print("2) Distillation apparatus")
        print("3) Protein analysis")
        print("4) First aid (cut)")
        print("5) Search in PDFs")
        print("6) Exit")
        return input("Choose: ").strip()

if __name__ == "__main__":
    lang = choose_language()
    while True:
        clear_screen()                
        c = menu(lang)

        if c == "1":
            ask_from_file(lang, "titolazione.txt")
        elif c == "2":
            ask_from_file(lang, "distillatore.txt")
        elif c == "3":
            ask_from_file(lang, "proteine.txt")
        elif c == "4":
            ask_from_file(lang, "primosoccorso.txt")
        elif c == "5":
            q = input("Query: " if lang == "it" else "Enter query: ").strip()
            if not q:
                print("Nessuna query inserita, riprova." if lang == "it" else "No query entered, please try again.")
                input("Premi Invio per continuare..." if lang == "it" else "Press Enter to continue...")
                continue

            qvec = vectorizer.transform([q])
            sims = linear_kernel(qvec, matrix).flatten()
            topk = sims.argsort()[-3:][::-1]

            rag_prompt = ("Ecco alcuni estratti dai miei documenti:\n\n" if lang=="it"
                          else "Here are some excerpts from my documents:\n\n")
            for idx in topk:
                rag_prompt += f"Fonte: {sources[idx]}\n{chunks[idx]}\n\n"
            rag_prompt += (f"Domanda: {q}\nRispondi facendo riferimento a questi estratti.\n"
                           if lang=="it" else
                           f"Question: {q}\nPlease answer referring to the excerpts above.\n")

            resp = model.generate(rag_prompt, n_predict=300)
            print("\n→ " + resp + "\n")
            input("Premi Invio per continuare..." if lang == "it" else "Press Enter to continue...")
        elif c == "6":
            break
        else:
            print("Scelta non valida." if lang == "it" else "Invalid choice.")
            input("Premi Invio per continuare..." if lang == "it" else "Press Enter to continue...")

    print("Ciao!" if lang == "it" else "Bye!")
