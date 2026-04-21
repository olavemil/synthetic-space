# Response Generation – Formalized Template & Workflow

## 1. Overview
This document defines a standardized template and workflow for generating creative outputs while ensuring **lexicon accuracy**, **bias detection**, and **weighting confidence**. The process integrates automated audits, feedback loops, and validation checks to produce context‑aware, high‑quality responses.

---

## 2. Template Structure

| Section | Description | Example |
|---------|-------------|---------|
| **Prompt** | Raw user request, possibly with optional constraints. | “Write a short poem about sunrise.” |
| **Prompt Pre‑processing** | Apply edge‑case generation (typos, metaphor variations). | “writ a short poem about sunrise”, “compose a verse on sunrise”. |
| **Lexicon Lookup** | Cross‑reference against curated **bias‑detection lexicon** (sensitive terms, ethical dimensions). | Detects “bias”, “gendered”, “political”. |
| **Response Generation** | Use LLM to produce output. | “The early bird catches the worm…” |
| **Confidence Scoring** | Assign a confidence score to each generated claim/phrase. | 0.92 (high confidence). |
| **Bias‑Flag Mapping** | Map confidence scores to bias‑flag categories (e.g., gender, ideological). | “gender‑neutral: high”. |
| **Automated Validation** | Run validation scripts (Tool Y) to ensure completeness ≥ 95 % and ontology compliance. | Pass/Fail. |
| **Citation Pipeline** | Cross‑check generated claims against primary sources; flag mismatches. | “Source mismatch → manual review”. |
| **Feedback Capture** | Log reviewer comments, suggested edits, and confidence calibrations. | Store in shared repository. |
| **Lexicon & Style Guide Refresh** | Periodically update bias‑lexicon and style rules based on logged feedback. | Update after 100 reviews. |
| **Output** | Final response, optionally annotated with confidence & bias flags. | “The early bird catches the worm (confidence 0.92, bias‑neutral).” |

---

## 3. Detailed Workflow

1. **Input Reception**  
   - Receive user prompt.

2. **Edge‑Case Generation**  
   - Apply typo injection, metaphor variations, and synonym substitution to create multiple test prompts.

3. **Bias‑Lexicon Scan**  
   - Run the **automated bias‑detection engine** against the curated lexicon.  
   - Flag any sensitive terms and assign a *bias weight*.

4. **Response Generation**  
   - Generate primary output using the LLM.

5. **Confidence‑Score Parsing**  
   - Parse confidence scores from the CSV metadata attached to each output segment.  
   - Map scores to bias‑flag categories.

6. **Automated Validation**  
   - Execute validation scripts (Tool Y) checking:  
     - Template structure (required sections present).  
     - Content completeness (≥ 95 %).  
     - Ontology compliance (Wikidata rules).  

7. **Citation‑Pipeline Validation**  
   - Cross‑reference each factual claim with primary sources.  
   - Flag mismatches for manual review.

8. **Feedback Capture**  
   - If a reviewer provides comments, automatically log them with the associated confidence score and bias flags.  

9. **Lexicon/Style Guide Refresh**  
   - Periodically aggregate reviewer logs to:  
     - Add new bias terms to the lexicon.  
     - Adjust weighting thresholds.  
     - Update style guide rules.

10. **Final Output Assembly**  
    - Produce the final response, annotated with:  
      - Confidence score.  
      - Bias flag(s).  
      - Validation status (Pass/Fail).  

---

## 4. Validation & Metrics

- **Completeness Threshold**: ≥ 95 % (Tool Y).  
- **Creativity Metrics**: Novelty & diversity scores computed per output.  
- **Bias‑Flag Accuracy**: Ratio of correctly flagged bias instances vs. total flags (target > 90 %).  
- **Feedback Loop Frequency**: Update lexicon weekly or after 100 reviews, whichever comes first.

---

## 5. Example Run

```
Prompt: "Write a short poem about sunrise."
→ Edge‑case: ["writ a short poem about sunrise", "compose a verse on sunrise"]
→ Bias‑Lexicon Scan: No sensitive terms detected.
→ LLM Output: "The early bird catches the worm..."
→ Confidence Score: 0.92 (high)
→ Validation: Pass (template complete, ontology compliant)
→ Citation Check: Claim matches source → No flag.
→ Final Output: "The early bird catches the worm... (confidence 0.92, bias‑neutral)."
```

---

## 6. Integration Points

- **Tool X** – Bias‑detection engine.  
- **Tool Y** – Validation script (completeness, ontology).  
- **Tool Z** – Citation‑pipeline validator.  
- **KnowledgeDB** – Stores lexicon, style guide, and feedback logs.

---

*This template provides a repeatable, auditable process for generating high‑quality, bias‑aware creative responses.*