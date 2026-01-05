# 5-core-db
**Evidence‑Linked 5‑Core Construction Data Integration and Audit‑Ready Design Compliance Checking**

This repository is a **reproducibility package** for the paper/manuscript on an **evidence‑linked (fine‑grained provenance) ontology knowledge graph** that unifies heterogeneous construction deliverables (“5‑core”) and enables **audit‑ready rule‑based compliance checking** and **grounded LLM reporting**.

> **Core idea:** Knowledge is stored as **assertions that must carry Evidence**.  
> If an assertion has **no Evidence link (`isDerivedFrom`)**, it **cannot be ingested** into the knowledge graph (traceability as an invariant).

---

## What this repo provides
- **Case 1 — Traceability Invariant Validation**  
  A minimal end‑to‑end reproduction showing that **every assertion in the KG is traceable** to at least one Evidence record with a **fine‑grained locator** (page+bbox / table cell / clause locator / timestamp).
- **Case 2 — Scaffold (Scaffolding) Compliance Checking**  
  A reproduction of rule‑based checking over a scaffold drawing dataset (anonymized/synthetic) where each violation is stored with **dual evidence**:
  - `E_actual`: evidence for extracted actual value (e.g., drawing bbox)
  - `E_clause`: evidence for the referenced clause/requirement (e.g., clause page+ID)
- **LLM Evaluation (Grounded Responses)**  
  A reproducible workflow for **data‑card bounded** question answering/report generation, where LLM outputs are constrained to retrieved Evidence/clauses.

---

## Concept glossary (quick)
- **5‑core data**: Drawing / Calculation·Analysis / 3D‑BIM / Document·Report / Field·Physical
- **Evidence**: a fine‑grained provenance unit that stores a locator  
  (e.g., `page+bbox`, `sheet+(row,col)`, `clauseId+page`, `timestamp`)
- **Traceability invariant**: “No Evidence → No assertion in KG”
- **Dual evidence** (for compliance results): actual evidence + clause evidence

---

## Repository structure
> The exact file names may evolve; the top‑level entry points are the three reproduction folders.

