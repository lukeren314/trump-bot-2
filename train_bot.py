import subprocess

print('training model')
subprocess.call(
    ["th train.lua -gpuid -1 -data_dir data/trumptweets -rnn_size 300 -num_layers 3 -dropout 0.5"])
