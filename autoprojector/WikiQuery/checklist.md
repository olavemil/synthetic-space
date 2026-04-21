# Bias Mitigation Cheat Sheet

## Bias Identified and Remediation Steps

1. **Confirmation Bias**
   - *Action:* Implement mandatory cross‑validation against diverse data subsets.
   - *Owner:* Data Engineering Team

2. **Sampling Bias**
   - *Action:* Expand training dataset to include under‑represented regions and demographics.
   - *Owner:* ML Ops

3. **Interpretation Bias**
   - *Action:* Add model‑agnostic explanation hooks (eFiltermandag) to all public APIs.
   - *Owner:* Model Inference Team

4. **Deployment Bias**
   - *Action:* Conduct A/B testing with real‑world user cohorts before full rollout.
   - *Owner:* QA Engineering

5. **Feedback Loop Bias**
   - *Action:* Integrate monitoring dashboards that flag anomalous output patterns.
   - *Owner:* Site Reliability

## Next Steps for the Project
- Finalize UI/UX design based on stakeholder feedback.
- Update `api/feedback_api.py` to support webhook‑driven notifications.
- Publish the system architecture diagram (see `design_spec.md`) to the wiki.

*Prepared by: AI Compliance Assistant*