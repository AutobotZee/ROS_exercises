import rosbag

bag = rosbag.Bag('/home/chaoster/Downloads/ex1.bag')

for topic , msg , t in bag.read_messages(topics =['/turtle1/pose']):
	print(msg)

bag.close()