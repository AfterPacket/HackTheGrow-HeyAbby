# HackTheGrow-HeyAbby

[![License: GPL-3.0](https://img.shields.io/badge/license-GPLv3-green.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security Research](https://img.shields.io/badge/focus-security%20research-critical.svg)](#)

A comprehensive **security research and protocol analysis toolkit** documenting an API security assessment of the HeyAbby Grow Box mobile application. This repository demonstrates proper responsible disclosure practices combined with technical security research methodology.

> ⚠️ **ETHICAL USE ONLY**
>
> This project is intended strictly for authorized security research, defensive analysis, responsible disclosure, and educational purposes. Unauthorized testing of systems you do not own or have explicit written permission to test may be illegal.

---

## 📋 Table of Contents

- [Project Purpose](#-project-purpose)
- [Ethical Framework](#-ethical-framework)
- [Research Methodology](#-research-methodology-overview)
- [Traffic Interception](#️-traffic-interception-with-proxyman)
- [API Endpoints](#-identified-api-endpoints)
- [Request Reconstruction](#-controlled-request-replay-python)
- [Findings](#-findings--observations)
- [Responsible Disclosure](#️-responsible-disclosure)
- [Repository Structure](#-repository-structure)
- [Learning Resources](#-learning-resources)
- [License](#-license)

---

## 🧠 Project Purpose

`HackTheGrow-HeyAbby` demonstrates how mobile applications communicate with backend APIs, how security controls can fail, and how researchers can responsibly identify and report vulnerabilities.

This is **not** a weaponized exploit kit. Rather, it's a **documented research workflow** that combines:

- ✅ Mobile traffic interception techniques
- ✅ API endpoint identification and reconstruction
- ✅ Controlled HTTP testing methodologies
- ✅ Responsible disclosure best practices
- ✅ Detailed technical documentation

---

## 🛡️ Ethical Framework

This research was conducted under the following principles:

| Principle | Implementation |
|-----------|-----------------|
| **Authorization** | Conducted on systems owned/controlled by researcher |
| **Transparency** | Full disclosure of methodology and findings |
| **Non-Exploitation** | No unauthorized data access or system modification |
| **Responsible Timing** | Vendors notified before any public disclosure |
| **Educational Value** | Findings documented to improve security awareness |

---

## 🔍 Research Methodology Overview

The assessment followed a standard **mobile API security research pipeline**:

```
Traffic Interception
    ↓
Endpoint Identification
    ↓
Request Reconstruction
    ↓
Controlled Replay
    ↓
Data Exposure Analysis
    ↓
Responsible Disclosure
```

Each step is documented in detail below.

---

## 🕵️ Traffic Interception with Proxyman

### Why Proxyman?

[Proxyman](https://proxyman.io/) is a professional-grade HTTP/HTTPS debugging proxy for macOS and iOS that enables full inspection of mobile app traffic without requiring access to application source code.

**Key capabilities used:**

- 🔐 TLS interception with custom certificate installation
- 👁️ Real-time request/response inspection
- 📋 Complete header and payload visibility
- 🔄 Request replay and export functionality
- 📱 Mobile device trust management

### Implementation Steps

1. **Certificate Installation**: Proxyman root certificate installed on iOS device
2. **Traffic Routing**: HeyAbby mobile app traffic routed through Proxyman proxy
3. **Decryption**: HTTPS requests decrypted and inspected in real-time
4. **Analysis**: API endpoints, headers, and payload structures identified
5. **Export**: Requests exported and reconstructed for offline analysis

**Result**: Discovery of previously undocumented API endpoints and sensitive data exposure patterns.

---

## 🔗 Identified API Endpoints

### Endpoint 1: Automatic Login

```
POST https://www.beheyabby.com:9330/abby/user/app/automaticLogin
```

**Purpose:**
- Handles silent/automatic authentication for the mobile application
- Accepts device metadata and session context
- Returns authentication tokens and session data

**Key Observation**: Backend accepts device information without proper validation.

### Endpoint 2: User Details

```
POST https://www.beheyabby.com:9330/abby/user/userDetail
```

**Purpose:**
- Returns comprehensive user profile information
- Provides device state and configuration data
- Includes subscription information

**Key Observation**: Response data exceeds what's necessary for client-side functionality.

---

## 🧪 Controlled Request Replay (Python)

The following script demonstrates how a captured mobile request can be safely reconstructed and analyzed in a controlled environment.

> 🔒 **Note**: All authentication tokens, API secrets, and personally identifiable information have been removed or redacted.

### Automatic Login Request

```python
import requests
import json
from typing import Dict, Any

# Configuration
TARGET_URL = "https://www.beheyabby.com:9330/abby/user/app/automaticLogin"

def build_headers() -> Dict[str, str]:
    """Reconstruct headers from observed mobile traffic (PII removed)."""
    return {
        "Host": "www.beheyabby.com:9330",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US;q=1",
        "User-Agent": "UniversalApp/3.1.0 (iPhone; iOS 17.1)",
        "Connection": "keep-alive",
        "token": "[REDACTED]"  # Authentication token removed
    }

def build_payload() -> Dict[str, Any]:
    """Construct request payload with device metadata (PII removed)."""
    return {
        "mobileModel": "iPhone 13 Pro Max",
        "mobileBrand": "apple",
        "version": "3.1.0",
        "channel": "appstore",
        "osType": 2,
        "timeZone": -14400,
        "city": "[REDACTED]"  # User location removed
    }

def send_request() -> None:
    """Execute controlled request and analyze response."""
    headers = build_headers()
    payload = build_payload()
    
    print(f"[*] Sending request to: {TARGET_URL}")
    print(f"[*] Payload: {json.dumps(payload, indent=2)}\n")
    
    try:
        response = requests.post(
            TARGET_URL,
            headers=headers,
            json=payload,
            verify=True  # Always verify SSL in production
        )
        
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Response Headers:\n{json.dumps(dict(response.headers), indent=2)}")
        print(f"\n[+] Response Body:\n{response.text}\n")
        
        # Log response for analysis
        if response.status_code == 200:
            data = response.json()
            print("[+] Successfully parsed JSON response")
            print(f"[+] Response keys: {list(data.keys())}")
        else:
            print(f"[-] Unexpected status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Request failed: {e}")
    except json.JSONDecodeError:
        print("[-] Response was not valid JSON")

if __name__ == "__main__":
    send_request()
```

### Code Walkthrough

**Imports & Setup**
```python
import requests  # HTTP client library
import json      # JSON serialization
```

**Header Reconstruction** (`build_headers()`)
- Mimics legitimate mobile application requests
- Demonstrates how authentication context is passed
- Includes device identification headers
- Sensitive values removed for safety

**Payload Construction** (`build_payload()`)
- Represents device and application metadata
- Shows backend reliance on client-provided values
- Demonstrates data validation gaps

**Request Execution** (`send_request()`)
- Sends POST request identical in structure to mobile app
- Validates response parsing
- Handles errors gracefully
- Logs results for analysis

---

## 📊 Findings & Observations

### Data Exposure Analysis

The `userDetail` endpoint returned substantially more information than necessary for normal client functionality:

#### User-Level Data Returned
- Account identifiers (user ID, account numbers)
- Email address
- Display name
- Subscription status and tier
- Billing information

#### Device-Level Data Returned
- Device serial numbers and identifiers
- Online/offline operational status
- Grow box configuration parameters
- Plant cycle metadata
- Historical sensor readings

### Key Security Findings

| Finding | Severity | Description |
|---------|----------|-------------|
| **Overprivileged API Response** | High | API returns more data than client needs |
| **Insufficient Input Validation** | Medium | Backend accepts unvalidated client metadata |
| **Session Token Exposure Risk** | High | Token compromise exposes full user profile |
| **Missing Rate Limiting** | Medium | No apparent request throttling observed |

### Risk Impact

If an authentication token were compromised, an attacker could:
- ✗ Access complete user profile data
- ✗ View device configuration details
- ✗ Retrieve historical sensor data
- ✗ Potentially manipulate device settings

---

## 🛡️ Responsible Disclosure

### Disclosure Timeline

| Date | Action |
|------|--------|
| **Initial Discovery** | Findings identified during authorized testing |
| **Vendor Notification** | HeyAbby staff contacted via official channels |
| **Direct Communication** | Issues discussed via Discord and email |
| **Acknowledgment** | Vendor acknowledged receipt of report |
| **Public Documentation** | Repository created for educational purposes |

### Best Practices Followed

✅ **No data was published before disclosure**  
✅ **No unauthorized access was continued after confirmation**  
✅ **Direct communication with vendor maintained**  
✅ **Findings reported with clear remediation guidance**  
✅ **This project documents process, not exploitation**  

---

## 🤝 Community & Transparency

As a positive outcome of responsible disclosure, this research was acknowledged by HeyAbby staff, reinforcing the value of ethical security research and open communication between security researchers and vendors.

**The goal**: Help organizations improve security posture while maintaining trust and professionalism.

---

## 📦 Repository Structure

```
HackTheGrow-HeyAbby/
├── README.md              # This document
├── LICENSE                # GNU GPL v3.0
├── SECURITY.md            # Security policy
├── examples/              # Sanitized request examples
│   ├── automatic_login.json
│   └── user_detail.json
├── scripts/               # Research tooling
│   ├── request_replay.py
│   └── response_analyzer.py
└── docs/                  # Detailed methodology
    ├── methodology.md
    ├── findings.md
    └── responsible_disclosure.md
```

---

## 📄 License

Licensed under **GNU GPL v3.0**

- Free to use, modify, and share
- Derivatives must remain open source
- No warranty provided
- See [LICENSE](LICENSE) for full terms

---

## 📚 Learning Resources

### Security Research & Mobile Security

- 🔗 [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)
- 🔗 [OWASP API Security](https://owasp.org/www-project-api-security/)
- 🔗 [OWASP Web Top 10](https://owasp.org/www-project-top-ten/)

### Tools & Documentation

- 🔗 [Proxyman Official Site](https://proxyman.io)
- 🔗 [Python Requests Library](https://docs.python-requests.org/)
- 🔗 [Burp Suite Community](https://portswigger.net/burp/communitydownload)

### Responsible Disclosure

- 🔗 [OWASP Responsible Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Responsible_Disclosure_Cheat_Sheet.html)
- 🔗 [HackerOne Disclosure Guidelines](https://www.hackerone.com/disclosure-guidelines)

---

## 🧭 Final Thoughts

This repository demonstrates:

- ✅ How mobile APIs can be analyzed safely and responsibly
- ✅ Why traffic interception and protocol analysis matter
- ✅ How overprivileged APIs create unnecessary risk
- ✅ The importance of proper responsible disclosure processes
- ✅ How security research strengthens systems and builds trust

**Key takeaway**: Security research is fundamentally about improving systems and protecting users—not breaking trust or exploiting vulnerabilities for personal gain.

---

## 📮 Contributing

If you have improvements to the documentation, additional research insights, or better practices to share, please consider contributing via pull requests or issues.

---

## ⚖️ Disclaimer

This project is provided for **educational and authorized security research purposes only**. Users are solely responsible for complying with all applicable laws and regulations. Unauthorized access to computer systems is illegal.

---

**Stay curious. Stay ethical. Stay responsible.** 🔒
