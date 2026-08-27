<!--
  Visual direction: a real spectral workflow leads; authored identity and
  evidence-led contribution groups follow. The loop is a lightweight preview
  derived from the approved sanitized demo and links to the fixed public MP4.
-->

<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/dvd233/dvd233@a9e0e32e544dc7cbafe1de8c0cc99e64aa82d55b/assets/demo-sanitized-1080p30-muted.mp4">
    <img src="assets/demo-loop.webp" width="100%" alt="Looping preview of a two-person team's private hyperspectral reconstruction prototype: camera capture, 30-band reconstruction from 400 to 690 nanometres, and a sampled spectral curve.">
  </a>
</p>

<p align="center"><sub>↗ Click the loop to open the full muted demo · 10.77 s · 400–690 nm</sub></p>

<p align="center">
  <img src="assets/intro-card.svg" width="100%" alt="Hi, I'm dvd233. AI Full-Stack Engineer.">
</p>

> I build reliable AI applications end to end, from frontend and client experiences to agent runtimes, APIs, and data workflows, grounded in computational imaging and evidence-first engineering.
>
> Open to AI full-stack engineering opportunities.

<p align="center">
  <code>🤖 full-stack AI</code>&nbsp;&nbsp;
  <code>🖥️ frontend + client</code>&nbsp;&nbsp;
  <code>🧠 agent systems</code>&nbsp;&nbsp;
  <code>🔬 computational imaging</code>&nbsp;&nbsp;
  <code>🧾 evidence-first</code>
</p>

构建可靠的 AI 全栈应用与前端/客户端体验，以计算成像和证据驱动工程形成技术纵深。

## 👋 About

I turn AI and agent capabilities into end-to-end interfaces and local tools people can actually inspect, use, and verify. My strongest overlap is **AI full-stack engineering with frontend, client, orchestration, and data delivery**; computational imaging gives that work a real systems constraint, and open-source collaboration keeps the claims honest.

## 🧭 Engineering focus

- **AI full-stack applications** — shaping agent and LLM capabilities into reliable product experiences across UI, orchestration, APIs, and data flows.
- **Frontend & client systems** — building streaming interfaces, desktop workflows, and cross-platform behavior.
- **Computational imaging** — bringing reconstruction research into usable software without erasing its limits.
- **Evidence-first delivery** — reproducing failures, adding focused tests, and leaving artifacts that can be reviewed.

## 🧰 AI engineering workflow

I use AI coding agents across the engineering loop: exploring unfamiliar codebases, implementing features, debugging, designing tests, documenting decisions, and preparing reviewable changes.

<p align="center">
  <code>Kimi Code</code>&nbsp;&nbsp;
  <code>Codex</code>&nbsp;&nbsp;
  <code>Pi</code>&nbsp;&nbsp;
  <code>Claude Code</code>
</p>

将 AI 编程工具融入代码理解、实现、调试、测试、文档与评审流程；架构决策、验证和最终改动仍由我负责。

## 🎬 What the demo shows

This is an **earlier private hyperspectral reconstruction prototype**, co-developed in a two-person team. The public loop and full demo show a desktop workflow for camera acquisition, lightweight deep-learning reconstruction, 30-band spectral display across 400–690 nm, per-point spectral curves, and result saving.

I was responsible for the lightweight deep-learning reconstruction and dataset work, plus the camera acquisition, desktop UI, spectral visualization, and result-saving modules. Code and data remain private because of research and industry-collaboration constraints.

## 🔧 Open-source contributions

Open source is where I practice the same loop I bring to product work: **reproduce → isolate → test → review → ship**.

<p align="center">
  <code>23 merged upstream PRs</code>&nbsp;&nbsp;
  <code>10 PRs in review</code>&nbsp;&nbsp;
  <code>7 upstream repositories</code>
</p>

<sub>Public snapshot · 27 Aug 2026 · plus one merged documentation PR in my own repository. Counts are time-bound; open work is shown as collaboration in review, not as shipped product.</sub>

### 🧩 Contribution map

