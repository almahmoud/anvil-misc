import json
import sys

args = sys.argv
project = args[1]
report = args[2]

with open("reports/{}/deployments.json".format(project), "r+") as f:
    out = json.load(f)
    deps = out.get("results", {}).get("deployments", [])
    current = json.loads(report)
    deps.insert(0, current)
    out["results"]["deployments"] = deps
    f.seek(0)
    f.write(json.dumps(out, indent=4))
    f.truncate()
     

