# %%

# -- Modules and packages to import for demo
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.analysis.testsuite import TestSuite, TestResult

# %%

# -- Video object
videoFilename = "./alex_resting/cv_camera_sensor_stream_handler.avi"
video = Video(videoFilename)

# -- extract faces
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')
video.printVideoInfo()

print("\nShow video cropped faces, crop size:", video.cropSize)
video.showVideo()

# %%

# -- define ROIs: free rectangular regions
video.setMask(typeROI='rect', rectCoords=[[15, 20, 140, 50], [10, 120, 100, 30]])
video.printROIInfo()
video.showVideo()

# %%

# -- define ROIs: standard regions, i.e. 'forehead', 'lcheek', 'rcheek', 'nose'
video.setMask(typeROI='rect', rectRegions=['forehead', 'lcheek', 'rcheek', 'nose'])
video.printROIInfo()
video.showVideo()

# %%

# -- define ROIs: using skin, with threshold param
video.setMask(typeROI='skin_adapt', skinThresh_adapt=0.2)
video.printROIInfo()
video.showVideo()

# %%

# -- define ROIs: using skin, with threshold param
video.setMask(typeROI='skin_fix', skinThresh_fix=[20, 50])
video.printROIInfo()
video.showVideo()


# %%

# 定义一个配置文件。它包含与数据集相关的所有信息（如路径 the path），以及测试过程（如超参数 hyperparamenters）。
cfgFilename = '../pyVHR/pyVHR/analysis/default_test.cfg'
# -- apply the pipeline until GT comparison

test = TestSuite(configFilename=cfgFilename)

# -- run exp and save results on a pandas file
#    change verb to see more details as follow:
#       0 - not verbose
#       1 - show the main steps
#       2 - display graphic
#       3 - display spectra
#       4 - display errors
#       (use also combinations, e.g. verb=21, verb=321)
result = test.start(outFilename='sampleExp.h5', verb=4)

# %%

# -- Detailed pipeline for rafinement steps and tuning

# -- define some params in the form of dict (those in the cfg file)
params = {"video": video, "verb": 2, "ROImask": "skin_adapt", "skinAdapt": 0.2}

# -- invoke the method
m = CHROM(**params)
# m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)
