#!/usr/bin/env python

import sys
import os
import json
import random

mutation_rate = 0.0
definitions = []

def combine_and_mutate(definitions, mutation_rate):
    gene = random.choice(definitions)[k]
    if type(gene) == float and mutation_rate:
        return max(0, min(1.0, gene + (random.random() * mutation_rate)))
    else:
        return gene

if len(sys.argv) > 1:
    keys = []
    for arg in sys.argv[1:]:
        if os.path.isfile(arg) and arg.endswith(".sfxr.json"):
            definition = json.loads(file(arg).read())
            keys = definition.keys()
            definitions.append(definition)
        elif arg.startswith("seed="):
            random.seed(arg)
        else:
            mutation_rate = float(arg)
    new_sound = dict([(k, combine_and_mutate(definitions, mutation_rate)) for k in keys])
    print json.dumps(new_sound, indent=2)
else:
    print "Usage:", sys.argv[0], "SOUND-DEFINITION.sfxr.json SOUND-DEFINITION-1.sfxr.json ...", "[MUTATION-RATE]"
    print "Creates a new sound definition by randomly combining the input sound definitions."

