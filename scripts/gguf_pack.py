#!/usr/bin/env python3
import json, argparse, hashlib, pathlib, time

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(1<<20)
            if not b: break
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Path to .gguf")
    ap.add_argument("--out", default="model-packs/manifest.json")
    ap.add_argument("--name", default="LocalModel")
    ap.add_argument("--license", default="")
    args = ap.parse_args()

    p = pathlib.Path(args.model)
    info = {
        "name": args.name,
        "license": args.license,
        "file": str(p),
        "size_bytes": p.stat().st_size,
        "sha256": sha256(p),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    outp = pathlib.Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)
    print(f"Wrote manifest to {outp}")

if __name__ == "__main__":
    main()
