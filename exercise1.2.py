import numpy as np
import matplotlib.pyplot as plt
import rosbag

bag = rosbag.Bag('/home/chaoster/Downloads/ex1.bag')
print(bag.get_message_count())

arr = np.zeros((2,bag.get_message_count()))
arr.shape