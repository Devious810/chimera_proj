import os, pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_split(path):
    reader = PdfReader(path)
    # estrae il testo da ogni pagina (gestisce anche pagine vuote)
    pages = []
    for p in reader.pages:
        txt = p.extract_text() or ""
        pages.append(txt)
    full = "\n".join(pages)
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(full)

def main():
    chunks, sources = [], []
    for fn in os.listdir("docs"):
        if fn.lower().endswith(".pdf"):
            path = os.path.join("docs", fn)
            for chunk in load_and_split(path):
                chunks.append(chunk)
                sources.append(fn)

    # Costruiamo il TF‑IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(chunks)

    # Salviamo tutto
    with open("faiss_index.pkl", "wb") as f:
        pickle.dump({
            "vectorizer": vectorizer,
            "matrix": X,
            "chunks": chunks,
            "sources": sources
        }, f)
    print("Indicizzazione TF‑IDF completata.")

if __name__ == "__main__":
    main()
