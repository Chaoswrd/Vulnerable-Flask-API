# Vulnerable Flask API
This repository will attempt to highlight some common programming mistakes.
It will primarily highlight the OWASP web security testing guide "vulnerabilites" in Flask.
This project exists to teach what can go wrong, it is not a good idea to expose this on a public network or to run in production.
The project runs in docker so it isn't exposed through any ports and so it is cross-platform (should work on ARM & x86).

## Dependencies
- Docker
- Python3
- gitleaks
- pre-commit

## Future Additions
- Kubernetes

# Security
Using GitLeaks and pre-commit to ensure that no private information is leaked
```bash
gitleaks detect --source . -v
```
Run the pre-commits commands
```bash
pre-commit autoupdate && pre-commit install
```