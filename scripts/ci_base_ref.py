"""Resolve push/PR trusted commits; only an all-zero push permits HEAD-only checks."""

import argparse
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
ZERO = "0" * 40


def resolve_base(event, before="", pr_base="", root=ROOT, fetch=False):
    if event not in ("push", "pull_request"):
        raise ValueError(f"unsupported event for trusted checks: {event}")
    ref = before if event == "push" else pr_base
    if event == "push" and ref == ZERO:
        return None
    if not isinstance(ref, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", ref) or ref == ZERO:
        raise ValueError("event requires a nonzero full commit SHA")
    def resolve():
        return subprocess.run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    try:
        return resolve()
    except subprocess.CalledProcessError as exc:
        if not fetch:
            raise ValueError(f"nonzero trusted base unavailable: {ref}") from exc
        try:
            subprocess.run(["git", "fetch", "origin", ref], cwd=root, capture_output=True, text=True, check=True)
            return resolve()
        except subprocess.CalledProcessError as failure:
            raise ValueError(f"nonzero trusted base could not be fetched/resolved: {ref}") from failure


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", required=True)
    parser.add_argument("--before", default="")
    parser.add_argument("--pr-base", default="")
    parser.add_argument("--fetch", action="store_true", help="Fetch a missing nonzero SHA from origin, never fall back")
    args = parser.parse_args()
    try:
        base = resolve_base(args.event, args.before, args.pr_base, fetch=args.fetch)
        if base:
            print(base)
        else:
            print("All-zero push before SHA: no previous base; HEAD-only checks.", file=sys.stderr)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
