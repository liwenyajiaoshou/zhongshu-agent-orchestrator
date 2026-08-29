import os
import sys
import json
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "README_部署与使用.md",
    "SKILL.md",
    "MANIFEST.json",
    "CHANGELOG.md",
    "RELEASE_GOVERNANCE.md",
    "policies/model-routing.yaml",
    "policies/governance-adapter.md",
    "policies/workspace-health.md",
    "policies/debug-escalation.md",
    "policies/execution-gating.md",
    "templates/stage-plan.md",
    "templates/stage-report.md",
    "templates/thread-handoff.md",
]

# Root duplicates check
FORBIDDEN_ROOT_FILES = [
    "model-routing.yaml",
    "governance-adapter.md",
    "workspace-health.md",
    "debug-escalation.md",
    "execution-gating.md",
    "stage-plan.md",
    "stage-report.md",
    "thread-handoff.md"
]

README_EXPECTED_STRINGS = [
    "debug-escalation.md",
    "execution-gating.md",
    "model-routing.yaml",
    "governance-adapter.md",
    "workspace-health.md",
    "stage-plan.md",
    "stage-report.md",
    "thread-handoff.md"
]

def check_required_files():
    errors = []
    for f in REQUIRED_FILES:
        if not Path(f).is_file():
            errors.append(f"Missing required file: {f}")
    return errors

def check_root_duplicates():
    errors = []
    for f in FORBIDDEN_ROOT_FILES:
        if Path(f).exists():
            errors.append(f"Forbidden duplicate file in root directory: {f}")
    return errors

def check_manifest():
    errors = []
    manifest_path = Path("MANIFEST.json")
    if not manifest_path.exists():
        return ["MANIFEST.json does not exist"]

    try:
        content = manifest_path.read_text(encoding='utf-8')
        data = json.loads(content)
        if not data.get("runtime_version"):
            errors.append("MANIFEST.json is missing 'runtime_version' field or it is empty.")
    except UnicodeDecodeError:
        errors.append("MANIFEST.json is not valid UTF-8.")
    except json.JSONDecodeError:
        errors.append("MANIFEST.json is not valid JSON.")
    return errors

def check_utf8():
    errors = []
    extensions = {".md", ".txt", ".json", ".yaml", ".yml"}
    # Walk through the repository, ignoring .git and other hidden dirs for simplicity,
    # but we will just check tracked files typically. Here we use os.walk.
    for root, dirs, files in os.walk("."):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in extensions:
                path = Path(root) / file
                try:
                    content = path.read_bytes()
                    text = content.decode('utf-8')
                    if '\ufffd' in text:
                        errors.append(f"File {path} contains Unicode replacement character ().")
                    if b'\x00' in content:
                        errors.append(f"File {path} contains null bytes.")
                except UnicodeDecodeError:
                    errors.append(f"File {path} is not valid UTF-8.")
    return errors

def check_readme_inclusions():
    errors = []
    for readme_file in ["README.md", "README_部署与使用.md"]:
        path = Path(readme_file)
        if not path.exists():
            continue
        try:
            content = path.read_text(encoding='utf-8')
            for exp in README_EXPECTED_STRINGS:
                if exp not in content:
                    errors.append(f"{readme_file} is missing expected string: {exp}")
        except Exception:
            pass # Handled by utf-8 check
    return errors

def main():
    print("Starting Repository Consistency Validation...")
    all_errors = []

    all_errors.extend(check_required_files())
    all_errors.extend(check_root_duplicates())
    all_errors.extend(check_manifest())
    all_errors.extend(check_utf8())
    all_errors.extend(check_readme_inclusions())

    if all_errors:
        print("\nValidation FAILED with the following errors:")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("\nValidation PASS. Repository consistency looks good.")
        sys.exit(0)

if __name__ == "__main__":
    main()
