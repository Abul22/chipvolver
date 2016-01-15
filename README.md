The chip sound definitions from http://sfxr.me/ can be combined and mutated in a way that is similar to genetic evolution to make new randomly generated sounds from combinations of other sounds.

`./chipvolver.py test-sounds/coin-*.sfxr.json | ../jsfxr/sfxr-to-wav && play sfxr-sound.wav`

Get the `sfxr-to-wav` script from [jsfxr](https://github.com/chr15m/jsfxr/)

Set a mutation rate between 0 and 1:

`./chipvolver.py test-sounds/coin-*.sfxr.json 0.01`

Set some seed to get a deterministic result:

`./chipvolver.py test-sounds/coin-*.sfxr.json 0.01 seed=23`
