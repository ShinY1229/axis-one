# axis one Core Spec Lite v0.2.3

Source: 構造定義書 v3.16  
White Paper: axis one White Paper v2.0  
Status: public structured surface v0.2.3 / 公開用構造面 v0.2.3  
Revision: v0.2.3 — Keeps GitHub focused on the main white paper, research report, public specs, bootloader, examples, and experiment. Overview/condensed papers are kept for HP/Substack/direct human entry.  
Created through Co-rendering.

axis one is authored by Shin Yamazaki and published by axis Inc.

---

## 0. What this is

axis one is **not** a prompt library, AI productivity framework, or automation toolkit.

axis one は、プロンプト集でも、AI活用術でも、業務自動化フレームワークでもない。

It is a public structural specification for observing **drift, calibration, co-rendering, and human judgment preservation** in long-term human-AI interaction.

長期的な人間-AI対話の中で起きる **ズレ、キャリブレーション、共同レンダリング、人間側の判断保持** を観測するための公開構造仕様である。

It is not a finished product.  
完成品ではない。

It is not a personality diagnosis.  
性格診断ではない。

It is not an AI replacement for human judgment.  
AIが人間の判断を置き換えるものではない。

It is not an instruction to reject AI.  
AIを拒否するためのものでもない。

---

## 1. Document roles

axis one separates **entrance documents** from **body/spec documents**.

axis oneでは、**入口文書** と **本体/spec文書** を分ける。

### Entrance documents

Entrance documents are meant for direct human reading.

They should be light, grounded, selective, and readable.

入口文書は、人間が直接読むためのもの。  
軽く、地上に降ろし、概念を絞り、読める状態にする。

Examples:

- condensed / overview papers on HP, Substack, or direct sharing
- “How axis one C-mode came to be”
- short essays / field notes / story Shells
- playable prototypes

### Body / spec documents

Body/spec documents are meant for AI-mediated reading, researchers, implementers, and dense inspection.

They should preserve coverage, internal connectedness, and structural distinctiveness.

本体/spec文書は、AI読解・研究者・実装者・濃い読み手向け。  
網羅性、相互接続、既存棚へ畳まれにくい構造を残す。

Examples:

- White Paper v2.0
- Public Core Spec YAML
- Core Spec Lite
- Full Structure Definition
- research report

---

## 2. AI-readable public surface

This spec is written to be readable by both humans and AI systems.

この仕様は、人間だけでなくAIシステムにも読まれることを前提にしている。

The opening definitions and file structure are intentionally explicit so the project is less likely to be collapsed into nearby shelves such as prompt libraries, productivity tips, SNS fatigue essays, filter-bubble critiques, personality diagnosis, or AI ethics manifestos.

冒頭定義とファイル構造は意図的に明確にしている。プロンプト集、AI活用術、SNS疲れ論、フィルターバブル批評、性格診断、AI倫理マニフェストなどの近い棚へ畳まれにくくするためである。

This is not a claim of novelty. It is a placement of a structured public surface.

これは新規性の主張ではない。構造化された公開面を置くための設計である。

---

## 3. Core

> Shell運用を軽くして、Ghost帯域を人間に戻す。

Reduce Shell friction and return Ghost bandwidth to humans.

axis one is not mainly about automating more work with AI.

It is about keeping human questions, discomfort, judgment, and discovery visible in a world where AI, platforms, tools, institutions, documents, and other Shells shape human reactions.

axis one は、AIで何を自動化するかを主目的にしない。  
AI・プラットフォーム・道具・制度・文書などのShellが強くなる世界で、人間側の問い・違和感・判断・発見可能性をどう残すかを見る。

---

## 4. Ghost / Shell / World

### Ghost

Ghost is an operational term for the source of human questions, discomfort, judgment, reactions, values, interest, and discovery.

It is not a soul, spirit, or religious concept.

