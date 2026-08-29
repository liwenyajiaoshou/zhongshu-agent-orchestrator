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

def get_manifest_project_files():
    manifest_path = Path("MANIFEST.json")
    if not manifest_path.exists():
        return [], None
    try:
        content = manifest_path.read_text(encoding='utf-8')
        data = json.loads(content)
        sources = data.get("project_source_files", [])
        instructions = data.get("project_instructions_file", None)
        return sources, instructions
    except Exception:
        return [], None

def check_required_files():
    errors = []
    sources, instructions = get_manifest_project_files()
    if instructions:
        sources.append(instructions)

    always_required = ["MANIFEST.json", "CHANGELOG.md", "RELEASE_GOVERNANCE.md", "START_HERE.md"]
    for f in sources + always_required:
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
        if "project_source_files" not in data or not isinstance(data["project_source_files"], list):
            errors.append("MANIFEST.json is missing 'project_source_files' list.")
        if "project_instructions_file" not in data or not isinstance(data["project_instructions_file"], str):
            errors.append("MANIFEST.json is missing 'project_instructions_file' string.")
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

    # Check README.md Quick Start concepts
    readme_path = Path("README.md")
    if readme_path.exists():
        try:
            content = readme_path.read_text(encoding='utf-8')
            required_concepts = [
                "Latest Runtime Pack",
                "project-upload",
                "PROJECT_INSTRUCTIONS.txt",
                "ZHONGSHU_RUNTIME_READY"
            ]
            for concept in required_concepts:
                if concept not in content:
                    errors.append(f"README.md is missing required concept: {concept}")
        except Exception as e:
            errors.append(f"Failed to read README.md: {str(e)}")

    # Check START_HERE.md concepts
    starthere_path = Path("START_HERE.md")
    if starthere_path.exists():
        try:
            content = starthere_path.read_text(encoding='utf-8')
            required_concepts = [
                "project-upload",
                "PROJECT_INSTRUCTIONS.txt",
                "ZHONGSHU_RUNTIME_READY"
            ]
            for concept in required_concepts:
                if concept not in content:
                    errors.append(f"START_HERE.md is missing required concept: {concept}")
        except Exception as e:
            errors.append(f"Failed to read START_HERE.md: {str(e)}")

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
