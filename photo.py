
from rembg import remove 
from PIL import Image 

file = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fphoto&psig=AOvVaw2GnUIgYhXdwr17RTdyNzWT&ust=1668045433925000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCLj4ybr_n_sCFQAAAAAdAAAAABAD' 
output = '/content/drive/MyDrive/fotografia_convertida.png' 

photoInput = Image.open(file) 
photoWithouthBackground = remove(photoInput) 
photoWithouthBackground.save(output) 
print("😎 Done.")
