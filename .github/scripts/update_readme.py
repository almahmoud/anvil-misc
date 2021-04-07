from datetime import datetime
import json
import sys

from jinja2 import Template

args = sys.argv
inchunk = args[1]
allchunks = args[2]

with open(inchunk, 'r') as f:
    new_chunk = json.load(f)
    chunk_id = new_chunk.keys()[0]

with open(allchunks, 'r+') as f:
    chunks = json.load(f)
    old_chunk = chunks.get(chunk_id, {})
    new_chunk['run2'] = old_chunk.get('run1', 'N/A')
    new_chunk['date2'] = old_chunk.get('date1', 'N/A')
    chunks[chunk_id] = new_chunk
    f.seek(0)
    f.write(json.dumps(chunks, indent=4))
    f.truncate()

with open(".github/templates/README.md.j2", "r") as f:
    template = Template(f.read())

with open("README.md", "w") as f:
    htmlout = "<thead><tr><th>Chunk ID</th><th>Tool List</th><th>Latest report</th><th>Date of latest</th><th>Previous report</th><th>Date of previous</th></tr></thead><tbody>"
    for eachid, eachchunk in chunks:
        htmlout += "<tr><td>{}</td><td>[Toolset]({})</td><td>[Latest report]({})</td><td>{}</td><td>[Previous report]({})</td><td>{}</td></tr>".format(eachid, eachchunk.get("tools"), eachchunk.get("run1"), eachchunk.get("date1"), eachchunk.get("run2"), eachchunk.get("date2"))
    htmlout += "</tbody>"
    f.write(template.render(anviltools=htmlout))
