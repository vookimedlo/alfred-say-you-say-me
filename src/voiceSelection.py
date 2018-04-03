#!/usr/bin/python
# Author: Michal Duda
# License: GPLv3
# WWW: https://github.com/vookimedlo/alfred-say-you-say-me
#

import json
import os
import re
import sys
from subprocess import Popen, PIPE

buggyVoicesFilter = os.environ['buggy_voices_filter']
buggyVoicesFilterRE = re.compile(buggyVoicesFilter, re.I)

langFilter = os.environ['language_filter']
langFilterRE = re.compile(langFilter, re.I)

query = sys.argv[1]

try:
    process = Popen(["say", "-v", "?"], stdout=PIPE)
    (output, err) = process.communicate()
    exitCode = process.wait()
    
    if exitCode == 0:
        alfreditems = {"items": []}
        voicesPattern = re.compile("^([^ \t]+)[ \t]+([^ \t]+).+# (.+)")
        output = output.split('\n')
        
        for line in output:
            results = voicesPattern.search(line)
            if results:
                # Filter out languages
                #
                if not langFilterRE.search(results.group(2)):
                    continue

                # Filter out buggy voices
                #
                if buggyVoicesFilter != "" and buggyVoicesFilterRE.search(results.group(1)):
                    continue

                # Alfred menu items
                #
                alfreditems['items'].append({
                                            "mysortkey": results.group(2) + results.group(1),
                                            "uid": results.group(2) + results.group(1),
                                            "title": results.group(2) + ' - ' + results.group(1),
                                            "subtitle": results.group(3),
                                            "autocomplete": results.group(1),
                                            "arg": results.group(1),
                                            "variables": {
                                            "textToSay": query
                                            },
                                            })
    # Sort voices
    #
    lines = sorted(alfreditems['items'], key=lambda k: k['mysortkey'], reverse=False)
    dump = json.dumps({'items': lines}, indent=4)
    sys.stdout.write(dump)
except:
    pass

