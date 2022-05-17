# 3dbbox

## Install libraries using PIP
- pip install -r requirements.txt

## Download the pretrained weights and evaluation images (KITTI)
- Link - https://drive.google.com/drive/folders/1mJbEdlki4S_xhyofSSgLe543fucq3L-H?usp=sharing

## Train the model (Optional)
- You need to download the KITTI 3D object detection dataset - http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d
- Download left color images, camera calibration matrices, and training labels 
- Run the train_model jupyter notebook (model saves after every 10 epochs)

# Test the model
- Run the run_mdoel jupyter notebook
- Change the paths for images and corresponding calibration files
- Infer

