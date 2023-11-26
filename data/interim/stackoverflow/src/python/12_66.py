import argparse

import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2

def parse_arguments():                                                                                                                                                                                                                                                
    parser = argparse.ArgumentParser(description='')                                                                                                                                                                                                                  
    parser.add_argument('pipeline')                                                                                                                                                                                                                                   
    parser.add_argument('output')                                                                                                                                                                                                                                     
    return parser.parse_args()                                                                                                                                                                                                                                        


def main():                                                                                                                                                                                                                                                           
    args = parse_arguments()                                                                                                                                                                                                                                          
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()                                                                                                                                                                                                          

    with tf.io.gfile.GFile(args.pipeline, "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)                                                                                                                                                                                                                 

    pipeline_config.model.ssd.image_resizer.fixed_shape_resizer.height = 300                                                                                                                                                                                          
    pipeline_config.model.ssd.image_resizer.fixed_shape_resizer.width = 300                                                                                                                                                                                           

    config_text = text_format.MessageToString(pipeline_config) 
                                                                                                                                                                                                   
    with tf.io.gfile.GFile(args.output, "wb") as f:                                                                                                                                                                                                                
        f.write(config_text)                                                                                                                                                                                                                                          

if __name__ == '__main__':                                                                                                                                                                                                                                            
    main() 
