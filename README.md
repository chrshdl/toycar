# toycar
playground for autonomous driving

# install ROS
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt-get update
sudo apt-get install ros-melodic-desktop-full


sudo pip3 install -U rosdep
sudo rosdep init
rosdep update

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source .bashrc

sudo pip3 install -U rosinstall vcstools rospkg

echo "export ROS_MASTER_URI=http://localhost:11311" | tee -a ~/.bashrc
echo "export ROS_IP=$(hostname -I)" | tee -a ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH" >> ~/.bashrc
```

# build
The src folder of the root directory is a catkin workspace. To build the project do
```
~/toycar$ catkin_make
```
# Run
```
~/toycar$ . ./devel/setup.bash 
~/toycar/src$ roslaunch sensors launch_sensors.launch
```
