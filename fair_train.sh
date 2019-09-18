#!/usr/bin/env bash

# bash fair_train.sh [data_folder] [arch]



cd fairseq
mkdir -p checkpoints/$1_$2

# bash fair_train.sh movie fconv
# bash fair_train.sh movie fconv_wmt_en_de

# nohup fairseq-train \
#     data-bin/$1 --lr 0.5 --clip-norm 0.1 --dropout 0.2 --max-epoch 500 --max-tokens 4000 \
#     --criterion label_smoothed_cross_entropy --label-smoothing 0.1 --lr-scheduler fixed --force-anneal 200 --arch $2 \
#     --save-dir checkpoints/$1_$2 > $1_$2.out &


# bash fair_train.sh movie transformer
# bash fair_train.sh movie transformer_iwslt_de_en
nohup fairseq-train data-bin/$1 \
    --arch $2 --share-decoder-input-output-embed \
    --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
    --lr 5e-4 --lr-scheduler inverse_sqrt --warmup-updates 4000 \
    --dropout 0.3 --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --max-tokens 4096 --max-epoch 500 \
    --save-dir checkpoints/$1_$2 > $1_$2.out &
# fairseq-train data-bin/$1 \
#     --arch $2 --share-decoder-input-output-embed \
#     --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
#     --lr 5e-4 --lr-scheduler inverse_sqrt --warmup-updates 4000 \
#     --dropout 0.3 --weight-decay 0.0001 \
#     --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
#     --max-tokens 4096 --max-epoch 500 \
#     --save-dir checkpoints/$1_$2

cd ..

