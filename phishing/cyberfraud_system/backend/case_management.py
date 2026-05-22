import os

def create_case_folder(case_id, base_path="evidence/cases"):
    """
    Create a folder for a new case.

    Args:
        case_id (str): Unique identifier for the case.
        base_path (str): Base directory for storing cases.

    Returns:
        str: Path to the created case folder.
    """
    case_folder = os.path.join(base_path, case_id)
    os.makedirs(case_folder, exist_ok=True)
    return case_folder