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
	"n_samples" : 3
}

SETTINGS_EXPLORE = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 50,
	"n_samples" : 5
}

SETTINGS_HQ = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 80,
	"n_samples" : 1
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
	
def _get_prompt(content, style):
	return "\""+content+", "+style+"\""
	
def _init(name, contentfile, contentkeys, stylefile, stylekeys):
	print ("get prompts from "+PROMPTSDIR)
	print ("\t.../"+contentfile+".json")
	print ("\t.../"+stylefile+".json")
	with open(PROMPTSDIR+"/"+contentfile+".json", 'r') as contentfile:
		contents = json.load(contentfile)
		if contentkeys is not None:
			contents = {key: contents[key] for key in contentkeys}
	with open(PROMPTSDIR+"/"+stylefile+".json", 'r') as stylefile:
		styles = json.load(stylefile)
		if stylekeys is not None:
			styles = {key: styles[key] for key in stylekeys}
	outdir = OUTDIR+"/"+name
	return contents, styles, outdir
	
def _construct_full_command(prompt, width, height, ddim_steps, n_samples, seed, outdir):
	return "python "+TXT2IMG_PATH+" --turbo --W "+str(width)+" --H "+str(height)+" --ddim_steps "+str(ddim_steps)+" --n_samples "+str(n_samples)+" --seed "+str(seed)+" --prompt "+prompt+" --outdir "+outdir

def explore_imagesize(contentfile, contentkeys, stylefile, stylekeys, seed=None):
	contents, styles, outdir = _init("explore_imagesize", contentfile, contentkeys, stylefile, stylekeys)
	if seed is None:
		seed = get_seed()
	
	for contentkey in contents:
		for stylekey in styles:
			# construct command:
			full_prompt = _get_prompt(contents[contentkey], styles[stylekey])
			
			for size in [128, 256, 384, 512, 768, 1024]:
				full_command = _construct_full_command(full_prompt, size, size, 50, 5, seed, outdir)
				#print (full_command)
				# run stable diffusion:
				subprocess.run(full_command)
				
				# move files into common output directory:
				orig_path_ = outdir+"/"+"_".join(re.split(":| ", full_prompt[1:-1]))
				orig_path = orig_path_[:150]
				for file in os.listdir(orig_path):
					fileparts = file.split('.')
					file_seed = fileparts[0].split('_')[1]
					os.replace(orig_path+"/"+file, outdir+"/"+contentkey+"_"+stylekey+"_"+file_seed+"_"+str(size)+"."+fileparts[-1])
				os.rmdir(orig_path)


def run_prompts(name, contentfile="contents_example", contentkeys=None, stylefile="styles_example", stylekeys=None, seed=None, settings=SETTINGS_DEFAULT_PORTRAIT):
	contents, styles, outdir = _init(name, contentfile, contentkeys, stylefile, stylekeys)
	width, height, ddim_steps, n_samples = load_settings(settings)
	if seed is None:
		seed = get_seed()
	
	for contentkey in contents:
		for stylekey in styles:
			# construct command:
			full_prompt = _get_prompt(contents[contentkey], styles[stylekey])
			#print (full_prompt)
			full_command = _construct_full_command(full_prompt, width, height, ddim_steps, n_samples, seed, outdir)
			#print (full_command)
			# run stable diffusion:
			subprocess.run(full_command)
			
			# move files into common output directory:
			orig_path_ = outdir+"/"+"_".join(re.split(":| ", full_prompt[1:-1]))
			orig_path = orig_path_[:150]
			for file in os.listdir(orig_path):
				fileparts = file.split('.')
				file_seed = fileparts[0].split('_')[1]
				os.replace(orig_path+"/"+file, outdir+"/"+contentkey+"_"+stylekey+"_"+file_seed+"."+fileparts[-1])
			os.rmdir(orig_path)


if __name__ == "__main__":
	print ("requires \"conda activate ldm\"!")
	
	# run set of prompts:
	run_prompts("debug", settings=SETTINGS_DEBUG)
	
	# explore impact of image size:
	#explore_imagesize("contents_example", ["paris"], "styles_example", ["photo_lowquali"])
