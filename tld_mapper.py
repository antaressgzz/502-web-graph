#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import re

def extract_hld(link):
    link_re = re.compile("^http[s]*://(www\.)*(\w+\.\w+[^/?]*)")
    m = link_re.search(link)
    if m:
        return True, m.group(2)
    else:
        return False, ''
    
    

    
for line in sys.stdin:
    if line.startswith('{'):
        meta_data = json.loads(line)
        try:
            links = meta_data['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']['HTML-Metadata']['Links']
            valid, source_hld = extract_hld(meta_data['Envelope']['WARC-Header-Metadata']['WARC-Target-URI'])         
        except KeyError:
            continue

        if not valid:
            continue

        source_hld_ = source_hld.split('.')
        hlds = []
        for l in links:
            url = l['url'] if l.get('url') else l.get('href')
            if url:
                valid, hld = extract_hld(url)

            # check if edge is valid and doesn't lead to source     
            if valid:
                hld_ = hld.split('.')
                if (len(hld_) + len(source_hld_)) == len(list(set(hld_+source_hld_))):
                    hlds.append(hld)

        for target_hld in hlds:
            sys.stdout.write("{}\t{}\n".format(source_hld, target_hld))