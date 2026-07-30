# 🔒 Security Policy

Welcome to the **AI Resume Evaluator & ATS Checker** Security Policy.

The security of this project and its users is our highest priority. We appreciate the efforts of security researchers, contributors, and the open-source community in helping identify and responsibly disclose security vulnerabilities.

---

# 🛡️ Supported Versions

The following versions of this project currently receive security updates.

| Version | Supported |
|----------|-----------|
| Latest Release | ✅ Yes |
| Development Branch | ✅ Yes |
| Previous Releases | ❌ No |
| Older Versions | ❌ No |

---

# 🚨 Reporting a Security Vulnerability

If you discover a security issue, **please do not create a public GitHub Issue**, as doing so may expose users to unnecessary risk.

Instead, please report it responsibly by:

- Opening a **Private Security Advisory** on GitHub (if enabled).
- Contacting the project maintainer directly through GitHub.
- Providing a detailed report including reproduction steps.

A good security report should include:

- Vulnerability description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Impact assessment
- Affected files or modules
- Screenshots or logs (if applicable)
- Suggested mitigation (optional)

---

# ⏱️ Response Timeline

We aim to respond according to the following timeline:

| Action | Expected Time |
|---------|---------------|
| Initial Response | Within 48 Hours |
| Vulnerability Assessment | 3–5 Days |
| Fix Development | Depends on Severity |
| Public Disclosure | After Security Patch |

---

# 🔐 Responsible Disclosure

We kindly request that you:

- Do not publicly disclose vulnerabilities before they are fixed.
- Give maintainers reasonable time to investigate.
- Avoid accessing or modifying user data.
- Avoid disrupting project availability.
- Report findings responsibly and ethically.

Responsible disclosure helps protect users and improves the security of the project.

---

# 🔍 Security Scope

This policy applies to:

- Streamlit Web Application
- Resume Parsing Module
- PDF & DOCX Processing
- ATS Score Calculation
- NLP Skill Extraction
- Resume Section Detection
- Job Role Prediction
- Dashboard Components
- Project Source Code

---

# 📂 Third-Party Dependencies

This project depends on several open-source libraries.

Examples include:

- Streamlit
- Pandas
- Scikit-learn
- PDFPlumber
- Python-docx
- Plotly
- NumPy

Please ensure these dependencies remain updated.

We recommend checking for vulnerabilities regularly using:

```bash
pip list --outdated
```

or

```bash
pip-audit
```

---

# 🛠 Security Best Practices

When using this project, we recommend the following:

- Always use the latest stable version.
- Keep Python updated.
- Keep dependencies updated.
- Use trusted resume files.
- Avoid uploading confidential personal information to public deployments.
- Review external libraries before installation.
- Enable HTTPS when deploying online.
- Protect deployment secrets using environment variables.
- Do not commit API keys or credentials.

---

# ☁️ Deployment Security

If deploying the application publicly:

- Enable HTTPS
- Secure environment variables
- Restrict administrative access
- Keep the server updated
- Monitor application logs
- Enable GitHub Dependabot
- Use strong authentication

---

# 📊 Security Recommendations

For developers:

- Follow secure coding practices.
- Validate all user inputs.
- Handle file uploads safely.
- Limit file size during uploads.
- Prevent directory traversal attacks.
- Avoid executing arbitrary user input.
- Sanitize extracted resume text.
- Keep dependencies patched.

---

# 🔄 Dependency Management

Regularly update project packages:

```bash
pip install --upgrade pip

pip install -r requirements.txt --upgrade
```

Recommended tools:

- GitHub Dependabot
- pip-audit
- Safety CLI
- Bandit

---

# 🚫 Out of Scope

The following are generally outside the scope of this policy:

- Third-party service vulnerabilities
- Browser-specific issues
- Local machine configuration
- Operating system vulnerabilities
- Internet connectivity issues

---

# 🤝 Security Contributions

Security improvements are always welcome.

You can contribute by:

- Identifying vulnerabilities
- Improving input validation
- Optimizing file handling
- Enhancing authentication
- Updating dependencies
- Improving documentation
- Suggesting secure coding practices

---

# 📜 Security Disclosure Policy

Security vulnerabilities will be disclosed only after:

- Investigation
- Validation
- Patch Development
- Testing
- Official Release

This process helps protect users while maintaining transparency.

---

# ❤️ Acknowledgements

We sincerely thank all contributors, researchers, and security enthusiasts who help improve the security of this project through responsible disclosure.

Your contributions help create a safer experience for everyone.

---

# 📄 Contact

For security-related concerns, please contact the project maintainer through GitHub.

Thank you for helping keep **AI Resume Evaluator & ATS Checker** secure.
