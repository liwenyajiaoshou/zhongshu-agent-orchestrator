import json
import os
import sys
import zipfile
import re
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

    if not version or not isinstance(version, str):
        print("Error: 'runtime_version' is missing or not a string in MANIFEST.json")
        sys.exit(1)

    if not re.match(r"^V\d+\.\d+(?:\.\d+)?$", version):
        print(f"Error: 'runtime_version' ({version}) does not match required format (e.g., V1.4, V1.4.1)")
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

        if not resolved_p.is_relative_to(repo_root):
            print(f"Error: Path resolves outside repository root: {f} -> {resolved_p}")
            sys.exit(1)

    # Ensure dist folder exists
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    final_zip_filename = dist_dir / f"Zhongshu_Runtime_Deployment_Pack_{version}.zip"
    temp_zip_filename = dist_dir / f"Zhongshu_Runtime_Deployment_Pack_{version}.zip.tmp"

    print(f"Building {temp_zip_filename}...")

    try:
        with zipfile.ZipFile(temp_zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in package_files:
                zipf.write(file, arcname=file)
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        if temp_zip_filename.exists():
            temp_zip_filename.unlink()
        sys.exit(1)

    # Verify ZIP contents
    print("Verifying ZIP contents...")
    verify_error = None
    try:
        with zipfile.ZipFile(temp_zip_filename, 'r') as zipf:
            zip_files = set(zipf.namelist())
            expected_files = set(package_files)

            if zip_files != expected_files:
                verify_error = f"ZIP contents do not match deployment_files exactly.\nExpected: {expected_files}\nFound: {zip_files}"

            if not verify_error:
                for zf in zip_files:
                    zp = Path(zf)
                    if '..' in zp.parts or zp.is_absolute() or zf.startswith('/') or zf.startswith('\\'):
                        verify_error = f"Invalid path in ZIP: {zf}"
                        break
    except Exception as e:
        verify_error = f"Error reading ZIP file: {e}"

    if verify_error:
        print(f"Error verifying ZIP file: {verify_error}")
        if temp_zip_filename.exists():
            temp_zip_filename.unlink()
        sys.exit(1)

    # Atomic rename on success
    try:
        temp_zip_filename.replace(final_zip_filename)
    except Exception as e:
        print(f"Error replacing final ZIP file: {e}")
        if temp_zip_filename.exists():
            temp_zip_filename.unlink()
        sys.exit(1)

    print(f"Build SUCCESS: {final_zip_filename}")
    sys.exit(0)

if __name__ == "__main__":
    main()
