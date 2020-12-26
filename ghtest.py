import aplpy
import matplotlib.pyplot as mpl
import montage_wrapper as montage
from astropy import units as u
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import wcsaxes


fig = mpl.figure(figsize=(8, 10))


glimpse3um = '/Users/cutout-reg-j00r.fits'
glimpse4um = '/Users/g8-i2-cutout-reg-j00r.fits'
glimpse8um = '/Users/g8-i4-cutout-reg-j00r.fits'
#I used g8-j00-8um.xy to regrid the files and to be able to have them in j2000
mipsgal24um = '/Users/g8-j00-mips.fits'

image1 = '/Users/g8-ag-j00-cut.fits'
image2 = '/Users/g8subcom-linmos-sup0.fits'


#this one G8 looks darker
aplpy.make_rgb_cube([mipsgal24um,glimpse8um,glimpse3um],'g8-3color.fits')
aplpy.make_rgb_image('g8-3color.fits','g8-3color.tiff',vmin_r=85,stretch_r='log',vmin_g=110,stretch_g='log',stretch_b='linear')


f1 = aplpy.FITSFigure('g8-3color_2d.fits', figure=fig, subplot=[0.15,0.5,0.7,0.5])
f1.recenter(271.3970875,-21.848825, width=0.15, height=0.133) #in degrees in j2000 : center at Ra 18h 05m 35.301s  Dec -21d 50m 55.77s
f1.show_rgb('g8-3color.tiff')

f1.show_contour(image1,levels=[0.21,0.63,1.05,1.47,1.89,2.31],colors='white')
f1.axis_labels.show()
f1.axis_labels.set_xtext('Right Ascension (J2000)')
f1.axis_labels.set_ytext('Declination (J2000)')
f1.tick_labels.set_xformat('hh:mm:ss.s')
f1.tick_labels.set_yformat('dd:mm:ss')
f1.ticks.set_linewidth(1.2)

#region to zoom in  the next panel
f1.show_rectangles(271.38025,-21.827302777,0.025,0.01528,facecolor='none',edgecolor='red',linestyle='dashed',linewidth=3.5)

f2 = aplpy.FITSFigure('g8-3color_2d.fits', figure=fig, subplot=[0.15,0.15,0.7,0.25])
f2.recenter(271.38025,-21.827302777,width=0.025, height=0.01528) #in degrees in j2000 : center at Ra 18h 05m 31.260s  Dec -21d 49m 38.29s #90 arcsec  55 arcsec
f2.show_rgb('g8-3color.tiff')
f2.show_contour(image2,levels=[18e-3,36e-3,54e-3,72e-3,90e-3,0.108,0.126],colors='white',convention='calabretta')
f2.axis_labels.show()
f2.axis_labels.set_xtext('Right Ascension (J2000)')
f2.axis_labels.set_ytext('Declination (J2000)')
f2.tick_labels.set_xformat('hh:mm:ss.s')
f2.tick_labels.set_yformat('dd:mm:ss')
f2.ticks.set_linewidth(1.2)

#sma beam centered at Ra 18h 05m 27.669s  Dec -21d 49m 18.29s
f2.show_ellipses(271.3640416,-21.82180555,0.00202999,0.001423937,-44,facecolor='yellow',edgecolor='yellow')
f2.show_rectangles(271.3640416,-21.8218055,0.0022,0.0022,facecolor='none',edgecolor='yellow',linestyle='solid')

f2.add_scalebar(0.002777)
#f2.show_scalebar()
f2.scalebar.set_length(10 * u.arcsecond)
f2.scalebar.set_corner('top left')
f2.scalebar.set_color('yellow')
f2.scalebar.set_label('0.21 pc')
f2.scalebar.set_linewidth(2)

f2.add_label(0.28, 0.67, 'MM 3', relative=True, color='yellow') #4
f2.add_label(0.57, 0.37, 'MM 1', relative=True, color='yellow') #3
f2.add_label(0.7, 0.15, 'MM 4', relative=True, color='yellow') #2
f2.add_label(0.9, 0.4, 'MM 2', relative=True, color='yellow') #1

f2.show_markers(271.39041667,-21.83027778, edgecolor='yellow',marker='+',facecolor='yellow',s=200,linewidth=1.9)

#arcs
#f2.set_theme('publication')

fig.canvas.draw()
