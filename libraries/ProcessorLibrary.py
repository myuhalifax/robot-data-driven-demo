"""Framework layer: Python keywords that drive the system under test.
In a real project this layer is written/maintained in Python;
test cases above it stay keyword + data only."""
import os, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ProcessorLibrary:
    def run_processor(self, data_file, run_name):
        outdir = os.path.join(BASE, "results", run_name)
        r = subprocess.run(
            [sys.executable, os.path.join(BASE, "app", "processor.py"),
             os.path.join(BASE, "data", data_file), outdir],
            capture_output=True, text=True)
        if r.returncode != 0:
            raise AssertionError(f"processor failed: {r.stderr}")
        return outdir

    def read_summary(self, outdir):
        d = {}
        with open(os.path.join(outdir, "summary.txt")) as f:
            for line in f:
                k, v = line.strip().split("=")
                d[k] = int(v)
        return d

    def read_log(self, outdir):
        with open(os.path.join(outdir, "app.log")) as f:
            return f.read()
