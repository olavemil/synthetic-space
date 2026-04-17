# Immutable Audit-Log Architecture with Cryptographic Signing

## 1. Data Model for Tamper-Evident Logs
- **Log Entry Structure**
  - `timestamp`: ISO‑8601 UTC timestamp
  - `event_id`: UUIDv4 (uniqueness across systems)
  - `event_type`: enum('authentication','authorization','data_access','system_event')
  - `actor`: anonymized identifier (hashed name + role)
  - `payload_hash`: SHA‑256 hash of the event data (for integrity)
  - `signature`: RSA-PKCS#1 v1.5 signature over (timestamp, event_type, payload_hash)
  - `nonce`: random nonce for replay‑attack protection
  - `metadata`: JSON object for GDPR/CCPA fields (pseudonymized PII, data‑subject rights flags)

## 2. Cryptographic Signing Algorithm
- **Algorithm**: RSA‑PSS with SHA‑256 (FIPS 186‑4 compliant)
- **Key Management**
  - Private key stored in HSM (Hardware Security Module) or secure enclave
  - Public key published via a trusted PKI or Web of Trust
- **Signing Process**
  1. Serialize event data deterministically (sorted JSON).
  2. Compute SHA‑256 hash of the serialized data.
  3. Sign the hash with the private key.
  4. Append signature and signature‑header to the log entry.

## 3. Storage Format
- **File format**: JSON Lines (each line = one log entry)
- **Rotation & Retention**
  - Daily files, with `.old` suffix; keep 90 days (compressible)
  - Cold‑storage tier-3 object storage for archival copies
- **Compliance**: 
  - GDPR/CCPA anonymization rules enforced by hashing personal identifiers before logging
  - Right‑to‑be‑forgotten erasure via secure overwrite before deletion

## 4. Anonymization Rules
- All direct identifiers (name, email, SSN) hashed with Argon2id
- Indirect identifiers (IP, device fingerprint) perturbed to prevent re‑identification
- Periodic audit of stored PII hashes against a deletion schedule

## 5. Validation & Verification
- Verify signature on read‑through using the public key
- Detect tampering via mismatched `payload_hash` and re‑computed hash
- Generate a public audit report (PDF/A) on demand for regulators

## 6. Moral Scenario Integration
- Embed scenario identifiers in `metadata` for traceability
- Provide a mapping between events and ethical guidelines (e.g., fairness, transparency)
- Support optional “scenario mode” where logs are written to a separate immutable store for compliance testing

## 7. Outline of the Prototype
- **Phase 1**: Implement deterministic serialization & SHA‑256 hashing
- **Phase 2**: Integrate RSA-PSS signing in Python (cryptography library)
- **Phase 3**: Build a small in‑memory log that writes JSON Lines to disk
- **Phase 4**: Add GDPR‑compliant anonymization middleware
- **Phase 5**: Conduct a pilot audit with synthetic moral‑scenario data

This design ensures immutable, cryptographically signed logs that meet legal requirements while providing a clear audit trail for ethical compliance.