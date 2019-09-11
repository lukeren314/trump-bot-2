import subprocess

subprocess.call(
	["th sample.lua cv/lm_lstm_epoch4.85_1.4760.t7 -gpuid -1 "],shell=True)
