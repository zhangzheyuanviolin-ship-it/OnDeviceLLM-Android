#!/usr/bin/env python3
import csv, json, argparse

ap = argparse.ArgumentParser()
ap.add_argument("--csv", default="benches/prompts.csv")
ap.add_argument("--out", default="model-packs/prompts.json")
args = ap.parse_args()

rows = []
with open(args.csv, newline='', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows.append(r)
with open(args.out, "w", encoding="utf-8") as wf:
    json.dump(rows, wf, indent=2, ensure_ascii=False)
print(f"Wrote {len(rows)} prompts to {args.out}")
