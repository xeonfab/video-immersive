#!/usr/bin/env python3
"""Scaffold a new hotel project folder from projects/_template.

Usage:
    python3 scripts/new_project.py "Castel Beau Site"
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slugify(name: str) -> str:
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 scripts/new_project.py "Nom de l\'hôtel"')
        sys.exit(1)

    hotel_name = sys.argv[1]
    slug = slugify(hotel_name)
    dest = ROOT / "projects" / slug

    if dest.exists():
        print(f"Le projet existe déjà : {dest}")
        sys.exit(1)

    template = ROOT / "projects" / "_template"
    shutil.copytree(template, dest)

    config_path = dest / "config.yaml"
    example = ROOT / "templates" / "config.example.yaml"
    text = example.read_text(encoding="utf-8")
    text = text.replace('nom: "Nom de l\'hôtel"', f'nom: "{hotel_name}"')
    text = text.replace('slug: "nom-de-lhotel"', f'slug: "{slug}"')
    config_path.write_text(text, encoding="utf-8")

    print(f"Projet créé : {dest}")
    print(f"→ Complète {config_path} puis lance /shotlist-generator")


if __name__ == "__main__":
    main()
