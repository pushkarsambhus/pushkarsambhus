# Engineering Productivity & AI Experiments

Hi, I'm Pushkar Sambhus — Principal Engineer with 16+ years in 
enterprise platform engineering, CI/CD automation, and AI/ML 
integration across large engineering organizations.

This repository is a collection of prototypes and learning 
projects exploring how AI can be applied to developer productivity 
problems — the same class of problems I've spent my career 
solving at scale at Workday.

These are intentionally small-scale explorations, not production 
systems. The production version of some of these ideas — 
particularly the build failure detection work — lives inside 
Workday's internal platform.

---

## Projects

### Dev Productivity Agent
A prototype exploring AI-assisted CI/CD log triage — given a 
build failure log, uses an LLM to identify the failure pattern 
and suggest a likely root cause.

Inspired by a production system I built at Workday that reduced 
build failure triage from 20+ minutes to near-immediate results 
across 60+ engineering teams.

**Stack:** Python · LangChain · OpenAI API

---

### Slack QA Assistant
A prototype Slack integration that takes a PR diff as input and 
suggests relevant test cases — exploring how LLMs can assist 
the developer-tester feedback loop.

**Stack:** Python · Slack API · OpenAI API

---

### CI/CD AI Guardrails
A prototype CLI tool that analyzes pipeline configuration for 
common quality gaps — missing tests, exposed secrets, dependency 
risks — using LLM-assisted pattern detection.

**Stack:** Python · GitHub Actions · OpenAI API

---

## What I'm Exploring

- How automated failure detection patterns from CI/CD pipelines 
  apply to evaluating AI system behavior
- LLM evaluation infrastructure using LangSmith and DeepEval
- Adversarial testing methodologies for AI quality systems

---

## Background

Currently leading technical strategy for Workday's Workforce 
pillar — supporting 260+ engineers globally across Time, Absence, 
Compensation, Benefits, HR Core, Scheduling, and Compliance.

The work here reflects where I'm headed next: the intersection 
of platform engineering, AI quality systems, and adversarial 
thinking about how AI systems fail.

→ LinkedIn: linkedin.com/in/pushkarsambhus
