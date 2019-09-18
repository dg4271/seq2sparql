#!/usr/bin/env bash

# bash fair_preprocess.sh movie

cd fairseq
fairseq-preprocess --source-lang en --target-lang sparql \
    --trainpref ../data/$1/train --validpref ../data/$1/valid --testpref ../data/$1/test \
    --destdir data-bin/$1 \
    --workers 20
cd ..
