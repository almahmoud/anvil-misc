import yaml
import sys
import datetime

args = sys.argv
outfile = args[1]
today = datetime.datetime.today()
weekday = today.weekday()
time_of_day = 0 if today.strftime("%p") == 'AM' else 1
runs_per_day = 2 # run twice a day
total_days = 7 * runs_per_day


with open("reports/anvil/tools.yaml", 'r') as f:
    out = yaml.safe_load(f.read())

l = out.get('tools', [])
num_per_run = int(len(l)/total_days)
start = (weekday * runs_per_day + time_of_day) * num_per_run
end = (weekday * runs_per_day + time_of_day + 1) * num_per_run
end = len(l) if end > len(l)
out['tools'] = l[start:end]


with open(outfile, 'w') as f:
    f.write(yaml.safe_dump(out))

