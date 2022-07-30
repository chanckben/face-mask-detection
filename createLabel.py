import os
import xml.etree.ElementTree as ET

def generate_box(object):
    bounding_box = object.find('bndbox')
    xmin = bounding_box.find('xmin').text
    ymin = bounding_box.find('ymin').text
    xmax = bounding_box.find('xmax').text
    ymax = bounding_box.find('ymax').text
    return [int(xmin), int(ymin), int(xmax), int(ymax)]

def generate_label(object):
    name = object.find('name').text
    if name == "without_mask":
        return 0
    elif name == "with_mask":
        return 1
    else:
        return 2

annotations_dir = os.path.join(os.curdir, 'annotations')
labels_dir = os.path.join(os.curdir, 'labels')
if not os.path.exists(labels_dir):
    os.mkdir(labels_dir)

for idx in range(len(os.listdir(annotations_dir))):
    xml_filename = f'maksssksksss{idx}.xml'
    xml_dir = os.path.join(annotations_dir, xml_filename)
    tree = ET.parse(xml_dir)
    root = tree.getroot()

    txt_filename = f'maksssksksss{idx}.txt'
    txt_dir = os.path.join(labels_dir, txt_filename)

    size_node = root.find('size')
    im_width = int(size_node.find('width').text)
    im_height = int(size_node.find('height').text)

    with open(txt_dir, 'w') as f:
        for object in root.findall('object'):
            xmin, ymin, xmax, ymax = generate_box(object)
            label = generate_label(object)
            xcenter = round((0.5 * (xmin + xmax)) / im_width, 6)
            ycenter = round((0.5 * (ymin + ymax)) / im_height, 6)
            width = round((xmax - xmin) / im_width, 6)
            height = round((ymax - ymin) / im_height, 6)
            f.write(f'{label} {xcenter} {ycenter} {width} {height}\n')
        f.close()

