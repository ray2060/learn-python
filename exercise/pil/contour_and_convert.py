from PIL import Image, ImageFilter

inputfilename = input('filename:')
im = Image.open(inputfilename)
im2 = im.convert("L")
im3 = im2.filter(ImageFilter.CONTOUR)
pos = inputfilename.rfind('.')
im3.save(inputfilename[0:pos] + '-out' + inputfilename[pos:])
