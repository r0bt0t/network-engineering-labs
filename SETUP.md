# Lab Index Automation — Setup

This package contains two files:

```text
scripts/generate_lab_index.py
.github/workflows/update-lab-index.yml
```

## What it does

The generator:

- scans **every direct folder inside `labs/`**
- recognises numbered folders such as `001-Basic-Switch-Configuration`
- also includes non-numbered folders if you ever add any
- derives a readable lab title from the folder name
- infers a **primary subject area**
- infers **relevant networking skills** from the lab title
- checks whether `README.md` exists
- checks for `evidence/raw-cli-output.md`, `evidence/README.md`, or an `evidence/` folder
- rebuilds the visual lab catalogue
- rebuilds the **Skills Progression & Coverage** section
- preserves all hand-written content outside the generated sections

No YAML/front-matter metadata is required in individual lab folders.

## First installation

Copy the two files into the same paths in your repository.

From the repository root, run:

```powershell
python scripts/generate_lab_index.py
```

The first run recognises the existing:

- `## Completed Labs`
- `## Skills Progression Map`

and replaces those sections with generated content.

Review the result:

```powershell
git diff -- Lab-index.md
```

Then commit the automation:

```powershell
git add scripts/generate_lab_index.py .github/workflows/update-lab-index.yml Lab-index.md
git commit -m "feat: automate lab catalogue and skills index"
git push
```

## What happens after that

Any push to `main` that changes something under:

```text
labs/**
```

runs the GitHub Action.

If the generated `Lab-index.md` changes, the action commits the new version using the GitHub Actions bot.

A bot commit containing only `Lab-index.md` does **not** retrigger the workflow because `Lab-index.md` is deliberately absent from the workflow's `paths` filter.

## Adding a future lab

Your normal workflow remains:

```text
labs/074-Example-New-Lab/
```

Add the lab files, commit and push. The index is then regenerated automatically.

## Changing categorisation or skill inference

All inference rules are centralised near the top of:

```text
scripts/generate_lab_index.py
```

Edit:

- `SKILL_RULES` to add or refine title → skill mappings
- `CATEGORY_RULES` to change title → subject-area mappings
- `CATEGORY_DESCRIPTIONS` to change the explanatory text displayed on the page

This avoids adding metadata to 73 existing labs.

## Manual verification

To check whether the index is current without writing anything:

```powershell
python scripts/generate_lab_index.py --check
```

Exit code `0` means it is current. Exit code `1` means regeneration would change `Lab-index.md`.
