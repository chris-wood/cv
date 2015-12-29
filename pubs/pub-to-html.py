import os
import sys

entries = {}
with open(sys.argv[1], "r") as fh:
    entryLines = []
    key = ""
    for line in fh:
        line = line.strip()
        if line.startswith("@"):
            key = line[line.index("{") + 1:line.index(",")]
            entryLines = []
            entryLines.append(line)
        elif line != "}":
            entryLines.append("   " + line)
        elif (line == "}"):
            entryLines.append(line)
            entries[key] = entryLines
            key = ""

for key in entries:
    print "                <div id=\"" + key + "\" class=\"panel panel-default\">"
    # print "                    <div class=\"panel-body\">"
    # print "                        TODO"
    # print "                    </div>"
    print "                    <div class=\"panel-body\"><pre>"
    print "                        \n".join(entries[key])
    print "                    </pre></div>"
    print "                </div>"
