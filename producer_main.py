from src.kafka_producer.json_producer import product_data_using_file
from src.constant import SAMPLE_DIR
import os
if __name__ == '__main__':
    
    topics = os.listdir(SAMPLE_DIR)
    print(f'topics: [{topics}]')
    for topic in topics:
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        product_data_using_file(topic=topic,file_path=sample_file_path)
        # a note here ---- topic name should be same as in sample_data and on confluent cluster topic
        # Otherwise error occurs while producing data on kafka showing UNKNOWN topic