- 🧾 **Evidence workflow** · [open-city-ai/haidian](https://github.com/open-city-ai/haidian) · `24 PRs · 23 merged · 1 open`<br>Evidence packages, Windows portability, deterministic artifacts, and review semantics.
- 🤖 **AI / Agent runtime** · [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) · `2 open`<br>AI/Agent runtime correctness and Windows subprocess behavior.
- 🧠 **Agent memory & Node runtime** · [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) · `3 open`<br>Proxy preservation, SQLite filtering, and self-healing store state.
- 🧩 **AI code-review tooling** · [alibaba/open-code-review](https://github.com/alibaba/open-code-review) · `1 open`<br>Go configuration and Jinja template support for review workflows.
- 🖥️ **Desktop UX** · [desktop/desktop](https://github.com/desktop/desktop) · `1 open`<br>React/TypeScript pull-request state and suggestion behavior.
- 🛠️ **Web tooling** · [parcel-bundler/parcel](https://github.com/parcel-bundler/parcel) · `1 open`<br>Correct UTF-8 BOM JSON parsing in the resolver path.
- 🗺️ **Search & coordinates** · [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps) · `1 open`<br>C++ search behavior for space-separated DMS coordinates.

One additional merged documentation PR lives in [dvd233/26.6.13-codex1#2](https://github.com/dvd233/26.6.13-codex1/pull/2); it is counted separately from upstream work.

### ✅ Merged proof

<details>
  <summary>📦 Complete delivery · bilingual formal submission — merged</summary>

  **Problem** — A civic-data submission needed a complete, reviewable package rather than an unsupported concept.

  **Contribution** — I delivered a scoped 41-file bilingual package spanning narrative, offline HTML/PDF, GeoJSON, metrics, sources, a manifest, and deterministic self-checks, while marking provisional geometry and non-endorsement boundaries.

  **Evidence** — [open-city-ai/haidian#2540](https://github.com/open-city-ai/haidian/pull/2540) · merged for repository intake, not gallery publication or government endorsement.
</details>

<details>
  <summary>🔍 Auditable evidence · site provenance — merged</summary>

  **Problem** — Provisional site inputs lacked consistent dates, hashes, licence and use boundaries, while an empty constraints layer could be mistaken for evidence that no controls existed.

  **Contribution** — I added a built-ins-only audit for four submitted geometries, recorded six missing official-control layers, and made replacement triggers and permitted uses traceable across the package. The merged change passed 18/18 audit checks.

  **Evidence** — [open-city-ai/haidian#3525](https://github.com/open-city-ai/haidian/pull/3525)
</details>

<details>
  <summary>🪟 Windows portability · import and worker locking — merged</summary>

  **Problem** — An unconditional <code>fcntl</code> import stopped two test modules from being collected on Windows, and worker-lock contention needed consistent cross-platform semantics.

  **Contribution** — I reproduced the failure, introduced the guarded POSIX/Windows lock path, and added the initial regression. Maintainer review then corrected the production file-open path and strengthened its test; the previously uncollectable target suite passed 21/21 tests.

  **Evidence** — [open-city-ai/haidian#3859](https://github.com/open-city-ai/haidian/pull/3859)
</details>

<details>
  <summary>↔️ Deterministic artifacts · LF across platforms — merged</summary>

  **Problem** — Three writer paths emitted CRLF on Windows, creating whole-file diff noise and breaking byte-hash consistency after line-ending normalization.

  **Contribution** — I made the writers emit LF bytes and added direct plus end-to-end regressions. After review exposed a Python 3.9 compatibility issue, I revised the implementation and revalidated both flows.

  **Evidence** — [open-city-ai/haidian#3915](https://github.com/open-city-ai/haidian/pull/3915)
</details>

<details>
  <summary>🧠 Review semantics · blockers versus future follow-ups — merged</summary>

  **Problem** — A flat review-action list converted future conditions into immediate change requests, creating an intake loop that compliant edits could not close.

  **Contribution** — I introduced explicit non-blocking follow-ups with trigger and owner fields, invalidated legacy review caches, and kept current or malformed repairs fail-closed with focused regression coverage.

  **Evidence** — [open-city-ai/haidian#3982](https://github.com/open-city-ai/haidian/pull/3982) · the original blocked head was re-reviewed and merged without weakening existing gates.
</details>

<sub>Latest merged follow-through: [open-city-ai/haidian#4011](https://github.com/open-city-ai/haidian/pull/4011) · publish bounded per-dimension repairs in PR comments.</sub>

### 🛠️ In review now

<details>
  <summary>🤖 AI / agent runtime · 5 open PRs</summary>

  - [agentscope-ai/agentscope#2434](https://github.com/agentscope-ai/agentscope/pull/2434) — disable Uvicorn hot reload on Windows so subprocess execution keeps a compatible event loop.
  - [agentscope-ai/agentscope#2435](https://github.com/agentscope-ai/agentscope/pull/2435) — preserve <code>encrypted_content</code> on Responses reasoning items for stateless multi-turn calls.
  - [TencentCloud/TencentDB-Agent-Memory#1171](https://github.com/TencentCloud/TencentDB-Agent-Memory/pull/1171) — keep Node's global proxy dispatcher intact while loading <code>undici@8</code>.
  - [TencentCloud/TencentDB-Agent-Memory#1172](https://github.com/TencentCloud/TencentDB-Agent-Memory/pull/1172) — self-heal the store-init cache after failed initialization or a closed store.
  - [TencentCloud/TencentDB-Agent-Memory#1173](https://github.com/TencentCloud/TencentDB-Agent-Memory/pull/1173) — honor <code>recordIds</code> filtering in the SQLite L1 query path.
</details>

<details>
  <summary>🖥️ Frontend / client / tooling · 4 open PRs</summary>

  - [alibaba/open-code-review#1056](https://github.com/alibaba/open-code-review/pull/1056) — add Jinja template support to the review configuration flow.
  - [desktop/desktop#22767](https://github.com/desktop/desktop/pull/22767) — hide pull-request suggestions when a branch has no commits ahead of the default branch.
  - [parcel-bundler/parcel#10352](https://github.com/parcel-bundler/parcel/pull/10352) — parse UTF-8 BOM JSON correctly in the resolver path.
  - [organicmaps/organicmaps#13423](https://github.com/organicmaps/organicmaps/pull/13423) — support space-separated DMS coordinates in search.
</details>

<details>
  <summary>🧾 Evidence workflow · 1 open PR</summary>

  - [open-city-ai/haidian#3821](https://github.com/open-city-ai/haidian/pull/3821) — expose synthetic-capacity gates in review carriers; currently in upstream review.
</details>

<p align="center"><a href="https://github.com/search?q=author%3Advd233+is%3Apr&type=pullrequests">↗ Browse the full public PR trail</a></p>

## 🎓 Education

Master's student at BUPT · Electronic Engineering & Information Photonics<br>
Undergraduate background in Network Engineering at BUPT

## 📬 Contact

Open to AI full-stack engineering opportunities.

[dvd@linux.do](mailto:dvd@linux.do) · [z1403594118@gmail.com](mailto:z1403594118@gmail.com)
