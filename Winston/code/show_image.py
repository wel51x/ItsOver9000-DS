import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Slider

def update(val):
    
   #do your update here
   pass

image_path = "charts/chart" + str(1) + ".png"
img=mpimg.imread(image_path)
plt.axis('off')
plt.imshow(img)

cat_plot = plt.axes([0.13, 0.02, 0.75, 0.02])
samp = Slider(cat_plot, 'Categ', 1.0, 10.0, valinit=1.0)
samp.on_changed(update)

plt.show()
