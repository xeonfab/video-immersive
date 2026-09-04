#!/usr/bin/env python3
"""Add or update a prospect row in projects/prospects.csv.

Usage:
    python3 update_tracker.py --hotel "Castel Beau Site" --contact "Jean Dupont" \\
        --role "Directeur Général" --email jean@castel.fr --statut contacte \\
        --date-premier-contact 2026-09-04 --notes "Envoyé email initial"

Only --hotel is required; omitted fields keep their existing value (or blank on
first creation). Matching is done on the hotel name (case-insensitive).
"""
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
TRACKER = ROOT / "projects" / "prospects.csv"
FIELDS = [
    "hotel", "contact", "role", "email", "statut",
    "date_premier_contact", "date_derniere_relance", "notes",
]


def load_rows() -> list[dict]:
    if not TRACKER.exists():
        return []
    with TRACKER.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(rows: list[dict]) -> None:
    TRACKER.parent.mkdir(parents=True, exist_ok=True)
    with TRACKER.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hotel", required=True)
    parser.add_argument("--contact")
    parser.add_argument("--role")
    parser.add_argument("--email")
    parser.add_argument("--statut")
    parser.add_argument("--date-premier-contact", dest="date_premier_contact")
    parser.add_argument("--date-derniere-relance", dest="date_derniere_relance")
    parser.add_argument("--notes")
    args = parser.parse_args()

    rows = load_rows()
    match = next(
        (r for r in rows if r["hotel"].strip().lower() == args.hotel.strip().lower()),
        None,
    )
    if match is None:
        match = {field: "" for field in FIELDS}
        match["hotel"] = args.hotel
        rows.append(match)

    for field in FIELDS[1:]:
        value = getattr(args, field, None)
        if value:
            match[field] = value

    save_rows(rows)
    print(f"Tracker mis à jour : {TRACKER}")
    print(match)


if __name__ == "__main__":
    main()
