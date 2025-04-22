import json
from datetime import datetime

def save_application(job):
    job['applied_at'] = datetime.now().isoformat()
    try:
        with open("applied_jobs.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(job)
    with open("applied_jobs.json", "w") as f:
        json.dump(data, f, indent=2)
