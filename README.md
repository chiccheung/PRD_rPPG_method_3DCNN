# Task 1 Research and Development Project : Development of a new rPPG method to be integrated into the pyVHR framework

<em> Author : Florian GIGOT </em>

## Repository architecture :

* notebooks --> Research, explanations, tests

    * Model folder --> Trained model files for experimentation
    * Train_3DCNN_model_BPM --> Jupyter notebook of the new method (3DCNN) implementation (with explanations)
    * Predict_3DCNN_model_BPM --> Jupyter notebook to make predictions with the model with [pyVHR framework](https://github.com/phuselab/pyVHR) constraints (with explanations).
    * Generating_training_data_with_GT --> Jupyter Notebook to create a training dataset from traditional rPPG datasets. Judge its relevance to improve the training of our model

* scripts --> final code

    * Installing_dependencies --> Install libraries for scripts (Windows File)
    * requirements --> List of used libraries + versions
    * training --> Script configuration file
    * training_script --> Script to launch a training session
    * validation_script --> Script to launch a validation session

## Main sources / Reading materials

* G. Boccignone, D. Conte, V. Cuculo, A. D’Amelio, G. Grossi and R. Lanzarotti, "An Open Framework for Remote-PPG Methods and Their Assessment," in IEEE Access, vol. 8, pp. 216083-216103, 2020, doi: 10.1109/ACCESS.2020.3040936. ([Link](https://ieeexplore.ieee.org/document/9272290)) ([GitHub](https://github.com/phuselab/pyVHR))

* Frédéric Bousefsaf, Alain Pruski, Choubeila Maaoui, 3D convolutional neural networks for remote pulse rate measurement and mapping from facial video, Applied Sciences, vol. 9, n° 20, 4364 (2019). ([Link](https://www.mdpi.com/2076-3417/9/20/4364)) ([GitHub](https://github.com/frederic-bousefsaf/ippg-3dcnn))

## Installing

- Python v3.8
- cuda_10.1.243_426.00_win10
- cuDNN v7.6.5.32


* 新建名为 PRD_rPPG，Python 版本3.8 的 conda 环境
  - `conda create -n PRD_rPPG python=3.8`

* 切换 conda 环境到 PRD_rPPG
  - `conda activate PRD_rPPG`

* 安装 cmake，boost
  - `pip install cmake boost`

* 安装 pyVHR 依赖包
  - `pip install -r requirements.txt`

* 切换到 pyVHR 目录
  - `cd C:\Users\chiccheung\Desktop\PRD_rPPG_method_3DCNN-main\pyVHR`

* 手动安装 pyVHR
  - `python setup.py install`
* 安装 ffmpeg
  - `conda install ffmpeg -c conda-forge`
  