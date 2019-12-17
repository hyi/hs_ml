import csv
import sys

from hs_restclient import HydroShare


hs = HydroShare(prompt_auth=False)


def write_resource_to_csv(output_file, res_status):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if res_status == 'published':
            header_list = ['UUID', 'Title', 'Keywords', 'Abstract']
            res_list = hs.resources(published=True)
        elif res_status == 'public':
            header_list = ['UUID', 'Title', 'Keywords', 'Abstract']
            res_list = hs.resources(published=False)
        else:
            header_list = ['UUID', 'Status', 'Title', 'Keywords', 'Abstract']
            res_list = hs.resources()

        writer.writerow(header_list)
        cnt = 0
        for res in res_list:
            rid = res['resource_id']
            r_title = res['resource_title']
            md_json = hs.getScienceMetadata(rid)
            r_keyword_list = md_json['subjects']
            r_keywords = ';'.join([item['value'] for item in r_keyword_list])
            r_abstract = md_json['description']
            r_abstract = r_abstract.replace('\r\n', ' ')
            if not res_status:
                r_status = 'published' if res['published'] else 'public'
                writer.writerow([rid, r_status, r_title, r_keywords, r_abstract])
            else:
                writer.writerow([rid, r_title, r_keywords, r_abstract])
            cnt += 1
        print('Dumped all specified resources to', output_file, '. The number of dumped resources: ', cnt)


# check whether the optional parameter is passed in
if len(sys.argv) > 1:
    status = sys.argv[1].strip()
    if status != 'published' and status != 'public':
        status = ''
else:
    status = ''

if status == 'published':
    # only write published data
    output_file = 'data/hs_data_published.csv'
elif status == 'public':
    # only write public data
    output_file = 'data/hs_data_public.csv'
else:
    # write all data
    output_file = 'data/hs_data.csv'

write_resource_to_csv(output_file, status)
