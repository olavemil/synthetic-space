# Cryptographic Signing Requirements for Immutable Audit Logs

## 1. Hashing Algorithm
We mandate the use of **SHA-256** as the core cryptographic hash function. This algorithm provides a strong balance between security and performance, and is widely supported across all modern platforms.

## 2. Signature Scheme
All audit entries must be signed using **ECDSA with the secp256k1 curve**. This scheme is widely adopted in blockchain and cryptographic libraries, offering robust security guarantees while maintaining efficiency.

## 3. Key Management
- **Key Type:** ECDSA‑secp256k1 keys.
- **Key Storage:** Private keys shall be stored in hardware security modules (HSMs) or secure enclaves, with no plaintext exposure.
- **Key Rotation:** Keys must be rotated at least annually or upon compromise, whichever occurs first.
- **Backup:** A BIP‑32‑compatible seed phrase must be generated and stored offline.

## 4. Log Immutability
Each log entry is hashed, and the hash of the previous entry is included to form a chain. The resulting chain is signed as a single unit, ensuring that any tampering is immediately detectable.

## 5. Verification Process
Auditors must verify the signature against the public key, check the integrity of the hash chain, and confirm that the current hash matches the expected value.

## 6. Governance
All cryptographic parameters must be documented in the project’s security policy and reviewed by the compliance team before deployment.

> This specification ensures that audit logs are cryptographically secure, tamper-evident, and aligned with best practices for key management and digital signatures.