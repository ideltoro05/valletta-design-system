# Valletta design system — instructions for Claude

This repo is the Valletta Industries brand system plus every finished presentation.
"Balada" in meeting transcripts means Valletta. Mission Protect is Valletta's training
platform; "SOC" is the Valletta SOC sub-brand.

## Making anything client-facing

- Follow `DESIGN_SYSTEM.md` (and `tokens.json`) for decks, one-pagers and documents:
  black / red `#FF002B` / white, Cambria headlines, Calibri or Arial body, red corner-tick motif.
- Use the real files in `assets/` (logos, Mission Protect screenshots). Look in `decks/` for
  finished decks to match.
- Build presentations as `.pptx` unless the user asks for another format.
- This repo is **public**. Never commit credentials or unblurred personal data (names,
  emails, phone numbers in screenshots). Blur them before capturing.

## Before starting

Pull the latest `main` so you build on the newest files.

## When a presentation is finished (always do every step)

1. **Save it in the repo:** `decks/Valletta_<Client>_<Topic>.pptx`, with any screenshots it
   used in `decks/<same name>_screenshots/`.
2. **Push it to GitHub** (`ideltoro05/valletta-design-system`): commit on a branch, push,
   open a pull request into `main` and merge it, so the file is on `main`.
3. **Upload it to Google Drive**, into the client's folder inside the
   [Valletta Industries](https://drive.google.com/drive/folders/1rJkLz4tiAWmZFyTm9ni3WwqvPacGXpYa) folder:
   - HHS → `HHS Training/Presenation`
   - General capability or business-development decks → `Biz Development`
   - Any other client → that client's folder. If there isn't one, ask before creating it.

   With Google Drive for desktop installed, copy the file into the synced folder
   (macOS: `~/Library/CloudStorage/GoogleDrive-<account>/`, under `My Drive` or
   `Shared drives`). Otherwise ask the user to drag the file into the folder.
4. **Tell the user** where the file is on GitHub and in Drive.

If a deck was edited in Google Slides or PowerPoint after it was uploaded, copy the newest
version from Drive into `decks/` before changing anything, so their edits aren't overwritten.

Never put this Git repo inside the Google Drive folder: Drive sync can corrupt it.
