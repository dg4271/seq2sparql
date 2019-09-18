#!/usr/bin/env bash

# bash make_train_set_from_template.sh data/annotations_monument.csv data/monument_300

#python2 generator.py --templates data/annotations_monument.csv  --output data/monument_300
python2 generator.py --templates $1  --output $2

python build_vocab.py $2/data.en > $2/vocab.en
python build_vocab.py $2/data.sparql > $2/vocab.sparql

NUMLINES=$(echo awk '{ print $1}' | cat $2/data.sparql |  wc -l)

python2 split_in_train_dev_test.py --lines $NUMLINES  --dataset $2