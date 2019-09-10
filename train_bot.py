import subprocess, argparse

parser = argparse.ArgumentParser(description='give checkpoints')

parser.add_argument('checkpoint',type=str,nargs=1,help='give checkpoint file name')

args = parser.parse_args()
if args.checkpoint:
	subprocess.call(
		    ["th train.lua -gpuid -1 -init_from cv/{} -data_dir data/trumptweets -rnn_size 300 -num_layers 3 -eval_val_every 250 -dropout 0.5".format(args.checkpoint[0])],shell=True)
else:
	subprocess.call(
	    ["th train.lua -gpuid -1 -data_dir data/trumptweets -rnn_size 300 -num_layers 3 -eval_val_every 250 -dropout 0.5"],shell=True)
# checkpoints = []
# for dirname,dirnames,filenames in os.walk("cv"):
#     for filename in filenames:
#         checkpoints.append(filename)
# print("Available checkpoints: " + str(checkpoints))
# if len(checkpoints) > 0:
# 	checkpoints.sort()
# 	last_cv = checkpoints[-1]
# 	print("Using checkpoint: " + last_cv)

# 	print('training model')
# 	subprocess.call(
# 	    ["th train.lua -gpuid -1 -init_from cv/{} -data_dir data/trumptweets -rnn_size 300 -num_layers 3 -eval_val_every 250 -dropout 0.5".format(last_cv)],shell=True)
# else:
# 	subprocess.call(
# 	    ["th train.lua -gpuid -1 -data_dir data/trumptweets -rnn_size 300 -num_layers 3 -eval_val_every 250 -dropout 0.5"],shell=True)
