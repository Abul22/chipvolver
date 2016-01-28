#!/usr/bin/env python

import sys
import os
import json
import random

def combine_and_mutate(k, definitions, mutation_rate):
    gene = random.choice(definitions)[k]
    if type(gene) == float and mutation_rate:
        return max(0, min(1.0, gene + (random.random() * mutation_rate)))
    else:
        return gene

def load_definition(filename):
    return json.loads(file(filename).read())

def load_definitions(filenames):
    return [load_definition(f) for f in filenames]

def reproduce(definitions, seed=str(random.random()), mutation_rate=0.0):
    random.seed(seed)
    return dict([(k, combine_and_mutate(k, definitions, mutation_rate)) for k in definitions[0].keys()])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # extract the sfxr json files from the passed in arguments
        sfxr_files = [f for f in sys.argv[1:] if f.endswith(".sfxr.json") and os.path.isfile(f)]
        definitions = load_definitions(sfxr_files)
        mutation_rate = 0.0
        seed = None
        # parse the rest of the arguments
        for arg in sys.argv[1:]:
            if arg.startswith("--seed="):
                seed = arg[len("--seed="):]
            elif not arg in sfxr_files:
                mutation_rate = float(arg)
        if not seed:
            seed = str(random.random())
            sys.stderr.write("Seed: " + seed + "\n")
        new_sound = reproduce(definitions, seed, mutation_rate)
        print json.dumps(new_sound, indent=2)
    else:
        print "Usage:", sys.argv[0], "SOUND-DEFINITION.sfxr.json SOUND-DEFINITION-1.sfxr.json ...", "[--seed=SEED]", "[MUTATION-RATE]"
        print "Creates a new sound definition by randomly combining the input sound definitions."

