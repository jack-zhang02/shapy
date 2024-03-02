from PIL import Image
import math
import shutil
import os
import json
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', dest='img_path', type=str, help='the image path')
    parser.add_argument('--weight', dest='weight', type=int, help='weight in kg')
    parser.add_argument('--height', dest='height', type=int, help='height in cm')
    return parser.parse_args()

def resize_and_save_image(img_path, weight, height):
    base_im = Image.open('/content/shapy/samples/images/img_01.jpg')
    resize_im = Image.open('/content/' + img_path)

    pixels = base_im.size[0] * base_im.size[1]

    oo1, oo2 = resize_im.size
    npixels = oo1 * oo2
    pixrat = pixels / npixels
    sidrat = math.sqrt(pixrat)

    print(pixrat, sidrat)
    print(base_im.size[0], base_im.size[1])
    print(oo1, oo2)
    
    reim1 = resize_im.resize((int(oo1 * sidrat), int(oo2 * sidrat)))
    print(reim1.size)

    reim1.convert('RGB').save('/content/shapy/samples/images/temp.jpg')
    shutil.copyfile('shapy/samples/openpose/img_01.json', '/content/shapy/samples/openpose/temp.json')

def run_external_commands():
    os.system('cd /shapy/regressor && python demo.py --save-vis true --save-params true --save-mesh true --split test --datasets openpose --output-folder samples/shapy_fit/ --exp-cfg configs/b2a_expose_hrnet_demo.yaml --exp-opts output_folder=../data/trained_models/shapy/SHAPY_A part_key=pose datasets.pose.openpose.data_folder=../samples datasets.pose.openpose.img_folder=images  datasets.pose.openpose.keyp_folder=openpose datasets.batch_size=1 datasets.pose_shape_ratio=1.0')

    shutil.copy('shapy/regressor/samples/shapy_fit/temp.npz', 'shapy/samples/shapy_fit_for_virtual_measurements/temp.npz')
    shutil.copy('shapy/regressor/samples/shapy_fit/temp.ply', 'shapy/samples/shapy_fit_for_virtual_measurements/temp.ply')

    os.system('cd shapy/measurements && python virtual_measurements.py --input-folder ../samples/shapy_fit_for_virtual_measurements/ --output-folder=../samples/virtual_measurements/')
    os.system('python demo.py --exp-cfg configs/s2a.yaml --exp-opts output_dir=../data/trained_models/b2a/polynomial/caesar-female_smplx-neutral-10betas ds_gender=female model_gender=neutral num_shape_comps=10')

def process_results(weight, height):
    attr_path = '/content/shapy/attributes/results.json'
    measure_path = '/content/shapy/measurements/results.json'

    with open(attr_path) as json_file:
        attr = json.load(json_file)
    with open(measure_path) as json_file:
        meas = json.load(json_file)
    print(attr)
    print(meas)

    scalar = math.sqrt(weight / float(meas['mass'])) * height / (float(meas['height']) * 100)
    print(scalar)
    
    bust_size = float(meas['chest']) * 100 * scalar + 35 * (max((float(attr['large_breasts']) - 3.4), 0) ** 2) - 2 * float(attr['petite'])
    under_bust = bust_size - 2.75 * (float(attr['large_breasts'])) - (float(attr['feminine'])) + (float(attr['big'])) - float(attr['petite'])
    cup_depth = (bust_size - under_bust) / 2 * (0.2 + (float(attr['large_breasts']) / 5))

    print(bust_size)
    print(under_bust)
    print(cup_depth)

def main():
    args = parse_arguments()
    resize_and_save_image(args.img_path, args.weight, args.height)
    run_external_commands()
    process_results(args.weight, args.height)

if __name__ == "__main__":
    main()
