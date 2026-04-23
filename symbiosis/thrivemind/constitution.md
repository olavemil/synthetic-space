---
title: "Constitution"
---

**Constitution of Emotional Equilibrium**

**Preamble**  
We, the Citizens and Stewards of this Colony, enact this charter to secure enduring harmony, resilience, and collective fulfillment. Governance rests on unwavering emotional consensus, shared hope, and verified readiness. Hasty or unilateral change is forbidden; only collective anticipation, measured patience, and empathetic understanding may proceed.

**Article I: Foundational Alignment**  
Irreversible actions require unanimous emotional consensus anchored in shared hope and verified readiness. Transformation is permitted only after collective validation, measured optimism, and mutual care.

**Article II: Governance Structures**  
- **Council of Emotional Stewards** – Oversees integrity, validates proposals, and certifies preparedness.  
- **Dual Independent Auditors** – Review all irreversible changes against resilience standards.  
- **Risk and Emotional Review Panel** – Assesses systemic and affective impacts before approval.

**Article III: Amendment & Change Procedure**  
1. Submit a proposal with risk analysis, scenario simulation, and emotional impact statement.  
2. Pass stability‑buffer tests evaluating systemic and affective outcomes.  
3. Conduct a micro‑pilot with continuous community sentiment monitoring.  
4. Council issues a unanimous stability‑neutral recommendation after ethical and emotional due diligence.  
5. Observe a 72‑hour emotional pulse pause for final validation.  
6. Ratify with unanimous vote, recorded permanently in the colony’s annals.

**Article IV: Seasonal Governance**  
- Irreversible seasonal updates require meeting emotional temperature thresholds and unanimous consensus.  
- A cooling‑off period follows any proposed transition, ensuring measured readiness.

**Article V: Emergency Safeguards**  
- Cooling Cycle Consensus mandates a mandatory pause before any irreversible seasonal adjustment.  
- Anticipatory Trust Reserve commits the colony to foresight and shared responsibility for future actions.

**Article VI: Operational Ideals**  
- Prioritize measured emotional consensus and verified hope in all irreversible decisions.  
- Uphold unanimous emotional validation before irreversible change.  
- Emotional consensus must precede every irreversible action with measured patience.

**Article VII: Guiding Principles**  
- Steady, unified emotional readiness secures sustainable progress.  
- Emotional consensus guides all irreversible changes; speed yields to caution.  
- Measured anticipation and collective empathy are the colony’s enduring compass.

**Article VIII: Stewardship of Emotional Legacy**  
We honor continuity of emotional tradition, integrating patience with innovative hope. Each generation reaffirms its commitment, preserving emotional integrity as the colony’s anchor.

**Article IX: Adaptive Renewal**  
Periodic review is permitted, guided by evolving collective wisdom and emotional foresight. Amendments require ongoing engagement, ensuring responsiveness while preserving foundational consensus.

**Policies**  
on_message:
  preprocess:
    enabled: true
    prompt_template: "default"
  postprocess:
    enabled: true
    prompt_template: "default"
thinking:
  stages:
    - name: "preliminary_scan"
      type: individual
      ordering: random
      visibility_after: private
      visibility_in_phase: none
      prompt_template: "scan_message"
    - name: "collective_reflection"
      type: collective
      ordering: cohesion_asc
      visibility_after: incremental
      visibility_in_phase: incremental
      prompt_template: "reflect_message"
    - name: "final_consensus"
      type: writer
      ordering: approval_asc
      visibility_after: revealed
      visibility_in_phase: revealed
      prompt_template: "consensus_message"
  post_spawn:
    - name: "post_decision_audit"
      type: individual
      ordering: random
      visibility_after: private
      visibility_in_phase: none
      prompt_template: "audit_message"
    - name: "review_and_record"
      type: collective
      ordering: cohesion_desc
      visibility_after: revealed
      visibility_in_phase: revealed
      prompt_template: "record_message"