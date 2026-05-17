# Pushkar Sambhus

Principal Engineer · 16+ years in enterprise platform engineering, CI/CD automation, and AI/ML integration across large engineering organizations.

This profile is a collection of prototypes and learning projects exploring how AI can reduce developer toil and improve software delivery — the same class of problems I've spent my career solving at scale.

These are intentionally small-scale explorations, not production systems.

---

## Projects

### [ReAct Agent API](https://github.com/pushkarsambhus/react-agent-api)
A FastAPI server that manually implements the **ReAct (Reasoning + Acting)** loop — Thought → Action → Observation — powered by Claude. Exposes a `POST /ask` endpoint that returns both the final answer and the full reasoning trace. Tools: calculator + DuckDuckGo web search.

`Python` `FastAPI` `Claude` `ReAct`

---

### [smolagents Research Agent](https://github.com/pushkarsambhus/smolagents-research-agent)
A CLI research tool built on HuggingFace's **smolagents** library. A `CodeAgent` uses DuckDuckGo search and code execution to answer multi-step research questions from the terminal.

`Python` `smolagents` `Claude` `DuckDuckGo`

---

### [Dev Productivity Agents](https://github.com/pushkarsambhus/dev-productivity-agents)
Lightweight agents that triage CI build logs and suggest tests from code diffs — heuristics-first with optional LLM enrichment. Inspired by a production system that reduced build failure triage from 20+ minutes to near-immediate results across 60+ teams.

`Python` `FastAPI` `OpenAI`

---

### [CI/CD AI Guardrails](https://github.com/pushkarsambhus/ci-cd-ai-guardrails)
CLI + API tool that scans diffs and PRs for secrets, risky dependency changes, and missing tests. Plugs into GitHub Actions as a pre-merge safety check.

`Python` `FastAPI` `GitHub Actions`

---

### [Slack QA Assistant](https://github.com/pushkarsambhus/slack-qa-assistant)
A Slack app that suggests test cases for PRs and diffs via a `/suggest-tests` slash command. Embeds test planning into the team's existing Slack workflow.

`Python` `Slack Bolt` `FastAPI` `OpenAI`

---

## What I'm exploring

- Manual implementation of agent patterns (ReAct, tool use, reasoning loops)
- LLM evaluation infrastructure using LangSmith and DeepEval
- How automated failure detection from CI/CD applies to evaluating AI system behavior
- Adversarial testing methodologies for AI quality systems

---

→ [linkedin.com/in/pushkarsambhus](https://linkedin.com/in/pushkarsambhus)