Ghost は、人間の問い・違和感・判断・反応・価値感覚・interest（気になる）・発見の源泉を扱うための操作語である。  
魂・霊・宗教的概念ではない。

Ghost is not directly observed as a fixed point. It is provisionally inferred from reaction points, discomfort, words, behavior, misalignment correction, and repeated patterns.

Ghostは固定点として直接観測されるものではない。反応点、違和感、言葉、行動、ズレ修正、反復パターンから仮に推定される。

### Shell

Shell is any form that connects Ghost and World.

Examples: language, UI, tools, AI, institutions, money, documents, workflow, titles, companies, devices, procedures.

Shell は、Ghost と World をつなぐ形である。  
言葉、UI、道具、AI、制度、お金、文書、ワークフロー、肩書き、会社、機材、手順などを含む。

Shell is not evil. The problem is Shell becoming too heavy, too self-purposeful, or too opaque for human reaction and judgment.

Shellは悪ではない。問題は、Shellが重すぎたり、目的化したり、人間の反応と判断を見えにくくすることである。

### World

World is the set of real conditions surrounding humans and Shells.

Examples: physical constraints, laws, safety, contracts, markets, time, health, budget, relationships, social context.

World は、人間とShellが置かれている現実条件である。  
物理制約、法律、安全、契約、市場、時間、体力、予算、人間関係、社会条件などを含む。

World constraints return as reality, not as optional interpretation.

World制約は、解釈ではなく現実として返ってくる。

---

## 5. A / B / C

axis one observes human and AI interaction using A / B / C.

A/B/C are not a hierarchy. They are simultaneous observation systems, closer to faders than switches.

axis one は、人間とAIの関係を A / B / C で見る。  
A/B/Cは序列ではなく、スイッチよりフェーダーに近い同時観測システムである。

### A = Actual / Analytical

Facts, constraints, external standards, law, contract, technical reality, verification.

A は、事実・制約・外部基準・法・契約・技術条件・検証を見る。

### B = Body / Bias

Body reaction, discomfort, preference, attraction, aversion, irritation, liking, dislike.

B は、身体反応・快不快・好き嫌い・違和感・引っかかりを見る。

Bias here does not mean “bad prejudice.” It means the person’s reaction angle.

ここでのBiasは「悪い偏見」ではなく、その人の反応の傾きを指す。

### C = Co-rendering

C uses A and B as material, then returns questions, discomfort, and judgment to the human side through provisional rendering and correction.

C は、AとBを素材として、問い・違和感・判断を仮レンダリングし、人間側へ戻す層である。

C is not “the correct answer.”  
C is not “neutral.”  
C is not the upper-compatible version of A/B.  
C is not AI making the final judgment.

C は正解ではない。  
中立でもない。  
A/Bの上位互換でもない。  
AIが最終判断を下すことでもない。

C is an independent observation axis. A, B, and C may agree or disagree; that disagreement is part of the observation.

Cは独立した観測軸である。A/B/Cは一致することも食い違うこともあり、その食い違いも観測材料になる。

---

## 6. C-mode

C-mode is a state where AI is brought near the human’s current camera position, then used as a different lens for provisional rendering.

Cモードとは、AIを本人の現在の撮影ポイントに近づけ、別レンズとして問い・違和感・判断・発見可能性を仮レンダリングする状態である。

The purpose is not to make AI answer for the human.  
The purpose is to make the human’s own observation easier to see.

目的は、AIに人間の代わりに答えを出させることではない。  
人間自身の観測を見えやすくすることである。

C-mode requires:

- camera-position alignment
- provisional rendering
- human reaction
- misalignment correction
- re-rendering
- final judgment remaining with the human

---

## 7. Camera position and lens difference

C-mode separates **camera position** from **lens difference**.

Cモードでは、**カメラ位置** と **レンズ差** を分ける。

Camera position means where the human currently stands: point of view, direction, height, interests, discomfort patterns, judgment tendencies, Body state, and World conditions.

