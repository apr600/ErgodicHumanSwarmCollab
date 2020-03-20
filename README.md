Ergodic Human-Swarm Collaboration Simulator
=============================

Decentralized Ergodic Swarm with User Inputs from TanvasTouch Tablet and Task Specifications for object avoidance and convergence.

Create a ros melodic environment with this package in the src folder. 
First source the ros devel/setup file
To run use the following commands:
```
python create_scene.py num_of_agents
```
where num_of_agents is replaced with the number of agents you 
want to see (don't set it higher than 50).

Then to visualize the environment, run: 
```
rosrun rviz rviz 
```
and open the swarm_paths.rviz config in the rviz folder in this repo.

Once running, the swarm can respond in realtime to easter eggs (EEs) to converge upon, disabling devices(DDs) to avoid, and user inputs sent through the TanvasTouch tablet. To send user inputs through the tablet, setup the TanvasTouch communications using the tanvas_comms package.

Send object locations (easter eggs) to converge upon by publishing a geometry_msgs/Pose message with the object location specified in the (x,y) position values of the message to the '/ee_loc' topic.

Send object locations (disabling devices) to avoid by publishing a geometry_msgs/Pose message with the object location specified in the (x,y) position values of the message to the '/dd_loc' topic.

Users can shade regions of interest on the TanvasTouch tablet and the inputs should be published to the /input_array topic. 

