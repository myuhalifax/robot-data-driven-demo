#!/usr/bin/env python3
"""Fake 'system under test': a small sonar-like contact processor.
Reads ping data (CSV), classifies each ping, writes a summary + a log file.
Stands in for a real system: data in -> processing -> outputs + logs out.
Usage: python3 processor.py <input.csv> <output_dir>
"""
import csv, os, sys

def classify(strength):
    if strength >= 70: return "CONTACT"
    if strength >= 40: return "WEAK"
    return "NOISE"

def main():
    src, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    counts = {"CONTACT": 0, "WEAK": 0, "NOISE": 0}
    logs = [f"INFO processor started, input={os.path.basename(src)}"]
    with open(src, newline="") as f:
        for row in csv.DictReader(f):
            try:
                s = float(row["signal_strength"])
            except (KeyError, TypeError, ValueError):
                logs.append(f"ERROR bad row skipped: {row}")
                continue
            label = classify(s)
            counts[label] += 1
            logs.append(f"INFO ping {row.get('ping_id','?')} range={row.get('range_m','?')} -> {label}")
    if counts["CONTACT"] == 0:
        logs.append("WARN no contacts detected in this run")
    with open(os.path.join(outdir, "summary.txt"), "w") as f:
        for k in ("CONTACT", "WEAK", "NOISE"):
            f.write(f"{k}={counts[k]}\n")
    with open(os.path.join(outdir, "app.log"), "w") as f:
        f.write("\n".join(logs) + "\n")
    print(f"done: {counts}")

if __name__ == "__main__":
    main()
