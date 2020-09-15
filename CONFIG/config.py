import yaml,sys

with open(sys.argv[1]) as f:
    conf=yaml.safe_load(f.read())

#print(conf)
