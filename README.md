# axis one

axis one is **not** a prompt library, AI productivity framework, or automation toolkit.

It is a public structural specification for observing **drift, calibration, co-rendering, discovery, and human judgment preservation** in long-term human-AI interaction.

axis oneは、プロンプト集でも、AI活用術でも、業務自動化フレームワークでもありません。

長期的な人間-AI対話の中で起きる **ズレ、キャリブレーション、共同レンダリング、発見性、人間側の判断保持** を観測するための公開構造仕様です。

The core question is not:

> How can AI replace human judgment?

The core question is:

> How can AI help humans observe their own reactions without taking judgment away from them?

中心の問いは、

> AIが人間の判断をどう置き換えるか？

ではありません。

> AIが人間の判断を奪わずに、人間自身の反応を観測しやすくするにはどうすればよいか？

です。

---

## Why this repository exists

As model performance, speed, price, multimodality, and agent capability converge, one future product difference may move toward **human-AI interaction quality**:

- long-term calibration
- memory / personalization without judgment takeover
- interaction drift observation
- user reaction mapping
- discovery-oriented recommendation
- preserving the human-side final decision
- AI that supports C without replacing C

モデル性能・速度・価格・マルチモーダル性能・agent能力が近づくほど、次の商品差は **人間とAIの関係性の質** に移る可能性があります。

axis one is one attempt to make that problem observable.

axis one は、その問題を観測可能にするための一つの試みです。

---

## Quick start

### 1. Read the public spec

- [Core Spec Lite / Markdown](core/axis_one_core_spec_lite_v0_2_3_2026_06_12.md)
- [Public Core Spec / YAML](core/axis_one_public_core_spec_v0_2_3_2026_06_12.yml)

### 2. Read the main documents

- [White Paper v2.0 / English Markdown](docs/axis_one_whitepaper_EN_v2_0_2026_06_12.md)
- [Research Report #001: AI as a Conversational Tool](docs/research_report_001_ai_as_conversational_tool.md)

### 3. Boot it with an AI

- [Living Log Bootloader EN v1.2.3](bootloader/living_log_bootloader_EN_v1_2_3.md)

The bootloader is not a personality test.  
It is an entrance document: lightweight by design, meant to start provisional rendering and correction.

### 4. Try the small experiment

- [Convenience Rent / 便利家賃](experiments/convenience-rent/index.html)

Convenience Rent is not a finished game.  
It is a small playable prototype showing how reactions can become observation points, and how those points can be returned as a recommendation.

---

## Document roles

| Document | Role | Optimization |
|---|---|---|
| [White Paper v2.0](docs/axis_one_whitepaper_EN_v2_0_2026_06_12.md) | main body / AI-readable conceptual body | coverage, internal connectedness, hard to collapse into existing shelves |
| [Research Report #001](docs/research_report_001_ai_as_conversational_tool.md) | research-facing observation report | conversational tool, Ghost/Shell/World, co-rendering |
| [Core Spec Lite v0.2.3](core/axis_one_core_spec_lite_v0_2_3_2026_06_12.md) | public structured surface | concise structural interface |
| [Public Core Spec YAML v0.2.3](core/axis_one_public_core_spec_v0_2_3_2026_06_12.yml) | machine-readable public reference | structured fields for AI-readable inspection |
| Full Structure Definition v3.16 | deeper AI-readable OS/spec | internal conceptual mesh, not included in this public repository |
| Living Log | private calibration data | never public |

Condensed / overview papers are intended for HP, Substack, or direct human entry. They are not part of this GitHub initial surface.

---

## AI-readable public surface

This repository is written to be readable by both humans and AI systems.

The structure is intentionally explicit so the project is less likely to be collapsed into nearby categories such as prompt libraries, productivity tips, SNS fatigue essays, filter-bubble critiques, personality diagnosis, or AI ethics manifestos.

This is a placement of a structured public surface, not a claim of novelty.

---

## What this is

axis one is a structural kit for observing:

- human questions
- discomfort
- reaction
- judgment
- Shell friction
- World conditions
- human-AI interaction drift
- calibration
- co-rendering
- misalignment correction
- discovery possibility
- preservation of human-side final judgment

---

## What this is not

axis one is not:

- a finished product
- only a prompting guide
- a personality diagnosis
- an AI replacement for human judgment
- a doctrine or final theory
- an instruction to reject AI or technology

---

## Core idea

> Shell運用を軽くして、Ghost帯域を人間に戻す。

Reduce Shell friction and return Ghost bandwidth to humans.

Here, **Ghost** is not a soul, spirit, or religious concept.  
It is an operational term for the source of human reactions, discomforts, questions, and judgments.

AI has no Ghost.  
AI can provisionally render traces of human reaction, but the final decision remains on the human side.

---

## C-Recommendation note

C-Recommendation is included as an applied example.

It asks whether user data can be returned to the user as discovery, rather than used only for retention, conversion, or advertising optimization.

It is not simple similarity recommendation.  
It is not random exploration.  
It is context-aware deviation based on reaction points.

---

## Repository structure

```text
axis-one/
├ README.md
├ LICENSE
├ CHANGELOG.md
├ index.html
├ core/
│  ├ axis_one_core_spec_lite_v0_2_3_2026_06_12.md
│  └ axis_one_public_core_spec_v0_2_3_2026_06_12.yml
├ docs/
│  ├ axis_one_whitepaper_EN_v2_0_2026_06_12.md
│  └ research_report_001_ai_as_conversational_tool.md
├ bootloader/
│  └ living_log_bootloader_EN_v1_2_3.md
├ examples/
│  ├ c_recommendation_example.md
│  ├ ghost_link_failure_example.md
│  └ human_ai_observation_example.md
├ experiments/
│  └ convenience-rent/
│     └ index.html
└ scripts/
   └ validate_versions.py
```

---

## GitHub Pages

The web experiment is placed at:

```text
experiments/convenience-rent/index.html
```

A small root `index.html` is also included so GitHub Pages can open a simple landing page.

---

## Spec relationship

YAML is the structured public reference spec.  
Markdown is the human-readable companion.

If they drift, the YAML fields are treated as the reference, and the Markdown should be updated.

---

## Experiments

Experiments are not separate projects.  
They are small rendered Shells from the same axis one source.

### Convenience Rent / 便利家賃

Convenience Rent is a co-rendering visual novel prototype.

It is not a finished game.  
It is a small playable Shell for observing how choices can become reaction points.

---

## Validation

```bash
python scripts/validate_versions.py
```

This checks that the public kit version labels and key file references stay aligned.

---

## License

MIT License.

---

## Links

- [Official site](https://www.axis-3.com)
- [Whitepaper](https://www.axis-3.com/whitepaper)
- [Contact](https://www.axis-3.com/contact)
- [Repository](https://github.com/ShinY1229/axis-one)

---

## Author / Publisher

axis one is authored by Shin Yamazaki and published by axis Inc.

axis one は Shin Yamazaki が著作し、axis Inc. により公開されています。

Created through Co-rendering.

---

## Status

Public working kit v0.2.3  
Updated 2026-06-12
