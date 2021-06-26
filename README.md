# toycar
playground for autonomous driving

# install ROS
```
sudo apt-get install ros-melodic-desktop-full

sudo pip3 install -U rosdep
sudo rosdep init
rosdep update

sudo pip3 install -U rosinstall vcstools rospkg

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
echo "export ROS_MASTER_URI=http://localhost:11311" | tee -a ~/.bashrc
echo "export ROS_IP=$(hostname -I)" | tee -a ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH" >> ~/.bashrc

source ~/.bashrc
```

# build
The src folder of the root directory is a catkin workspace. To build and run the project do
```
catkin_make

source devel/setup.bash 
roslaunch sensors launch_sensors.launch
```

in a second terminal
```
source devel/setup.bash 
rostopic echo gps
```

gps output
```
time: 214516
latitude: 52.3626289368
longitude: 12.7428302765
fix: 1
satellites: 9
---
time: 214517
latitude: 52.3626327515
longitude: 12.7428302765
fix: 1
satellites: 9
---
```