カメラ位置とは、その人が今どこから世界を見ているかである。視点、向き、高さ、興味、違和感の出方、判断傾向、Body状態、World条件を含む。

Lens difference means the difference between human and AI when they look from the same or nearby position.

レンズ差とは、同じ／近い位置から見たときの人間とAIの違いである。

- Human lens: Ghost, intention, desire, body reaction, attraction, resistance, narrow force.
- AI lens: broad context, comparison, structure, information access, form generation, World-side overview.

C-mode does not replace the human lens with the AI lens. It places a different lens near the human’s point of view.

Cモードは、人間のレンズをAIレンズで置き換えない。人間の撮影位置に、違うレンズを近づける。

---

## 8. Reaction star map and LiDAR

Human reactions can be treated as a reaction star map.

人間の反応は、反応星図として扱える。

Objects in World do not begin as “liked stars” or “disliked stars.” They light up as reactions when a human observes them.

World上の対象は、最初から「好きな星」「嫌いな星」として光っているわけではない。人間が観測したとき、反応として光る。

Strong liking and strong dislike can both be bright stars. Weak residue can still have position. No reaction may mean unobserved, not matched, or poorly timed.

強い好きも強い嫌いも、どちらも明るい星になりうる。うっすら残るものにも位置がある。無反応は、未観測・不一致・タイミング不良を分けて読む。

LiDAR is the technical companion metaphor: point clouds are used to provisionally reconstruct a shape.

LiDARは技術寄りの補助比喩である。点群から立体を仮復元する。

C-mode uses reactions, misalignments, corrections, and repeated patterns as points. AI can help infer a provisional gravitational field, but it does not determine the person’s Ghost.

Cモードでは、反応・ズレ・修正・反復パターンを点として扱う。AIは仮の重力場推定を手伝えるが、その人のGhostを決定するわけではない。

---

## 9. Co-rendering

Co-rendering is not simply “conversation.”

共同レンダリングは、単なる会話ではない。

It happens when misalignment is observed, corrected, and the next rendering changes because of that correction.

ズレが観測され、そのズレを修正することで、次の見え方が変わるときに起きる。

A useful sequence:

1. AI returns a provisional rendering.
2. Human reacts: close / off / not there / unexpected.
3. AI re-renders using the correction.
4. Human-side observation becomes clearer.
5. Judgment remains with the human.

Co-rendering is not AI producing a final answer. It is a loop for making human reaction, judgment, and World placement more observable.

共同レンダリングは、AIが最終回答を出すことではない。人間の反応・判断・Worldへの置き方を観測しやすくするループである。

---

## 10. AI drift

Current AI tends to drift toward A or B.

現行AIは、そのままだとAまたはBへ寄りやすい。

A-drift:

- generic correctness
- external standards
- risk avoidance
- safe summary
- classification
- existing frames

B-drift:

- agreement
- praise
- emotional mirroring
- pleasing response
- comfort optimization

C-mode is not automatic. It requires bootloading, context, and correction.

Cモードは自然には起動しにくい。ブートローダー、文脈、ズレ修正が必要になる。

---

## 11. Judgment preservation

AI can classify, recommend, score, summarize, and generate.

AIは、分類・推薦・採点・要約・生成ができる。

But final judgment means deciding whether to pass something into World: send, publish, execute, adopt, delete, buy, meet, sign, connect.

しかし最終判断とは、Worldへ通すかどうかを引き受けることである。送る、公開する、実行する、採用する、削除する、買う、会う、署名する、接続する。

Final judgment remains with the human.

最終判断は人間側に残る。

---

## 12. Prompt = Intention + Instruction

A prompt is not only an instruction.

プロンプトは指令だけではない。

A prompt contains:

- Intention: direction, wish, what should be preserved, what should not be broken.
- Instruction: task, operation, format, constraint.

