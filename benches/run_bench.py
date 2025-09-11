import csv, time, argparse, random, pathlib
from datetime import datetime

def simulate_latency(tokens:int)->float:
    # crude simulator: 15 tok/s baseline +/- jitter
    rate = 15.0 + random.uniform(-3,3)
    return tokens / max(rate, 1e-3)

def run(prompts_path:str, quant:str, device:str, out_csv:str):
    start = time.time()
    rows = []
    with open(prompts_path, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            tokens = 100 if r['task']=='chat' else 60
            lat = simulate_latency(tokens)
            time.sleep(0.02)  # tiny pause to keep it quick
            rows.append({
                "ts": datetime.utcnow().isoformat(),
                "id": r["id"],
                "task": r["task"],
                "quant": quant,
                "device": device,
                "tokens": tokens,
                "latency_s": round(lat, 3),
                "tok_per_s": round(tokens/lat, 2)
            })
    # write
    out = pathlib.Path(out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    import csv as _csv
    with open(out, "w", newline="", encoding="utf-8") as wf:
        w = _csv.DictWriter(wf, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    dur = time.time() - start
    print(f"Wrote {len(rows)} rows to {out} in {dur:.2f}s")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompts", default="prompts.csv")
    ap.add_argument("--quant", default="Q4_K_M")
    ap.add_argument("--device", default="Snapdragon-8-Gen-3")
    ap.add_argument("--out", default="results/results.csv")
    args = ap.parse_args()
    run(args.prompts, args.quant, args.device, args.out)
