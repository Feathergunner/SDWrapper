#!usr/bin/python
# -*- coding: utf-8 -*-import string

import subprocess
import json
import numpy as np
import os
import re

from prompt_params import *

TXT2IMG_PATH = "OptimizedSD/optimized_txt2img.py"
PROMPTSDIR = "prompts/multiprompts"
OUTDIR = "outputs/multiprompt"

### ---------------------------------------------
### HELPER FUNCTIONS:
### ---------------------------------------------

def load_settings(settings):
	return settings["width"], settings["height"], settings["ddim_steps"], settings["n_samples"]

def get_seed():
	return np.random.randint(1000000)
	
def _get_prompt(content, style):
	'''
	Constructs the prompt-string from content and style
	'''
	if len(style) == 0:
		return "\""+content+"\""
	else:
		return "\""+content+", "+style+"\""
	
def _init(name, contentfile, contentkeys, stylefile, stylekeys):
	'''
	initialization script.
	Loads prompt-parts from files
	'''
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
	'''
	Constructs the full python command as string
	'''
	return "python "+TXT2IMG_PATH+" --turbo --W "+str(width)+" --H "+str(height)+" --ddim_steps "+str(ddim_steps)+" --n_samples "+str(n_samples)+" --seed "+str(seed)+" --prompt "+prompt+" --outdir "+outdir+" --format png"

### ---------------------------------------------
### EXPERIMENTS:
### ---------------------------------------------

def explore_imagesize(contentfile, contentkeys, stylefile, stylekeys, seed=None):
	'''
	An experiment that explores the effect of varying the image size
	'''
	contents, styles, outdir = _init("explore_imagesize", contentfile, contentkeys, stylefile, stylekeys)
	if seed is None:
		seed = get_seed()
	
	for contentkey in contents:
		for stylekey in styles:
			# construct prompt:
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

def explore_samplers(contentfile, contentkeys, stylefile, stylekeys, seed=None):
	'''
	An experiment that explores how the different samplers affect the generated images
	'''
	contents, styles, outdir = _init("explore_samplers", contentfile, contentkeys, stylefile, stylekeys)
	if seed is None:
		seed = get_seed()
	size = 512
	
	for contentkey in contents:
		for stylekey in styles:
			# construct prompt:
			full_prompt = _get_prompt(contents[contentkey], styles[stylekey])
			
			for sampler in ["ddim", "plms","heun", "euler", "euler_a", "dpm2", "dpm2_a", "lms"]:
				print ("Run experiment for sampler", sampler,"...")
				# get default command:
				full_command = _construct_full_command(full_prompt, size, size, 30, 5, seed, outdir)
				# add sampler argument:
				full_command += " --sampler "+sampler
				# run stable diffusion:
				subprocess.run(full_command)
				
				# move files into common output directory:
				orig_path_ = outdir+"/"+"_".join(re.split(":| ", full_prompt[1:-1]))
				orig_path = orig_path_[:150]
				for file in os.listdir(orig_path):
					fileparts = file.split('.')
					file_seed = fileparts[0].split('_')[1]
					os.replace(orig_path+"/"+file, outdir+"/"+contentkey+"_"+stylekey+"_"+file_seed+"_"+sampler+"."+fileparts[-1])
				os.rmdir(orig_path)

### ---------------------------------------------
### MAIN SCRIPT:
### ---------------------------------------------

def run_prompts(name, contentfile="contents_example", contentkeys=None, stylefile="styles_example", stylekeys=None, seed=None, settings=SETTINGS_DEFAULT, model="DEFAUL"):
	'''
	Main script that runs a batch of prompts, specified by contentfile, contentkeys, stylefile, stylekeys, seed, and settings
	Args:
		name (string):
			custom name for this batch of images, is used as folder name for output.
		contentfile (string):
			filename of json where the dictionary of content-prompts is defined.
		contentkeys (list of strings):
			the keys of the prompts that should be used. If None, all prompts from the contentfile are used.
		stylefile (string):
			filename of json where the dictionary of style-definitions is defined.
		stylekeys (list of strings):
			the keys of the styles that should be used. If None, all styles are used.
		seed (int):
			seed to be used. If None, random seed is generated.
		settings (dictionary):
			a dictionary that contains definitions for image size, number of sampling steps and number of generated images.
			By default, 5 images 512x512 with 50 steps are used.
			See also prompt_params.py, where some settings are defined.
		model (string):
			allows to use other models (requires modifying the code below).
	'''
	contents, styles, outdir = _init(name, contentfile, contentkeys, stylefile, stylekeys)
	width, height, ddim_steps, n_samples = load_settings(settings)
	if seed is None:
		seed = get_seed()
	
	for contentkey in contents:
		for stylekey in styles:
			print ("Run prompt content: "+contentkey+", style: "+stylekey)
			# construct prompt:
			full_prompt = _get_prompt(contents[contentkey], styles[stylekey])
			#print (full_prompt)
			full_command = _construct_full_command(full_prompt, width, height, ddim_steps, n_samples, seed, outdir)
			if model == "OTHER":
				# adds argument to use a different model:
				# requires a OTHER_MODEL
				
				# remove the following two lines if you want to use this
				print ("other model")
				return
				
				#full_command += " --ckpt "+OTHER_MODEL
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
	#explore_imagesize("contents_example", ["paris"], "styles", ["photo_lowquali"])
