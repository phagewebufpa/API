#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import sys
import time

def help_message():
    msg = "PHAGEWEB: \n \
    run: python3 api.py --file inpu_file.gbk --id 80 --integrity 80 --cds 6 --email 'example@mail.com'"
    print(msg)

def get_code():
    url = "http://computationalbiology.ufpa.br/phageweb/analyse.php"
    request = requests.get(url)
    if request.status_code == 200:
        page = request.text
        code = page[page.find("analysis/20") + len("analysis/"):page.find("/blast.php")]
        return code
    else:
        return False

def submit_data(code, file_gbk, email = None, identity = '80', cds = '6', integrity = '80'):
    url = "http://computationalbiology.ufpa.br/phageweb/analysis/" + code + "/blast.php"
    file = {'arquivo': open(file_gbk, 'rb')}
    payload = {
        'email'         : email,
        'email_select'  : '1',
        'identity'      : identity,
        'cds'           : cds,
        'integrity'     : integrity,
        'protocolo'     : code
    }
    #print(payload)
    r = requests.post(url, files=file, data=payload)
    
    return r
    
def get_args(args):
    xargs = {'--email' : 'denermaues@gmail.com',
            '--file' : None, 
            '--id' : '80', 
            '--integrity' : '80', 
            '--cds' : '6'
        
    }
    for arg in args:
        if arg in xargs:
            xargs[arg] = args[args.index(arg) + 1]
    
    return xargs

def get_status(code):
    url = "http://computationalbiology.ufpa.br/phageweb/result_status.php?protocolo=" + code
    request = requests.get(url)
    if request.status_code == 200:
        page = request.text
        
        return page.strip()
    else:
        return False

def get_files(code):
    url = "http://computationalbiology.ufpa.br/phageweb/analysis/" + code + "/"
    files = ['output_genbank.gbk', 'output_tabular.tab', 'output_characterization.txt']
    for file in files:
        request = requests.get(url + file)
        if request.status_code == 200:
            page = request.text
            with open(file, 'w') as out:
                out.write(page)
                
    
    
if len(sys.argv) > 1:
    code = get_code()
    #print(code)
    args = get_args(sys.argv)
    r = submit_data(code, args['--file'], args['--email'], args['--id'], args['--cds'])
    
    while(get_status(code) != '6'):
        time.sleep(1)
        #print(get_status(code))
    
    get_files(code)
    print("Your review has been successfully processed! Your results can be downloaded in the indicated directory or access the results online at: http://computationalbiology.ufpa.br/phageweb/analysis/" + code)
    
else:
    help_message()
