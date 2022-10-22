# SDWrapper
A wrapper for stable diffusion.

### Requirements
Basujindals optimized stable diffusion ( https://github.com/basujindal/stable-diffusion ).

### Istallation
1. Download or clone this repository.
2. Move the content into the main directory of your stable diffusion installation (The sdwrapper.py has to be in the same directory that also contains the filder optimizedSD from basujindal).

### Run
1. Write your content-prompt(s) as a dictionary into a .json-file at prompts/multiprompts. See prompts/multiprompts/contents_example.json for examples.
2. Write your style specification(s) as a dictionary into another .json-file at prompts/multiprompts. See prompts/multiprompts/styles_all.json for examples.
2. Call sdwrapper.run_prompts(). See sdwrapper.py for examples.

# Styles
The file prompts/multiprompts/styles_all.json contains a list of different styles to choose from. Here are examples for all the styles, applied to the prompts
- castle
- elephant
- girl in a field of flowers

<p float="left">
  <img src="/exampleimgs/castle/castle_anime_cute_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_anime_cute_854248.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_anime_cute_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_anime_highquali_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_anime_highquali_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_anime_highquali_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_anime_simple_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_anime_simple_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_anime_simple_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_baroque_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_baroque_854248.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_baroque_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_cells1_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_cells1_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_cells1_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_cells2_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_cells2_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_cells2_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_comic_854246.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_comic_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_comic_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_concept_drawing_cl_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_concept_drawing_cl_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_concept_drawing_cl_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_concept_drawing_gr_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_concept_drawing_gr_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_concept_drawing_gr_854246.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_dark_fantasy_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_dark_fantasy_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_dark_fantasy_854246.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_digital_art_1_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_digital_art_1_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_digital_art_1_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_digital_art_2_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_digital_art_2_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_digital_art_2_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_digital_art_3854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_digital_art_3_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_digital_art_3_854244.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_distorted_lines_854248.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_distorted_lines_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_distorted_lines_854244.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_escher_854244.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_escher_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_escher_854244.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_fractal_854248.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_fractal_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_fractal_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_graffiti_854246.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_graffiti_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_graffiti_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_impressionism_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_impressionism_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_impressionism_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_insta_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_insta_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_insta_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_japanese1_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_japanese1_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_japanese1_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_japanese2_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_japanese2_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_japanese2_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_logo_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_logo_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_logo_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_low-poly_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_low-poly_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_low-poly_854246.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_manga_854246.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_manga_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_manga_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_neoexp_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_neoexp_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_neoexp_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_neon_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_neon_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_neon_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_paint_abstr_854248.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_paint_abstr_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_paint_abstr_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_paint_child_854248.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_paint_child_854248.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_paint_child_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_photo_lowquali_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_photo_lowquali_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_photo_lowquali_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_photo_quali_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_photo_quali_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_photo_quali_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_pixelart_854247.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_pixelart_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_pixelart_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_points_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_points_854246.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_points_854246.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_popart_854246.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_popart_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_popart_854244.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_renaissance_854246.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_renaissance_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_renaissance_854248.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_render3d_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_render3d_854244.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_render3d_854247.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_scififan_854247.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_scififan_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_scififan_854246.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_synthwave_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_synthwave_854248.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_synthwave_854244.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_triang_854245.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_triang_854247.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_triang_854245.png" width="100" />
</p>

<p float="left">
  <img src="/exampleimgs/castle/castle_vaprowave_854244.png" width="100" />
  <img src="/exampleimgs/elephant/elephant_vaprowave_854245.png" width="100" /> 
  <img src="/exampleimgs/girl/girl_vaprowave_854247.png" width="100" />
</p>
