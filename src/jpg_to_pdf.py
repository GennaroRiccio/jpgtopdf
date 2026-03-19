"""
jpg_to_pdf.py - Unisce tutti i file JPG di una cartella in un unico PDF.

Utilizzo:
    python jpg_to_pdf.py <cartella_input> <file_output.pdf>

Esempio:
    python jpg_to_pdf.py ./immagini output.pdf
"""

import os
import re
import sys
from pathlib import Path

from PIL import Image


def jpg_to_pdf(input_folder: str, output_pdf: str) -> None:
    folder = Path(input_folder)
    if not folder.is_dir():
        print(f"Errore: la cartella '{input_folder}' non esiste.")
        sys.exit(1)

    jpg_files = sorted(
        (f for f in folder.iterdir() if f.suffix.lower() in (".jpg", ".jpeg")),
        key=lambda x: [
            int(c) if c.isdigit() else c for c in re.split(r"(\d+)", x.stem)
        ],
    )

    if not jpg_files:
        print(f"Nessun file JPG trovato in '{input_folder}'.")
        sys.exit(1)

    print(f"Trovati {len(jpg_files)} file JPG:")
    for f in jpg_files:
        print(f"  {f.name}")

    images = []
    for f in jpg_files:
        img = Image.open(f).convert("RGB")
        images.append(img)

    first, rest = images[0], images[1:]
    first.save(output_pdf, save_all=True, append_images=rest)
    print(f"\nPDF creato: {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizzo: python jpg_to_pdf.py <cartella_input> <file_output.pdf>")
        sys.exit(1)

    jpg_to_pdf(sys.argv[1], sys.argv[2])