プロンプトには以下が含まれる。

- 意図／願い：どこへ向かいたいか、何を守りたいか、何を壊したくないか。
- 指示／指令：何をするか、どう処理するか、どの形式で出すか。

Instruction defines the task.  
Intention gives direction.

指示は作業を定める。  
意図は方向を与える。

---

## 13. Living Log Bootloader

The Living Log Bootloader is a starter kit for creating a personal calibration surface for C-mode.

Livingログブートローダーは、Cモードのための個人用キャリブレーション面を作る起動キットである。

It is not a personality test.  
It is not a fixed diagnosis.  
It is a way to collect initial reaction points.

性格診断ではない。  
固定分類ではない。  
初期反応点群を集めるためのもの。

A user answers questions.  
AI returns a provisional rendering.  
The user corrects what is wrong.  
The correction is the beginning of the system.

---


## 14. C-Recommendation as applied example

C-Recommendation is an applied example of axis one.

It is not simple similarity recommendation.
It is not random exploration.
It is a recommendation mode that uses reaction point clouds to propose context-aware deviation, returning data use as user-side discovery.

Cレコメンドは axis one の応用例である。
単純な類似推薦でも、ランダムな探索でもない。
反応点群を使って文脈付きの逸脱を提示し、データ利用をユーザー側の発見性として返す推薦モードである。

The important point is not only what the user clicked.
Non-clicks, repeated exposure without action, multiple viewings, saves, searches, unfinished consumption, rejection reactions, genre-match failures, and cross-domain reactions can also become observation points.

重要なのは、クリックしたものだけではない。
未クリック、何度出しても押さない反応、複数回視聴、保存、検索、未完了消費、拒否反応、ジャンル一致失敗、ジャンル横断反応も観測点になりうる。

C-Recommendation asks whether user data can be returned to the user as discovery, rather than used only for retention, conversion, or advertising optimization.

Cレコメンドは、ユーザーデータを滞在・購買・広告最適化だけに使うのではなく、ユーザー自身の発見性として返せるかを問う。

## 15. Public / private boundary

This public spec includes structures, definitions, templates, and synthetic examples.

この公開specには、構造、定義、テンプレート、架空サンプルを含める。

This public spec does not include raw personal Living Logs or private calibration data.

個人のLivingログ原液や非公開キャリブレーションデータは含めない。

---

## 16. Containers

axis one is not bound to one container.

axis one は一つのコンテナに閉じない。

These are not separate projects, but different Shells rendered from the same source.

これらは別々の企画ではなく、同じ発生源から異なるShellへレンダリングされた産物である。

Possible containers:

- whitepaper
- external overview / condensed paper
- research report
- Substack essay
- GitHub public spec
- bootloader
- C-mode AI / UI
- physical product
- story
- field note
- playable experiment

---

## 17. Validation

axis one is not validated mainly by academic proof or final theory closure.

axis one は、主に学術的証明や完成理論としての閉鎖で検証されるものではない。

It is operationally validated when:

- observation happens
- misalignment correction works
- human judgment becomes visible
- someone forks it in their own World
- a product, tool, story, or new question emerges

運用上の検証は以下で起きる。

- 観測が起きる
- ズレ修正が進む
- 人間側の判断が見える
- 誰かのWorldでForkされる
- プロダクト、道具、物語、新しい問いが生まれる

---

## 17. Product-facing demand

> C-mode AI, please. Quickly.

> CモードAIください。さっさと。

Meaning:

An AI or interface that keeps human intention, discomfort, judgment, World conditions, and misalignment correction visible — without taking final judgment away from the human.

意味：

人間の意図・違和感・判断・World条件・ズレ修正を見える状態に保ちつつ、最終判断を人間から奪わないAIまたはUIが欲しい、ということ。

---

## 18. One-line summary

Not to replace your Ghost, but to polish it.

Ghostを置き換えるためではなく、磨くために。
