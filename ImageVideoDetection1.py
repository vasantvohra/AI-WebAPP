from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import tensorflow as tf
import numpy as np
import os
import pandas as pd

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()
graph = tf.get_default_graph()
def VideoDetection(file_path,objects=None,min_prob=30):
    print(file_path) # debug
    execution_path = r'./media/output_video'
    #detector = VideoObjectDetection()
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
detector1 = ObjectDetection()
detector1.setModelTypeAsYOLOv3()
detector1.setModelPath("yolo.h5")
detector1.loadModel()
graph1 = tf.get_default_graph()
result=tuple()
listt=[]
prob={}
def ImageDetection(file_path,objects=None,min_prob=30):
    print(file_path)
    execution_path = r'./media/output_video'
    #detector = ObjectDetection()
    #detector.setModelTypeAsYOLOv3()
    #detector.setModelPath("yolo.h5")
    #detector.loadModel()
    if objects:
        print(objects)
        def func(person,truck,bus,bicycle,bird,motorcycle):
        #for k,v in objects.items():"%s = %s" % (k,v)
            custom = detector1.CustomObjects(person=person,truck=truck,bus=bus,bicycle=bicycle,bird=bird,motorcycle=motorcycle)
            return custom
        custom = func(**objects)
        global graph1
        with graph1.as_default():
            detections = detector1.detectCustomObjectsFromImage( custom_objects=custom,
                                                            input_image=file_path,
                                                            output_image_path=os.path.join(execution_path ,"Detected {}".format(os.path.basename(file_path))),
                                                            minimum_percentage_probability=min_prob)
    else:
        
        with graph1.as_default():
            detections = detector1.detectObjectsFromImage(input_image=file_path,
                                                     output_image_path=os.path.join(execution_path ,"Detected {}".format(os.path.basename(file_path))),
                                                     minimum_percentage_probability=min_prob)
    global result
    objects=[]
    probs=[]
    for eachObject in detections:
        objects.append(eachObject["name"])
        probs.append(str(np.round(eachObject["percentage_probability"],2))+"%")
        #result = eachObject["name"], str(np.round(eachObject["percentage_probability"],2))+"%"
        #listt.append(result)
    #print('listt',listt)
    #prob.update(listt)
    #print('prob',prob)
    
    
    #for k,v in prob.items():
     #   objects.append(k)
      #  probs.append(v)
    data={'Objects':objects,'Probabilities':probs}
    #print(data)
    dataframe = pd.DataFrame(data)
    #print(dataframe)
    Html = dataframe.to_html(na_rep = "",index=False)
    img_path = "Detected {}".format(os.path.basename(file_path))
    Html = Html.replace('<thead>','<thead class="thead-dark">')
    #Html = Html.replace('<tr>','<tr align="left">')
    Html = Html.replace('<tr style="text-align: right;">',"<tr>")
    Html = Html.replace('<table border="1" class="dataframe">','<table class="dataframe table" style="text-align: left;">')
    print(Html)
    return(Html,img_path)

if __name__=='__main__':
    #objects={'person':True,'chair':False}
    objects = {'truck': True, 'person': True, 'bus': True, 'bicycle': False, 'bird': False,
                   'motorcycle': True}
    print(ImageDetection('./embee.jpg',objects))
    #objects2 = {'truck': True, 'person': False, 'bus': True, 'bicycle': False, 'bird': False,
     #              'motorcycle': True}
    #print(VideoDetection('./media/videos/traffic-mini.mp4',objects2))
