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
     
with open("reports/{}/deployments.html".format(project), "r+") as f:
    htmlout = "<table><thead><tr><th>Date</th><th>Status</th><th>GKM time</th></tr></thead><tbody>"
    for each in deps:
        htmlout += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(each.get("date"), each.get("status"), each.get("time"))
    htmlout += "</tbody></table>"
    f.write(htmlout)

