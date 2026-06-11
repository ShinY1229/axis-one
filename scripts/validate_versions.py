#!/usr/bin/env python3
"""Validate public axis one GitHub kit version references."""
from pathlib import Path
import re
import sys
import yaml

EXPECTED_CORE = "0.2.3"
EXPECTED_BOOTLOADER = "1.2.3"
EXPECTED_STRUCTURE = "v3.16"
EXPECTED_WHITEPAPER = "v2.0"

CORE_MD = "axis_one_core_spec_lite_v0_2_3_2026_06_12.md"
CORE_YML = "axis_one_public_core_spec_v0_2_3_2026_06_12.yml"
WHITEPAPER_MD = "axis_one_whitepaper_EN_v2_0_2026_06_12.md"
RESEARCH_MD = "research_report_001_ai_as_conversational_tool.md"


def find_root() -> Path:
    here = Path(__file__).resolve()
    candidates = [here.parent.parent, here.parent, Path.cwd()]
    for c in candidates:
        if (c / "README.md").exists():
            return c
    return here.parent.parent

ROOT = find_root()

checks = {
    "README.md": [
        r"axis one is \*\*not\*\* a prompt library",
        rf"Core Spec Lite / Markdown\]\(core/{CORE_MD}\)",
        rf"Public Core Spec / YAML\]\(core/{CORE_YML}\)",
        rf"White Paper v2\.0 / English Markdown\]\(docs/{WHITEPAPER_MD}\)",
        rf"Research Report #001: AI as a Conversational Tool\]\(docs/{RESEARCH_MD}\)",
        r"Living Log Bootloader EN v1\.2\.3",
        r"AI-readable public surface",
        r"C-Recommendation note",
        r"experiments/convenience-rent/index\.html",
        r"Public working kit v0\.2\.3",
    ],
    f"core/{CORE_MD}": [
        rf"# axis one Core Spec Lite v{EXPECTED_CORE}",
        rf"Source: 構造定義書 {EXPECTED_STRUCTURE}",
        rf"White Paper: axis one White Paper {EXPECTED_WHITEPAPER}",
        r"AI-readable public surface",
        r"C-Recommendation",
    ],
    f"core/{CORE_YML}": [
        rf"version:\s*{re.escape(EXPECTED_CORE)}",
        rf"version:\s*{re.escape(EXPECTED_STRUCTURE)}",
        rf"version:\s*{re.escape(EXPECTED_WHITEPAPER)}",
        r"ai_readable_public_surface:",
        r"c_recommendation:",
        r"github_public_surface:",
    ],
    f"docs/{WHITEPAPER_MD}": [
        r"axis one White Paper v2\.0",
        r"Ghost Polish Thinking",
        r"C-mode",
    ],
    f"docs/{RESEARCH_MD}": [
        r"Research Report #001",
        r"AI as a Conversational Tool",
        r"Ghost / Shell / World",
        r"co-rendering",
    ],
    "bootloader/living_log_bootloader_EN_v1_2_3.md": [
        rf"v{EXPECTED_BOOTLOADER}",
        r"Document role",
        r"This bootloader is an entrance document",
    ],
    "experiments/convenience-rent/index.html": [
        r"axis one co-rendering prototype",
        rf"{CORE_MD}",
        rf"{CORE_YML}",
    ],
    "examples/c_recommendation_example.md": [
        r"C-Recommendation",
        r"Do not read only the genre",
    ],
}

failed = []
for rel, patterns in checks.items():
    path = ROOT / rel
    if not path.exists():
        failed.append(f"missing: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for pat in patterns:
        if not re.search(pat, text):
            failed.append(f"{rel}: pattern not found: {pat}")

# Ensure overview/condensed document is not part of GitHub initial docs.
overview_docs = list((ROOT / "docs").glob("*overview*")) + list((ROOT / "docs").glob("*condensed*")) + list((ROOT / "docs").glob("*gairyaku*"))
if overview_docs:
    failed.append("overview/condensed docs should not be included in docs/: " + ", ".join(str(p.relative_to(ROOT)) for p in overview_docs))

# YAML must parse.
try:
    yaml.safe_load((ROOT / f"core/{CORE_YML}").read_text(encoding="utf-8"))
except Exception as e:
    failed.append(f"YAML parse failed: {e}")

if failed:
    print("Version validation failed:")
    for item in failed:
        print(" -", item)
    sys.exit(1)

print(f"Version validation passed: core v{EXPECTED_CORE}, structure {EXPECTED_STRUCTURE}, bootloader v{EXPECTED_BOOTLOADER}")
