import json
import os
import sys
import zipfile
from pathlib import Path

def main():
    print("Starting Runtime Pack Build (Secured)...")

    manifest_path = Path("MANIFEST.json")
    if not manifest_path.exists():
        print("Error: MANIFEST.json not found.")
        sys.exit(1)

    try:
        content = manifest_path.read_text(encoding='utf-8')
        data = json.loads(content)
        version = data.get("runtime_version")
        deployment_files = data.get("deployment_files")
    except Exception as e:
        print(f"Error parsing MANIFEST.json: {e}")
        sys.exit(1)

    if not version:
        print("Error: 'runtime_version' is missing or empty in MANIFEST.json")
        sys.exit(1)

    if not isinstance(deployment_files, list):
        print("Error: 'deployment_files' is missing or not a list in MANIFEST.json")
        sys.exit(1)

    # Manifest Validations
    seen = set()
    repo_root = Path.cwd().resolve()

    for f in deployment_files:
        if not isinstance(f, str) or not f.strip():
            print(f"Error: deployment_files contains non-string or empty item: {f}")
            sys.exit(1)
        if f in seen:
            print(f"Error: deployment_files contains duplicate entry: {f}")
            sys.exit(1)
        seen.add(f)

    package_files = list(deployment_files)
    if "MANIFEST.json" not in package_files:
        package_files.append("MANIFEST.json")

    # Security Validations
    for f in package_files:
        p = Path(f)
        if p.is_absolute():
            print(f"Error: Absolute path not allowed: {f}")
            sys.exit(1)
        if '..' in p.parts:
            print(f"Error: Path traversal (..) not allowed: {f}")
            sys.exit(1)

        if not p.is_file():
            print(f"Error: File does not exist or is not a regular file: {f}")
            sys.exit(1)

        try:
            resolved_p = p.resolve(strict=True)
        except Exception as e:
            print(f"Error: Could not resolve path {f}: {e}")
            sys.exit(1)

        if not str(resolved_p).startswith(str(repo_root)):
            print(f"Error: Path resolves outside repository root: {f} -> {resolved_p}")
            sys.exit(1)

    # Ensure dist folder exists
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    zip_filename = dist_dir / f"Zhongshu_Runtime_Deployment_Pack_{version}.zip"

    print(f"Building {zip_filename}...")

    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in package_files:
                zipf.write(file, arcname=file)
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        sys.exit(1)

    # Verify ZIP contents
    print("Verifying ZIP contents...")
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zip_files = set(zipf.namelist())
            expected_files = set(package_files)

            if zip_files != expected_files:
                print("Error: ZIP contents do not match deployment_files exactly.")
                print(f"Expected: {expected_files}")
                print(f"Found: {zip_files}")
                sys.exit(1)

            for zf in zip_files:
                zp = Path(zf)
                if '..' in zp.parts or zp.is_absolute() or zf.startswith('/') or zf.startswith('\\'):
                    print(f"Error: Invalid path in ZIP: {zf}")
                    sys.exit(1)

    except Exception as e:
        print(f"Error verifying ZIP file: {e}")
        sys.exit(1)

    print(f"Build SUCCESS: {zip_filename}")
    sys.exit(0)

if __name__ == "__main__":
    main()
