#!/usr/bin/env bash

# bash nmt_train.sh data/movie 120000

cd nmt

#nohup python -m nmt.nmt --attention=scaled_luong --src=en --tgt=sparql \
#	--vocab_prefix=../$1/vocab --dev_prefix=../$1/dev --test_prefix=../$1/test \
#	--train_prefix=../$1/train --out_dir=../$1_att_model --num_train_steps=$2 \
#	--steps_per_stats=100 --num_layers=2 --num_units=128 --dropout=0.2 --metrics=bleu > movie_att_$2.out &

nohup python -m nmt.nmt --attention=scaled_luong  --attention_architecture=gnmt \
	--src=en --tgt=sparql \
	--vocab_prefix=../$1/vocab --dev_prefix=../$1/dev --test_prefix=../$1/test \
	--train_prefix=../$1/train --out_dir=../$1_gnmt_model --num_train_steps=$2 \
	--steps_per_stats=100 --num_layers=2 --num_units=128 --dropout=0.2 --metrics=bleu > movie_gnmt_$2.out &


#nohup python -m nmt.nmt --src=en --tgt=sparql \
#	--vocab_prefix=../$1/vocab --dev_prefix=../$1/dev --test_prefix=../$1/test \
#	--train_prefix=../$1/train --out_dir=../$1_model --num_train_steps=$2 \
#	--steps_per_stats=100 --num_layers=2 --num_units=128 --dropout=0.2 --metrics=bleu > movie_$2.out &


cd ..
