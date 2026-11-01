# az401-agentops

AZ-401 lab: FastAPI service delivered via Azure Pipelines and GitHub Actions
Health check: `GET /health` returns the service status.

## Branch strategy

AgentOps uses GitHub flow.

- `main` is always deployable and protected by the ruleset `main-protection`.
- Work happens in short-lived branches named `feature/<name>`, `bugfix/<name>` or `hotfix/<name>`.
- Every change reaches `main` through a pull request; the branch is deleted after the merge.
- Releases are marked with tags `vX.Y.Z` on `main`.

