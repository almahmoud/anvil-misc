import yaml
import sys
import datetime

args = sys.argv
outfile = args[1]
weekday = datetime.datetime.today().weekday()

with open("reports/anvil/tools.yaml", 'r') as f:
    out = yaml.safe_load(f.read())

l = out.get('tools', [])
num = int(len(l)/7)
start = weekday*num
end = num + weekday * num if weekday < 6 else len(l)
out['tools'] = l[start:end]


with open(outfile, 'w') as f:
    f.write(yaml.safe_dump(out))

