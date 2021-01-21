#!/usr/bin/env python
"""

Neural SPARQL Machines - Split into train, dev, and test sets.

'SPARQL as a Foreign Language' by Tommaso Soru and Edgard Marx et al., SEMANTiCS 2017
https://w3id.org/neural-sparql-machines/soru-marx-semantics2017.html
https://arxiv.org/abs/1708.07624

Version 0.0.4

"""
import argparse
import random
import os

TRAINING_PERCENTAGE = 80
TEST_PERCENTAGE = 10
DEV_PERCENTAGE = 10

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('--lines', dest='lines', metavar='lines', help='total number of lines (wc -l <file>)', required=True)
    requiredNamed.add_argument('--dataset', dest='dataset', metavar='dataset.sparql', help='sparql dataset file', required=True)
    args = parser.parse_args()

    lines = int(args.lines)
    dataset_file = os.path.splitext(args.dataset)[0]
    print dataset_file
    sparql_file = dataset_file + '/data.sparql'
    ko_file = dataset_file + '/data.ko'

    random.seed()

    test_and_dev_percentage = sum([TEST_PERCENTAGE, DEV_PERCENTAGE])
    number_of_test_and_dev_examples = int(lines * test_and_dev_percentage / 100)
    number_of_dev_examples = int(number_of_test_and_dev_examples * DEV_PERCENTAGE / test_and_dev_percentage)

    dev_and_test = random.sample(xrange(lines), number_of_test_and_dev_examples)
    dev = random.sample(dev_and_test, number_of_dev_examples)

    with open(sparql_file) as original_sparql, open(ko_file) as original_ko:
        sparql = original_sparql.readlines()
        korean = original_ko.readlines()

        dev_sparql_lines = []
        dev_ko_lines = []
        train_sparql_lines = []
        train_ko_lines = []
        test_sparql_lines = []
        test_ko_lines = []

        for i in range(len(sparql)):
            sparql_line = sparql[i]
            ko_line = koglish[i]
            if i in dev_and_test:
                if i in dev:
                    dev_sparql_lines.append(sparql_line)
                    dev_ko_lines.append(ko_line)
                else:
                    test_sparql_lines.append(sparql_line)
                    test_ko_lines.append(ko_line)
            else:
                train_sparql_lines.append(sparql_line)
                train_ko_lines.append(ko_line)

        with open(dataset_file + '/train.sparql', 'w') as train_sparql, open(dataset_file + '/train.ko', 'w') as train_ko, \
                open(dataset_file + '/valid.sparql', 'w') as dev_sparql, open(dataset_file + '/valid.ko', 'w') as dev_ko, \
                open(dataset_file + '/test.sparql', 'w') as test_sparql, open(dataset_file + '/test.ko', 'w') as test_ko:

            train_sparql.writelines(train_sparql_lines)
            train_ko.writelines(train_ko_lines)
            dev_sparql.writelines(dev_sparql_lines)
            dev_Ko.writelines(dev_ko_lines)
            test_sparql.writelines(test_sparql_lines)
            test_ko.writelines(test_ko_lines)
