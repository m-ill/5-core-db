# Evidence-linked Ontology Knowledge Graph for 5-core Construction Data Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the official **reproduction package** for the research paper:

> **"Evidence-linked Ontology Knowledge Graph based 5-core Construction Data Integration and Auditability"**

This project demonstrates a framework that integrates heterogeneous construction data (Drawings, Calculations, BIM, Documents, Field data) into an **Evidence-linked Knowledge Graph**, ensuring that every assertion is traceable to its micro-locator (bbox, cell, clause).

## 📂 Repository Structure

The repository is organized to validate the three main claims of the paper:

```text
.
├── data/                    # Synthetic datasets with identical schema to the proprietary source
│   ├── synthetic_assertions.json  # For Case 1 (Traceability)
│   ├── synthetic_scaffold.json    # For Case 2 (Compliance Checking)
│   └── synthetic_rules.json       # Anonymized rule definitions
├── repro_case1/             # [Claim A] Traceability Invariant Validation
│   └── reproduce_case1.py   # Script to verify ingestion constraints and evidence linkage
├── repro_case2/             # [Claim B] Auditable Compliance Checking
│   ├── reproduce_case2.py   # Script to run dual-evidence rule checking
│   └── rules_engine.py      # Lightweight rule evaluation logic
├── repro_llm_eval/          # [Claim C] Grounded LLM Response Evaluation
│   └── reproduce_llm_eval.py # Script to calculate citation coverage & hallucination rates
├── figures/                 # Figures used in the manuscript
└── requirements.txt         # Python dependencies
🚀 Getting Started
Prerequisites
Python 3.8 or higher

Recommended: Virtual environment (venv or conda)

Installation
Bash

git clone [https://github.com/m-ill/5-core-db.git](https://github.com/m-ill/5-core-db.git)
cd 5-core-db
pip install -r requirements.txt
📊 Reproduction Steps
We provide synthetic data that mirrors the structure of the proprietary project data used in the paper. This allows reviewers to verify the algorithmic logic and data structures without violating NDA constraints.

1. Reproduce Case 1: Traceability Invariant (Claim A)
Validates that the system enforces mandatory evidence linkage during data ingestion.

Target: Table 2 (Panel A) in the manuscript.

Run:

Bash

python repro_case1/reproduce_case1.py
Expected Output:

Console output showing "Ingestion Acceptance Rate".

A CSV log of rejected assertions (due to missing evidence) in repro_case1/outputs/.

2. Reproduce Case 2: Scaffold Compliance Checking (Claim B)
Demonstrates the Dual-Evidence mechanism where every violation links to both the Actual Value Source (e.g., Drawing bbox) and the Requirement Source (e.g., Standard Clause).

Target: Table 4 & 5 (Violation Instances & Dual Locators).

Run:

Bash

python repro_case2/reproduce_case2.py
Expected Output:

violation_instances.csv: A list of detected violations with evidence_actual and evidence_clause fields populated.

3. Reproduce LLM Evaluation (Claim C)
Calculates quantitative metrics for the "Data Card" bounded RAG approach.

Target: Table 6 (Citation Coverage, Hallucination Rate).

Run:

Bash

python repro_llm_eval/reproduce_llm_eval.py
Expected Output:

Console report of Citation Coverage and Hallucination Rate based on the provided labeled logs.

🛡️ Data Availability
Due to confidentiality agreements and intellectual property rights involving the construction company and the specific project (High-rise building in South Korea), the raw source files (DWG drawings, full internal standard documents) cannot be made public.

However, the data/ directory contains synthetic JSON data that strictly follows the Evidence-linked Ontology Schema defined in the paper. This ensures that the code logic and the "Traceability Invariant" mechanism are fully reproducible.

📝 Citation
If you use this code or framework, please cite our paper:

코드 스니펫

@article{heo2026evidence,
  title={Evidence-linked Ontology Knowledge Graph based 5-core Construction Data Integration and Auditability},
  author={Heo, Seok-Jae and Others},
  journal={Submitted to Automation in Construction},
  year={2026}
}
(Citation details will be updated upon publication)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
