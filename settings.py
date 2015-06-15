__author__ = 'gideon'

import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


ACTIONS_DIR = os.path.join(BASE_DIR, 'actions')
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')


installed_actions = {
    'reverse': 'Reverser',
    'shuffle': 'Shuffler',
    'sort': 'Sorter'
}