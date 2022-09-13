#!usr/bin/python
# -*- coding: utf-8 -*-import string

import subprocess
import json
import numpy as np
import os
import re

TXT2IMG_PATH = "OptimizedSD/optimized_txt2img.py"
PROMPTSDIR = "prompts/multiprompts"
OUTDIR = "outputs/multiprompt"

SETTINGS_DEBUG = {
	"width" : 256,
	"height" : 256,
	"ddim_steps" : 20,
	"n_samples" : 1
}

SETTINGS_TEST = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 30,
	"n_samples" : 5
}

SETTINGS_DEFAULT_PORTRAIT = {
	"width" : 512,
	"height" : 768,
	"ddim_steps" : 50,
	"n_samples" : 5
}

SETTINGS_DEFAULT_LANDSCAPE = {
	"width" : 768,
	"height" : 512,
	"ddim_steps" : 50,
	"n_samples" : 5
}

def load_settings(settings):
	return settings["width"], settings["height"], settings["ddim_steps"], settings["n_samples"]

def get_seed():
	return np.random.randint(1000000)
	
def run_prompts(name, promptfile="prompts_example", stylefile="styles_example", settings=SETTINGS_DEFAULT_PORTRAIT):
	print (PROMPTSDIR)
	print (promptfile)
	with open(PROMPTSDIR+"/"+promptfile+".json", 'r') as promptsfile:
		prompts = json.load(promptsfile)
	with open(PROMPTSDIR+"/"+stylefile+".json", 'r') as stylefile:
		styles = json.load(stylefile)
	
	outdir = OUTDIR+"/"+name
	width, height, ddim_steps, n_samples = load_settings(settings)		
	seed = get_seed()
	
	for promptkey in prompts:
		prompt = prompts[promptkey]
		#print (prompt)
		for stylekey in styles:
			#print (stylekey)
			# construct command:
			full_prompt = "\""+prompt+", "+styles[stylekey]+"\""
			#print (full_prompt)
			full_command = "python "+TXT2IMG_PATH+" --turbo --W "+str(width)+" --H "+str(height)+" --ddim_steps "+str(ddim_steps)+" --n_samples "+str(n_samples)+" --seed "+str(seed)+" --prompt "+full_prompt+" --outdir "+outdir
			#print (full_command)
			# run stable diffusion:
			subprocess.run(full_command)
			
			# move files into common output directory:
			orig_path_ = outdir+"/"+"_".join(re.split(":| ", full_prompt[1:-1]))
			orig_path = orig_path_[:150]
			for file in os.listdir(orig_path):
				fileparts = file.split('.')
				newfilename = fileparts[0].split('_')[1]+"."+fileparts[-1]
				os.replace(orig_path+"/"+file, outdir+"/"+promptkey+"_"+stylekey+"_"+newfilename)
			os.rmdir(orig_path)


if __name__ == "__main__":
	print ("requires \"conda activate ldm\"!")
	run_prompts("test", settings=SETTINGS_TEST)
	
