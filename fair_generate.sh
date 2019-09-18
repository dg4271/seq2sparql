#!/usr/bin/env bash

# bash fair_generate.sh [data_folder] [arch]
# bash fair_generate.sh movie fconv_wmt_en_de

cd fairseq
fairseq-generate data-bin/$1 --path checkpoints/$1_$2/checkpoint_best.pt --batch-size 128 --beam 5 --remove-bpe | tee ./results/$1_$2.out

# system output
grep ^H ./results/$1_$2.out | cut -f3- > ./results/$1_$2.out.sys
# Target of test data
grep ^T ./results/$1_$2.out | cut -f2- > ./results/$1_$2.out.ref
cd ..

python2 interpreter.py ./fairseq/results/$1_$2.out.sys ./fairseq/results/$1_$2.out.sys.decoded
