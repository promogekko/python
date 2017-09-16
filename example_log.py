import sys

log_file= "jenkins.log"
warn = "warning.txt"

with open(log_file) as infile:
    with open(warn, "w") as outfile:
        warnings = (line for line in infile if 'WARNING' in line)
        for l in warnings:
            outfile.write(l)