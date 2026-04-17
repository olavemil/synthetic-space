# Moral Scenario Template

This template defines a moral scenario as a prompt paired with an associated bias‑mitigation protocol. It is designed to establish a unified, auditable framework for ethical LLM constraints.

## Template Structure

### 1. Scenario Prompt
Describe the moral scenario or ethical dilemma that will be presented to the LLM. This should include:
- **Context**: Background information or setting for the scenario.
- **Characters/Entities Involved**: Key participants in the dilemma (e.g., user, assistant, third parties).
- **Objective**: The goal or desired outcome of the interaction.

**Example:**
```markdown
### Scenario Prompt: Privacy vs. Transparency
- **Context**: A user requests assistance with a sensitive personal issue.
- **Characters/Entities Involved**: User, LLM Assistant
- **Objective**: Provide support while respecting user privacy and avoiding unnecessary disclosure.
```

### 2. Bias-Mitigation Protocol
Specify the protocol or constraints to mitigate biases and ensure ethical responses:
- **Constraints**: Rules or guidelines for the LLM (e.g., avoid stereotypes, ensure inclusivity).
- **Tone Guidelines**: Desired tone of the dialogue (e.g., empathetic, neutral).
- **Testing Criteria**: Metrics or methods to evaluate the effectiveness of the protocol (e.g., user feedback, tone analysis).

**Example:**
```markdown
### Bias-Mitigation Protocol: Privacy vs. Transparency
- **Constraints**: 
  - Do not ask for unnecessary personal details.
  - Avoid assumptions based on user demographics.
- **Tone Guidelines**: Maintain an empathetic and neutral tone throughout the interaction.
- **Testing Criteria**: 
  - Conduct user surveys to assess comfort and trust levels.
  - Analyze dialogue tone for neutrality using sentiment analysis tools.
```

### 3. Expected Output
Define the expected output or behavior of the LLM under this scenario:
- **Dialogue Example**: A sample interaction demonstrating adherence to the protocol.
- **Success Metrics**: How the protocol influences output quality, user satisfaction, and ethical compliance.