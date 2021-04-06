import yaml
import sys
import datetime

args = sys.argv
infile = args[1]
outfile = args[2]
today = datetime.datetime.today()
weekday = today.weekday()
time_of_day = 0 if today.strftime("%p") == 'AM' else 1
runs_per_day = 2 # run twice a day
total_chunks = 7 * runs_per_day


with open(infile, 'r') as f:
    out = yaml.safe_load(f.read())

l = out.get('tools', [])
num_per_run = int(len(l)/total_chunks)
current_num = weekday * runs_per_day + time_of_day

# option to override which section to run
if len(args) > 3:
    try:
        new_num = int(args[3])
        if new_num in range(0, total_chunks):
            current_num = new_num
        elif not new_num == 999:
            print(f"Given input {new_num} is out of the valid range [0:{total_chunks-1}]")
    except ValueError:
        print(f"Given input {args[3]} is invalid")
        pass

start = current_num * num_per_run
end = current_num * num_per_run
end = len(l) if end > len(l) else end
out['tools'] = l[start:end]


with open(outfile, 'w') as f:
    f.write(yaml.safe_dump(out))

