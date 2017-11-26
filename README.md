#15-112 project


Python2
lib: 
Pygame
Tkinter
image
media
random, math,sys


Introduction: My project is mainly based on an ancient Chinese Painting “A Panorama of Rivers and Mountains”, which is the archetypal work of the blue–green shanshui style, and in which the painting stands as the most representable and historically marked piece, with both historical and political meaning in Song Dynasty. In fact, ‘rivers and mountains’ is not satisfactory equivalent from its initial Chinese words ‘江山’ . Since in Chinese humanity culture,’jiangshan(江山)’ points out far more merely landscape but country, permeated with the attachment of the nature and nation.

Description: In this project, what I plan to do is to make people appreciate “A Panorama of Rivers and Mountains” via more interactive way. By strictly setting river’s boundaries, a boat(from the painting) could sail on specific area by manipulation. In other words, if a boat move to bank, it would stop shipping on its initial direction and need people adjust its direction(if it is in manipulation). For the issue concerning about how to manipulate a boat, the first approach is using mouse event: boat will sail to the line direction to mouse.  
I changed keypoints here from the various manipulation to various behaviors of boats.The other boats(the player boat need to be activated) can move randomly on limited area, but they would have behaviors like wander, flee(from the player boat) and follow as groups, counted in weight random.
(If having time, the second approach is through OpenCV: the video can identify what the relative location the finger points out.In addition, when a boat come across some sites, events will be activated. )

In preliminary plan, PIL, pygame, tkinter, sys are the basic libraries.

The hard part, in my view, is when boat moves, the picture should also move in calculated distance in same time;there are so many boats with different initial location and attached surface; double-click also approach more larger pics; boats' various behaviors.

