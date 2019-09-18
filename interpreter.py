#!/usr/bin/env python
"""

Neural SPARQL Machines - Interpreter module

'SPARQL as a Foreign Language' by Tommaso Soru and Edgard Marx et al., SEMANTiCS 2017
https://w3id.org/neural-sparql-machines/soru-marx-semantics2017.html
https://arxiv.org/abs/1708.07624

Version 0.1.0-akaha

"""
import sys
import re

from generator_utils import decode, fix_URI, query_dbpedia

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # python2 interpreter.py ./fairseq/results/$1_$2.out.sys ./fairseq/results/$1_$2.out.ref 
    with open(sys.argv[1], 'r') as f_sys, open(sys.argv[2], 'r') as f_ref, \
        open(sys.argv[1]+'.decoded2', 'w') as f_decoded, open(sys.argv[1]+".decoded.final2", 'w') as f_out:
        
        count_false = 0

        for encoded_sparql_sys, encoded_sparql_ref in zip(f_sys, f_ref):
            decoded_sparql = decode(encoded_sparql_sys)
            f_decoded.write(decoded_sparql)
            decoded_sparql = fix_URI(decoded_sparql)
            return_json = query_dbpedia(decoded_sparql)
            is_sparql_right = "True"
            
            if '<unk>' in encoded_sparql_ref or ("results" in return_json.keys() and len(return_json["results"]["bindings"]) == 0):
                #print(encoded_sparql_sys)
                #print(encoded_sparql_ref)
                #print("false"+ str(count_false))
                is_sparql_right = "False"
                count_false = count_false + 1

            if count_false%100 == 0:
                print(count_false)

            f_out.write(is_sparql_right + ", " + decoded_sparql)


    


