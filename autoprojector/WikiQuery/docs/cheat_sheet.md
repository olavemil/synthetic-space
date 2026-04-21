# Glass Atrium Architecture & Deployment Cheat Sheet

## Overview
- Purpose: Quick reference for architecture, deployment, and governance.
- Audience: Developers, ops, stakeholders.

## Architecture Overview
- **Components**: Frontend, API Gateway, Backend Services, Database, CI/CD Pipeline.
- **Key Flows**: Request → API → Service → DB → Response.
- **Versioning**: Semantic versioning (vX.Y.Z).

## Deployment Steps
1. **Prerequisites**: Install Docker/Kubernetes and kubectl.
2. **Clone repository**: `git clone <repo-url>`.
3. **Install dependencies**:
   - Frontend: `npm install`
   - Backend: `pip install -r requirements.txt`
4. **Build artifacts**:
   - Frontend: `npm run build`
   - Backend: `npm install --production`
5. **Deploy to staging**:
   - Apply Kubernetes manifests: `kubectl apply -f k8s/staging.yaml`
6. **Run smoke tests** to validate deployment.
7. **Promote to production**:
   - Apply production manifests: `kubectl apply -f k8s/prod.yaml`
   - Start app: `npm start`

## How to Run
```bash
# Install in-memory dependencies (no install needed)
npm ci

# Build frontend assets
npm run build

# Start dev server
npm start
```

## Development Environment Setup
```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
alembic upgrade head

# Start application server
python app.py
```

## Documentation Structure Checklist
- [x] Overview
- [x] Architecture
- [x] API Reference (TODO)
- [ ] Deployment
- [x] Changelog
- [ ] Lessons Learned
- [ ] Version & Revision History

## Version & Revision History
| Version | Date       | Summary                              | Author |
|---------|------------|--------------------------------------|--------|
| 0.1.0   | 2025-11-03 | Initial release                       | AI     |

## Lessons Learned
- Early changelog integration improved traceability.
- Clear deployment scripts reduced onboarding time.
- Documentation checklist helped track missing sections.

## Allowed / Blocked Operations
- **Allowed**: Creating new markdown files, updating existing docs, adding code snippets.
- **Blocked**: Modifying production database schemas without review.

## Sample Configuration (config.yaml)
```yaml
service_name: GlassAtrium
environment: staging
api_endpoint: https://api.staging.example.com
logging:
  level: INFO
```

## Quick Reference Table
| Command                     | Description                          |
|-----------------------------|--------------------------------------|
| `npm install`               | Install dependencies                  |
| `npm run build`             | Build frontend/backend artifacts     |
| `kubectl apply -f <manifest>` | Deploy to Kubernetes                 |
| `npm start`                  | Start app in development mode         |
| `kubectl rollout restart deployment/service` | Rollback deployment |

---

## Changelog Entry
**v1.2 - 2025-11-03:** Added OAuth support, improved rate limiting, and updated database connection pool.

## Deployment Prerequisites
- **Kubernetes**: Must have admin rights to apply manifests.
- **kubectl**: Ensure `kubectl` is configured with the correct context.
- **Docker**: Images must be pushed to a registry accessible by the cluster.

## Troubleshooting Tips
- **Error 403**: Verify IAM roles have sufficient permissions.
- **Service Unavailable**: Check pod logs with `kubectl logs <pod>`.
- **Database Connection Failed**: Ensure the service can reach the DB endpoint.

## Version-Specific Notes
- **Breaking Changes**: None in this release, but review the API changes documentation for deprecated fields.

## Links to Documentation
- [Deployment Guide](#)
- [API Reference](#) - Coming soon
- [ Design Decisions](#) - Coming soon

This cheat sheet provides a concise overview of the Glass Atrium system, covering architecture, deployment workflow, and governance essentials. Use it as a quick reference for onboarding, troubleshooting, and onsite discussions.

---

*Generated with AI assistance.*