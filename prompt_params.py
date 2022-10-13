# really only useful for debug
SETTINGS_DEBUG = {
	"width" : 256,
	"height" : 256,
	"ddim_steps" : 10,
	"n_samples" : 1
}

SETTINGS_EXPLORE = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 30,
	"n_samples" : 5
}

# less steps, more samples
SETTINGS_EXPLORE_2 = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 20,
	"n_samples" : 10
}

SETTINGS_DEFAULT = {
	"width" : 512,
	"height" : 512,
	"ddim_steps" : 50,
	"n_samples" : 5
}

SETTINGS_PORTRAIT = {
	"width" : 512,
	"height" : 768,
	"ddim_steps" : 50,
	"n_samples" : 5
}

# almost 9x16 (phone screen format)
SETTINGS_PORTRAIT_HIGH = {
	"width" : 512,
	"height" : 960,
	"ddim_steps" : 50,
	"n_samples" : 5
}

SETTINGS_LANDSCAPE = {
	"width" : 768,
	"height" : 512,
	"ddim_steps" : 50,
	"n_samples" : 5
}

# smaller version
SETTINGS_LANDSCAPE2 = {
	"width" : 512,
	"height" : 384,
	"ddim_steps" : 50,
	"n_samples" : 5
}

# almost 16x9
SETTINGS_LANDSCAPE_BIG = {
	"width" : 960,
	"height" : 512,
	"ddim_steps" : 50,
	"n_samples" : 5
}