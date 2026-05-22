"""
APK Analysis Module
"""
import hashlib
from androguard.core.bytecodes.apk import APK


def hash_apk(apk_path):
    """
    Calculate the SHA256 hash of an APK file.

    Args:
        apk_path (str): Path to the APK file.

    Returns:
        str: SHA256 hash of the APK file.
    """
    # Validate APK file path
    if not isinstance(apk_path, str) or not apk_path.endswith('.apk'):
        raise ValueError("Invalid APK file. Please provide a valid .apk file path.")

    sha256_hash = hashlib.sha256()
    with open(apk_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def extract_apk_metadata(apk_path):
    """
    Extract metadata from an APK file.

    Args:
        apk_path (str): Path to the APK file.

    Returns:
        dict: Metadata extracted from the APK file.
    """
    try:
        apk = APK(apk_path)
        metadata = {
            "package_name": apk.get_package(),
            "version_name": apk.get_androidversion_name(),
            "version_code": apk.get_androidversion_code(),
            "permissions": apk.get_permissions(),
            "activities": apk.get_activities(),
            "services": apk.get_services(),
            "providers": apk.get_providers(),
            "receivers": apk.get_receivers(),
            "main_activity": apk.get_main_activity(),
            "sha256": hash_apk(apk_path)
        }
        print(f"[APK_ANALYSIS] Metadata extracted for {apk_path}")
        return metadata
    except Exception as e:
        print(f"[APK_ANALYSIS] Error analyzing APK: {e}")
        return {"error": str(e)}