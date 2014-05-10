import svgwrite as svg
import xml
import sys
 
 
def convert(input,output,width,height,scale):
        d = xml.etree.ElementTree.parse(input)
        r = d.getroot()
       
        scale = int(scale)
        width = int(width)
        height = int(height)
        
        canvas = svg.Drawing(output, size=(str(width*scale), str(height*scale)))
        canvas.add(canvas.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(0,0,0)'))
        for poly in r.find('Polygons'):
                red = int(poly.find('Brush').find('Red').text)
                blue = int(poly.find('Brush').find('Blue').text)
                green = int(poly.find('Brush').find('Green').text)
                alpha = float(poly.find('Brush').find('Alpha').text)
                alpha = alpha/255
                color = svg.rgb(red,green,blue)
                pts = []
                for point in poly.find('Points'):
                        x = int(point.find('X').text)*scale
                        y = int(point.find('Y').text)*scale
                        pts.append((x,y))
                       
                canvas.add(svg.shapes.Polygon(points=pts, fill=color, opacity=alpha))
        canvas.save()
 
if __name__ == "__main__":
        if (len(sys.argv) != 6):
                print("usage: python xml2svg.py <input.xml> <output.svg> <INT original_width> <INT original_height> <INT scale>")
                sys.exit(0)
        else:
                input = str(sys.argv[1])
                output = str(sys.argv[2])
                width = str(sys.argv[3])
                height = str(sys.argv[4])
                scale = int(sys.argv[5])
                convert(input,output,width,height,scale)
