# Architecture

## Overview
This project follows a layered architecture with five layers, each with a single responsibility. Dependencies only flow 
downward - layer may call the layer directly below it, never the reverse.

## Layers

### 1. CLI Layer (`app/cli/`)
Handles user input/output only. Parses commands (via `click`), calls into the Service layer, and formats results for 
display. Contains no business logic and no direct storage/crypto access.

### 2. Service Layer (`app/services/`)
Orchestrates business operations (e.g., "add a new entry" = validate input → encrypt sensitive fields via core → persist 
via Storage). Application rules live here, not in the CLI or storage layers.

### 3. Core Layer (`app/core/`)
Pure logic with no external dependencies on files or databases:
- Encryption / decryption
- Key derivation from the master password
- Password generation
- Password strength evaluation

This layer has no side effects, making it the most straightforward to unit test in isolation.

### 4. Model Layer (`app/models/`)
Data structures (e.g., "PasswordEntity", "VaultMetadata") with minimal behavior - primary field validation, not business 
logic.

### 5. Storage Layer (`app/storage/`)
The only layer aware that SQLite exists. Handles rendering and writing encrypted data to disk. If the storage technology 
changes later, only this layer is affected.

## Dependency Rule
CLI → Services → Core / Models → Storage

No layer imports "upward". For example, `core/` must never import from `cli/` or `services/`.

## Why This Structure
Keeping crypto logic isolated in `core/` (rather than scattered through CRUD or LCI code) means encryption can be added, 
audited, ot swapped without touching unrelated layers - critical for a security-sensitive application like this one.