#from imageai.Detection import VideoObjectDetection
#import tensorflow as tf
import numpy as np
import os
import pandas as pd
##
##detector = VideoObjectDetection()
##detector.setModelTypeAsYOLOv3()
##detector.setModelPath("yolo.h5")
##detector.loadModel()
##graph = tf.get_default_graph()
def VideoDetection(file_path,objects=None,min_prob=30):
    print(file_path) # debug
    execution_path = r'./media/output_video'
    #detector = VideoObjectDetection()ṭ
    #detector.setModelTypeAsYOLOv3()
    #detector.setModelPath("yolo.h5")
    #detector.loadModel()
    #graph = tf.get_default_graph() #debug
    if objects:
        print(objects) #debug
        def func(person, truck, bus, bicycle, bird, motorcycle):
            custom = detector.CustomObjects(person=person, truck=truck, bus=bus, bicycle=bicycle, bird=bird,
                                            motorcycle=motorcycle)
            return custom
        custom = func(**objects)
        global graph
        with graph.as_default():
            video_path = detector.detectCustomObjectsFromVideo( custom_objects=custom,
                                                            input_file_path=file_path,
                                                            output_file_path= os.path.join(execution_path ,"Detected {}".format(os.path.basename(file_path[:-4]))),
                                                            frames_per_second=29, minimum_percentage_probability=min_prob,  log_progress=True)
    else:
        
        with graph.as_default():
            video_path = detector.detectObjectsFromVideo(input_file_path=file_path,
                                                     output_file_path=os.path.join(execution_path ,"Detected {}".format(os.path.basename(file_path[:-4]))),
                                                     minimum_percentage_probability=min_prob, frames_per_second=29, log_progress=True)
    #video_path = detector.detectObjectsFromVideo(input_file_path=file_path,
    #                                             output_file_path=os.path.join(execution_path,"Detected {}".format(os.path.basename(file_path[:-4]))),
    #                                             frames_per_second=29, log_progress=True)
    return(video_path)
