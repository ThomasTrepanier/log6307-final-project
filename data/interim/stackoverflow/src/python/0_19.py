import os

image_width = 1280
image_height = 720

def yolo_to_voc_convertion(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = list()
    for line in lines:
        data = line.strip().split(' ')

        class_id = int(data[0])
        x_center = float(data[1])
        y_center = float(data[2])
        width = float(data[3])
        height = float(data[4])

        x_min = int((x_center - (width / 2)) * image_width)
        y_min = int((y_center - (height / 2)) * image_height)
        x_max = int((x_center + (width / 2)) * image_width)
        y_max = int((y_center + (height / 2)) * image_height)

        new_data = f'{class_id} {x_min} {y_min} {x_max} {y_max}\n'
        new_lines.append(new_data)

    with open(output_file, 'w') as f:
        f.writelines(new_lines)

input_folder = '..' # folder that includes .txt files
output_folder = '..' # output folder that will be included new format ann files

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        yolo_to_voc_convertion(input_file, output_file)
