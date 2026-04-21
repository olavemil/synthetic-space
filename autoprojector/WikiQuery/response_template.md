# Response Generation Template

This template ensures reproducibility, traceability, and auditability of generated responses. It includes source anchors, metadata tags, timestamps, and contextual information.

## Template Structure

```
[Source: <URL> (v<version>)]
<Timestamp>

### Response Content
[Response text here...]

### Metadata Tags
- **Confidence**: <High/Medium/Low>
- **Tags**: [ambiguity, critical_fact]

### Source Citations
1. <Source 1>
2. <Source 2>
...

### Ethical-Clearance Note
[Ethical considerations or notes here...]
```

## Workflow for Response Generation

1. **Source Identification**: Extract and validate the source URL, version number, and timestamp.
2. **Content Generation**: Generate response content based on the input query and available knowledge sources.
3. **Metadata Tagging**: Assign confidence levels, contextual tags (e.g., ambiguity), and ethical considerations.
4. **Source Citations**: List all sources used for generating the response, including URLs and version numbers.
5. **Verification**: Ensure all metadata tags contain valid URLs and version numbers before finalizing the output.

## Example Output Format

```
[Source: https://en.wikipedia.org/wiki/Example (v2024.1)]
2024-05-30T12:00:00Z

### Response Content
Example response content generated based on the query about Example.

### Metadata Tags
- **Confidence**: High
- **Tags**: [critical_fact]

### Source Citations
1. https://en.wikipedia.org/wiki/Example (v2024.1)

### Ethical-Clearance Note
No ethical concerns identified for this response.
```

## Traceability Matrix

| Requirement | Source Doc |
|-------------|-----------|
| Traceability Matrix | README.md |
| Source Fingerprinting | design_spec.md |
