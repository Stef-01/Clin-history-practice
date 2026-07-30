#!/usr/bin/env python3
"""List differentials that fall back to the system template, most frequent first.

Use this to decide which DIFFERENTIAL_KB entries to write next.

Run:  python3 build/coverage.py
"""

import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build import SOURCE, build_case_practice  # noqa: E402


def main():
    src = open(SOURCE, encoding="utf-8").read()
    unmatched, total, matched = Counter(), 0, 0

    for sysm in re.finditer(
        r'<section class="source-system"(.*?)</section>\s*'
        r'(?=<section class="source-system"|</div>)', src, re.S
    ):
        block = sysm.group(0)
        system = re.search(r'data-name="([^"]+)"', block).group(1)
        for cm in re.finditer(r'<article class="case-card.*?</article>', block, re.S):
            _, entry = build_case_practice(cm.group(0), system)
            for t in entry["tabs"][1:]:
                total += 1
                if t.get("matched"):
                    matched += 1
                else:
                    unmatched[t["label"].lower()] += 1

    print("%d differential tabs / %d matched (%.0f%%) / %d unmatched (%d unique)\n"
          % (total, matched, 100.0 * matched / max(total, 1),
             total - matched, len(unmatched)))
    print("Unmatched, most frequent first:")
    for label, n in unmatched.most_common():
        print("  %2d  %s" % (n, label))


if __name__ == "__main__":
    main()
