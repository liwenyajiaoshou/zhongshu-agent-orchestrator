import json
import os
import sys
import zipfile
from pathlib import Path

def main():
    print("Starting Runtime Pack Build...")
    
    # Check if Manifest exists
    manifest_path = Path("MANIFEST.json")
    if not manifest_path.exists():
        print("Error: MANIFEST.json not found.")
        sys.exit(1)
        
    try:
        content = manifest_path.read_text(encoding='utf-8')
        data = json.loads(content)
        version = data.get("runtime_version")
        files_to_pack = data.get("deployment_files")
    except Exception as e:
        print(f"Error parsing MANIFEST.json: {e}")
        sys.exit(1)
        
    if not version:
        print("Error: 'runtime_version' is missing or empty in MANIFEST.json")
        sys.exit(1)
        
    if not files_to_pack or not isinstance(files_to_pack, list):
        print("Error: 'deployment_files' is missing or invalid in MANIFEST.json")
        sys.exit(1)
        
    # Verify all files exist before building
    missing_files = [f for f in files_to_pack if not Path(f).is_file()]
    if missing_files:
        print("Error: The following required deployment files are missing:")
        for f in missing_files:
            print(f"  - {f}")
        sys.exit(1)
        
    # Ensure dist folder exists
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)
    
    zip_filename = dist_dir / f"Zhongshu_Runtime_Deployment_Pack_{version}.zip"
    
    print(f"Building {zip_filename}...")
    
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # We explicitly ONLY pack files declared in deployment_files + MANIFEST.json
            files_to_pack.append("MANIFEST.json")
            for file in set(files_to_pack):
                # Using file as arcname to preserve relative paths
                zipf.write(file, arcname=file)
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        sys.exit(1)
        
    # Verify ZIP contents
    print("Verifying ZIP contents...")
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zip_files = set(zipf.namelist())
            expected_files = set(files_to_pack)
            
            if zip_files != expected_files:
                print("Error: ZIP contents do not match deployment_files exactly.")
                print(f"Expected: {expected_files}")
                print(f"Found: {zip_files}")
                sys.exit(1)
                
            for zf in zip_files:
                if '..' in zf or zf.startswith('/') or zf.startswith('\\'):
                    print(f"Error: Invalid path in ZIP: {zf}")
                    sys.exit(1)
                    
    except Exception as e:
        print(f"Error verifying ZIP file: {e}")
        sys.exit(1)

    print(f"Build SUCCESS: {zip_filename}")
    sys.exit(0)

if __name__ == "__main__":
    main()
