# Vaultic - Password Manager - Project Planning

## Purpose
An offline, local-first password manager built in Python to securely store, generate, and manage credentials without 
replying on any cloud service.

## User Stories
- As a user, I want to create a master password so that only I can access my vault.
- As a user, I want to add a new password entry so that I can store credentials for a site/app.
- As a user, I want to retrieve a stored password so that I can log in to a service.
- As a user, I want to search my entries by name so that I can find credentials quickly.
- As a user, I want to update an existing entry so that I can keep my credentials current.
- As a user, I want to delete an entry so that I can remove credentials I no longer need.
- As a user, I want to generate a strong random password so that I don't reuse weak passwords.
- As a user, I want to see a strength indicator for passwords I type manually.

## MVP Scope (v1)
- [ ] Master password authentication
- [ ] Encrypted local storage (SQLite)
- [ ] Add / view / update / delete password entries
- [ ] password generator integrated into entry creation
- [ ] Basic search by entry name

## Postponed (v2+)
- [ ] Categories / tags
- [ ] Notes field
- [ ] Clipboard auto-clear
- [ ] Auto-lock
- [ ] Import / export
- [ ] backup / restore

## Non-Goals (explicitly out of scope)
- No cloud sync
- No multi-user support
- No browser extension / autofill
- No mobile app

## Constraints
- Single user, single master password
- Fully offline, no network calls
- CLI-based interface for v1

## Definition of Done (v1)
- [ ] User can create a vault with a master password
- [ ] User can add, view, search, update, and delete entries via CLI
- [ ] All data is encrypted at rest - verifiable by inspecting the raw DB file directly
- [ ] Wrong master password is rejected without leaking any data or crashing
- [ ] Core logic (crypto, generator, strength check) has passing unit tests