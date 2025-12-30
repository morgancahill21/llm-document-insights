from pathlib import Path

def load_document(path: str) -> str:
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"{path} not found")

    if file_path.suffix == ".txt":
        return file_path.read_text(encoding="utf-8")

    else: # could try to implement other file types later
        raise ValueError("Unsupported file type")
