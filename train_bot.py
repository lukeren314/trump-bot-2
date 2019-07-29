import subprocess

print('training model')
subprocess.call(["th train.lua -gpuid -1 -data_dir data/trumptweets -rnn_size 200 -num_layers 2 -dropout 0.5"])
