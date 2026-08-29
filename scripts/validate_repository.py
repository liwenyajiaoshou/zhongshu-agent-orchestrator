import os
import sys
import json
import subprocess
from pathlib import Path

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

def get_manifest_deployment_files():
    manifest_path = Path("MANIFEST.json")
    if not manifest_path.exists():
        return []
    try:
        content = manifest_path.read_text(encoding='utf-8')
        data = json.loads(content)
        return data.get("deployment_files", [])
    except Exception:
        return []

def check_required_files():
    errors = []
    required = get_manifest_deployment_files()
    # Also strictly require some maintenance files not in deployment_files
    always_required = ["MANIFEST.json", "CHANGELOG.md", "RELEASE_GOVERNANCE.md"]
    for f in required + always_required:
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
        if "deployment_files" not in data or not isinstance(data["deployment_files"], list):
            errors.append("MANIFEST.json is missing 'deployment_files' list.")
    except UnicodeDecodeError:
        errors.append("MANIFEST.json is not valid UTF-8.")
    except json.JSONDecodeError:
        errors.append("MANIFEST.json is not valid JSON.")
    return errors

def get_tracked_files():
    try:
        result = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()
    except Exception:
        return None

def check_utf8():
    errors = []
    extensions = {".md", ".txt", ".json", ".yaml", ".yml"}
    tracked_files = get_tracked_files()
    if tracked_files is None:
        errors.append("Git is not available or failed to run `git ls-files`.")
        return errors

    for file in tracked_files:
        ext = Path(file).suffix.lower()
        if ext in extensions:
            path = Path(file)
            if not path.exists():
                continue
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
    deployment_files = get_manifest_deployment_files()
    if not deployment_files:
        return errors # Handled by manifest check

    for readme_file in ["README.md", "README_部署与使用.md"]:
        path = Path(readme_file)
        if not path.exists():
            errors.append(f"Missing {readme_file}")
            continue
        try:
            content = path.read_text(encoding='utf-8')
            for exp in deployment_files:
                basename = Path(exp).name
                # Check for either the relative path or the basename
                if exp not in content and basename not in content:
                    errors.append(f"{readme_file} is missing expected reference to runtime file: {exp}")
        except Exception as e:
            errors.append(f"Failed to read {readme_file}: {str(e)}")
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
