import pandas as pd
import os


def export_excel(job_id: str, data: list):
    os.makedirs("jobs/exports", exist_ok=True)

    file_path = f"jobs/exports/{job_id}.xlsx"

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

    return file_path