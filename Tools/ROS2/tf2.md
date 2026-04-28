# `tf2`

[toc]

### Introduce `tf2`

`tf2` is the **transform library**, which lets the user keep track of multiple **coordinate frames** over time. `tf2` maintains the relationship between coordinate frames in a **tree structure** buffered in time and lets the user **transform points, vectors, etc. **between any two coordinate frames at any desired point in time.

#### Transforms

Published transform $_BT_A^{frame}$ means moving frame A to coincide with frame B, i.e., transforming the frame itself.

While $_BT_A^{data}$ （$_BT_A$） means converting a point/vector from representation in frame A to representation in frame B, i.e., transforming data represented in a frame.

$_BT_A^{data}=(_BT_A^{frame})^{-1}$

#### Position

If $A$ observes something and a person on the ground wants to know its position relative to the ground, transform the observation from the source frame to the target frame.

$_ET_A*P_A^{Obs}=P_E^{Obs}$

If $B$ wants to know where it is too, you can compute the net transform. 

$_BT_E*_ET_A*P_A^{Obs}=_BT_A*P_A^{Obs}=P_B^{Obs}$

$_BT_A$: $A$ is the source `frame_id` and $B$ is the target `frame_id`.

$P_A^{Obs}$: If $P$ is a `Stamped` datatype then $A$ is its `frame_id`.

#### Velocity

$V_{observing\_frame}^{moving\_frame-reference\_frame}$ represents the velocity between the moving frame and the reference frame in the observing frame.

The car A is driving forward (observed in A) at 1m/s (relative to earth). This velocity is expressed as $V_{A}^{A-E} = (1, 0, 0)$. Whereas that same velocity could be observed from the view point of the earth (assume the car is driving east and Earth is NED) , it would be $V_{E}^{A-E} = (0, 1, 0)$.

Same velocity could be observed from different view point:

$_ET_A*V_A^{A-E}=V_E^{A-E}$

Velocities can be directly added or subtracted if they are observed in the **same frame**:

$V_{Obs}^{A-C}=V_{Obs}^{A-B}+V_{Obs}^{B-C}$

Velocities in the reverse direction:

$V_{Obs}^{A-C}=-(V_{Obs}^{C-A})$

To compare two velocities you must transform them into the same observational frame.

**`view_frames`**

```
ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py
```

`view_frames` creates a diagram of the frames being broadcast by tf2 over ROS.

```
ros2 run tf2_tools view_frames
Listening to tf data during 5 seconds...
Generating graph in frames.pdf file...
```

![tf2_frames](/home/yunxiu/Desktop/ROS2_study/Pictures/tf2_frames.png)

Here we can see three frames that are broadcast by tf2: `world`, `turtle1`, and `turtle2`. The `world` frame is the parent of the `turtle1` and `turtle2` frames. `view_frames` also reports some diagnostic information about when the oldest and most recent frame transforms were received and how fast the tf2 frame is published to tf2 for debugging purposes.

**`tf2_echo`**

`tf2_echo` reports the transform between any two frames broadcast over ROS.

```
ros2 run tf2_ros tf2_echo [source_frame] [target_frame]
```

```
ros2 run tf2_ros tf2_echo turtle2 turtle1
[INFO] [1773535832.729811868] [tf2_echo]: Waiting for transform turtle2 ->  turtle1: Invalid frame ID "turtle2" passed to canTransform argument target_frame - frame does not exist
At time 1773535833.711791404
- Translation: [0.000, 0.000, 0.000]
- Rotation: in Quaternion (xyzw) [0.000, 0.000, 0.927, 0.374]
- Rotation: in RPY (radian) [0.000, -0.000, 2.375]
- Rotation: in RPY (degree) [0.000, -0.000, 136.082]
- Matrix:
 -0.720 -0.694  0.000  0.000
  0.694 -0.720  0.000  0.000
  0.000  0.000  1.000  0.000
  0.000  0.000  0.000  1.000
```

**`rviz2`**

`rviz2` is a visualization tool that is useful for examining tf2 frames.

```
ros2 run rviz2 rviz2 -d $(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz
```



### Write a static broadcaster(Python)

Navigate to `src`

```
ros2 pkg create --build-type ament_python --license Apache-2.0 -- learning_tf2_py
```

**Write the static broadcast node**

Inside the `src/learning_tf2_py/learning_tf2_py` directory download the example static broadcaster code 

```
wget https://raw.githubusercontent.com/ros/geometry_tutorials/rolling/turtle_tf2_py/turtle_tf2_py/static_turtle_tf2_broadcaster.py
```

Open the file called `static_turtle_tf2_broadcaster.py`:

```python
import math
import sys

from geometry_msgs.msg import TransformStamped

import numpy as np

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q


class StaticFramePublisher(Node):
    """
    Broadcast transforms that never change.

    This example publishes transforms from `world` to a static turtle frame.
    The transforms are only published once at startup, and are constant for all time.
    """

    def __init__(self, transformation):
        super().__init__('static_turtle_tf2_broadcaster')

        self.tf_static_broadcaster = StaticTransformBroadcaster(self)

        # Publish static transforms once at startup
        self.make_transforms(transformation)

    def make_transforms(self, transformation):
        t = TransformStamped()
		
        # stamp the transform being published with the current time
        t.header.stamp = self.get_clock().now().to_msg()
        # set the name of the parent frame of the link
        t.header.frame_id = 'world'
        # set the name of the child frame of the link
        t.child_frame_id = transformation[1]

        # populate the 6D pose (translation and rotation) of the turtl
        t.transform.translation.x = float(transformation[2])
        t.transform.translation.y = float(transformation[3])
        t.transform.translation.z = float(transformation[4])
        quat = quaternion_from_euler(
            float(transformation[5]), float(transformation[6]), float(transformation[7]))
        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]

        # broadcast static transform using the sendTransform() function
        self.tf_static_broadcaster.sendTransform(t)


def main():
    try:
        logger = rclpy.logging.get_logger('logger')

        # obtain parameters from command line arguments
        if len(sys.argv) != 8:
            logger.info('Invalid number of parameters. Usage: \n'
                        '$ ros2 run learning_tf2_py static_turtle_tf2_broadcaster'
                        'child_frame_name x y z roll pitch yaw')
            sys.exit(1)

        if sys.argv[1] == 'world':
            logger.info('Your static turtle name cannot be "world"')
            sys.exit(2)

        # pass parameters and initialize node
        with rclpy.init():
            node = StaticFramePublisher(sys.argv)
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

**Update `package.xml`**

Navigate back to the `src/learning_tf2_py` directory. Open `package.xml`.

```xml
<description>Learning tf2 with rclpy</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

```xml
<exec_depend>geometry_msgs</exec_depend>
<exec_depend>python3-numpy</exec_depend>
<exec_depend>rclpy</exec_depend>
<exec_depend>tf2_ros_py</exec_depend>
<exec_depend>turtlesim_msgs</exec_depend>
```

**Add an entry point**

Add the entry point to `setup.py`:

```python
'static_turtle_tf2_broadcaster = learning_tf2_py.static_turtle_tf2_broadcaster:main',
```

**Build and run**

```
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select learning_tf2_py
```

Open a new terminal:

```
cd ~/ros2_ws
. install/setup.bash
```

```
ros2 run learning_tf2_py static_turtle_tf2_broadcaster mystaticturtle 0 0 1 0 0 0
```

This sets a turtle pose broadcast for `mystaticturtle` to float 1 meter above the ground.

**The proper way to publish static transforms**

`tf2_ros` provides an executable named `static_transform_publisher` that can be used either as a command line tool or a node that you can add to your launch files.

The following command publishes a static coordinate transform to tf2 resulting in a 1 meter offset in z and no rotation between the frames `world` and `mystaticturtle`.

In ROS 2, roll/pitch/yaw refers to rotation in radians about the x/y/z-axis, respectively.

```
ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --yaw 0 --pitch 0 --roll 0 --frame-id world --child-frame-id mystaticturtle
```

Use quaternion representation for the rotation:

```
ros2 run tf2_ros static_transform_publisher --x 0 --y 0 --z 1 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id world --child-frame-id mystaticturtle
```

use within `launch` files for setting static transforms.

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0', '--y', '0', '--z', '1',
                '--yaw', '0', '--pitch', '0', '--roll', '0',
                '--frame-id', 'world', '--child-frame-id', 'mystaticturtle']
        ),
    ])
```

Check that the static transform:

```
ros2 topic echo /tf_static
transforms:
- header:
    stamp:
      sec: 1773558996
      nanosec: 58532582
    frame_id: world
  child_frame_id: mystaticturtle
  transform:
    translation:
      x: 0.0
      y: 0.0
      z: 1.0
    rotation:
      x: 0.0
      y: 0.0
      z: 0.0
      w: 1.0
---
```



### Write a broadcaster(Python)

#### Write the broadcast node

Inside the `src/learning_tf2_py/learning_tf2_py `directory download the example broadcaster code

```
wget https://raw.githubusercontent.com/ros/geometry_tutorials/rolling/turtle_tf2_py/turtle_tf2_py/turtle_tf2_broadcaster.py
```

`turtle_tf2_broadcaster.py`

```python
import math

# TransformStamped provides us a template for the message 
# that we will publish to the transformation tree
from geometry_msgs.msg import TransformStamped

import numpy as np

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from tf2_ros import TransformBroadcaster

from turtlesim_msgs.msg import Pose


def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q


class FramePublisher(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_publisher')

        # Declare and acquire `turtlename` parameter
        self.turtlename = self.declare_parameter(
          'turtlename', 'turtle').get_parameter_value().string_value

        # Initialize the transform broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

		# Subscribe to topic {self.turtlename}/pose
        # runs function handle_turtle_pose on every incoming message
        self.subscription = self.create_subscription(
            Pose,
            f'/{self.turtlename}/pose',
            self.handle_turtle_pose,
            1)
        self.subscription  # prevent unused variable warning

    def handle_turtle_pose(self, msg):
        t = TransformStamped()

        # Read message content and assign it to corresponding tf variables
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = self.turtlename

        # Turtle only exists in 2D, thus we get x and y translation 
        # coordinates from the message and set the z coordinate to 0
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0

        # For the same reason, turtle can only rotate around one axis 
        # and this why we set rotation in x and y to 0 
        # and obtain rotation in z axis from the message
        q = quaternion_from_euler(0, 0, msg.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        # Broadcast a transform from parent frame to child frame
        # Describe the pose of the child frame relative to the parent frame
        self.tf_broadcaster.sendTransform(t)


def main():
    try:
        with rclpy.init():
            node = FramePublisher()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

$_{world}T_{turtle1}^{data}$

```python
self.tf_broadcaster.sendTransform(t)
```

$P_{world}=_{world}T_{turtle1}^{data}*P_{turtle1}$

**Add an entry point**

 Add the entry point to `setup.py`

```
'turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main',
```

#### Write the launch file

Create a `launch` folder in the `src/learning_tf2_py` directory. Create a file called `turtle_tf2_demo_launch.py` in the `launch` folder.

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
    ])
```

**Add dependencies**

Navigate back to the `learning_tf2_py` directory. Open `package.xml`

```xml
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

**Update `setup.py`**

```python
import os
from glob import glob

data_files=[
    ...
    (os.path.join('share', package_name, 'launch'), glob('launch/*')),
],
```

**Build and run**

```
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select learning_tf2_py
```

Open a new terminal:

```
cd ~/ros2_ws
. install/setup.bash
```

```
ros2 launch learning_tf2_py turtle_tf2_demo_launch.py
```

```
ros2 run turtlesim turtle_teleop_key
```

Use the `tf2_echo` tool to check if the turtle pose is actually getting broadcast to tf2:

```
ros2 run tf2_ros tf2_echo world turtle1
```

```
At time 1773561778.397856073
- Translation: [7.519, 5.631, 0.000]
- Rotation: in Quaternion (xyzw) [0.000, 0.000, 0.846, 0.534]
- Rotation: in RPY (radian) [0.000, -0.000, 2.016]
- Rotation: in RPY (degree) [0.000, -0.000, 115.508]
- Matrix:
 -0.431 -0.903  0.000  7.519
  0.903 -0.431  0.000  5.631
  0.000  0.000  1.000  0.000
  0.000  0.000  0.000  1.000
```



### Write a listener(Python)

#### Write the listener node

Inside the `src/learning_tf2_py/learning_tf2_py` directory download the example listener code

```
wget https://raw.githubusercontent.com/ros/geometry_tutorials/rolling/turtle_tf2_py/turtle_tf2_py/turtle_tf2_listener.py
```

`turtle_tf2_listener.py`: Command `turtle2` to follow `turtle1` using `tf2` transforms.

```python
import math

from geometry_msgs.msg import Twist

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from turtlesim_msgs.srv import Spawn


class FrameListener(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

        # Declare and acquire `target_frame` parameter
        self.target_frame = self.declare_parameter(
          'target_frame', 'turtle1').get_parameter_value().string_value

        # Once the listener is created, it starts receiving tf2 transformations
        # and buffers them for up to 10 seconds
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Create a client to spawn a turtle
        self.spawner = self.create_client(Spawn, 'spawn')
        # Boolean values to store the information
        # if the service for spawning turtle is available
        self.turtle_spawning_service_ready = False
        # if the turtle was successfully spawned
        self.turtle_spawned = False

        # Create turtle2 velocity publisher
        self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 1)

        # Call on_timer function every second
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        # Store frame names in variables that will be used to compute transformations
        from_frame_rel = self.target_frame
        to_frame_rel = 'turtle2'

        if self.turtle_spawning_service_ready:
            if self.turtle_spawned:
                # Look up the transform from source frame to turtle2 (target) frame.
                # and send velocity commands for turtle2 to reach target_frame
                try:
                    t = self.tf_buffer.lookup_transform(
                        to_frame_rel,
                        from_frame_rel,
                        rclpy.time.Time())
                except TransformException as ex:
                    self.get_logger().info(
                        f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
                    return

                msg = Twist()
                scale_rotation_rate = 1.0
                msg.angular.z = scale_rotation_rate * math.atan2(
                    t.transform.translation.y,
                    t.transform.translation.x)

                scale_forward_speed = 0.5
                msg.linear.x = scale_forward_speed * math.sqrt(
                    t.transform.translation.x ** 2 +
                    t.transform.translation.y ** 2)

                self.publisher.publish(msg)
            else:
                if self.result.done():
                    self.get_logger().info(
                        f'Successfully spawned {self.result.result().name}')
                    self.turtle_spawned = True
                else:
                    self.get_logger().info('Spawn is not finished')
        else:
            if self.spawner.service_is_ready():
                # Initialize request with turtle name and coordinates
                # x, y and theta are defined as floats in turtlesim_msgs/srv/Spawn
                request = Spawn.Request()
                request.name = 'turtle2'
                request.x = float(4)	# 4.0
                request.y = float(2)	# 2.0
                request.theta = float(0)# 0.0
                # Call request
                self.result = self.spawner.call_async(request)
                self.turtle_spawning_service_ready = True
            else:
                # Check if the service is ready
                self.get_logger().info('Service is not ready')


def main():
    try:
        with rclpy.init():
            node = FrameListener()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

$_{turtle2}T_{turtle1}^{data}$: Transform a representation from source frame to the target frame.

```python
t = self.tf_buffer.lookup_transform(
    to_frame_rel,		# target frame
    from_frame_rel,		# source frame
    rclpy.time.Time())	# the time at which we want to transform
```

**Add an entry point**

 Add the entry point to `setup.py`

```python
'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
```

#### Update launch file

Open the launch file called `turtle_tf2_demo_launch.py`

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='learning_tf2_py',
            executable='turtle_tf2_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])
```

**Build and run**

```
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select learning_tf2_py
```

Open a new terminal:

```
. install/setup.bash
ros2 launch learning_tf2_py turtle_tf2_demo_launch.py
```

```
ros2 run turtlesim turtle_teleop_key
```



### Add a frame(Python)

#### tf2 tree

tf2 builds up a tree structure of frames and doesn't allow a closed loop in the frame structure. This means that a frame only has one single parent, but it can have multiple children.

If we want to add a new frame to tf2, one of the existing frames needs to be the parent frame, and the new one will become its child  frame.

#### Write the fixed frame broadcaster

Inside the `src/learning_tf2_py/learning_tf2_py` directory download the fixed frame broadcaster code

```
wget https://raw.githubusercontent.com/ros/geometry_tutorials/rolling/turtle_tf2_py/turtle_tf2_py/fixed_frame_tf2_broadcaster.py
```

`fixed_frame_tf2_broadcaster.py`

```python
from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from tf2_ros import TransformBroadcaster


class FixedFrameBroadcaster(Node):

   def __init__(self):
       super().__init__('fixed_frame_tf2_broadcaster')
       self.tf_broadcaster = TransformBroadcaster(self)
       self.timer = self.create_timer(0.1, self.broadcast_timer_callback)

   def broadcast_timer_callback(self):
       t = TransformStamped()

       t.header.stamp = self.get_clock().now().to_msg()
       # Create a new transform from the parent turtle1 to the new child carrot1
       t.header.frame_id = 'turtle1'
       t.child_frame_id = 'carrot1'
       # carrot1 frame is 2 meters offset in y axis in terms of the turtle1 frame
       t.transform.translation.x = 0.0
       t.transform.translation.y = 2.0
       t.transform.translation.z = 0.0
       t.transform.rotation.x = 0.0
       t.transform.rotation.y = 0.0
       t.transform.rotation.z = 0.0
       t.transform.rotation.w = 1.0

       self.tf_broadcaster.sendTransform(t)


def main():
    try:
        with rclpy.init():
            node = FixedFrameBroadcaster()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

The code is very similar to the tf2 broadcaster tutorial example and the only difference is that the transform here does not change over time.

**Add an entry point**

 Add the entry point to `setup.py`

```
'fixed_frame_tf2_broadcaster = learning_tf2_py.fixed_frame_tf2_broadcaster:main',
```

**Write the launch file**

`turtle_tf2_fixed_frame_demo_launch.py`

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        # Include launch file turtle_tf2_demo_launch.py
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('learning_tf2_py'), 'launch', 'turtle_tf2_demo_launch.py'])
        ),
        # Add our fixed carrot1 frame to the turtlesim world
        Node(
            package='learning_tf2_py',
            executable='fixed_frame_tf2_broadcaster',
            name='fixed_broadcaster',
        ),
    ])
```

**Build and run**

```
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select learning_tf2_py
```

Open a new terminal:

```
cd ~/ros2_ws
. install/setup.bash
```

```
ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo_launch.py
```

```
ros2 run turtlesim turtle_teleop_key
```

Because adding an extra frame does not affect the other frames and our listener is still using the previously defined frames.

Therefore, if we want our second turtle to follow the carrot instead of the first turtle, we need to change value of the `target_frame`.

```
ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo_launch.py target_frame:=carrot1
```

The second way is to update the launch file. To do so, open the `turtle_tf2_fixed_frame_demo_launch.py` file, and add the `'target_frame': 'carrot1'` parameter via `launch_arguments` argument.

```python
def generate_launch_description():
    demo_nodes = IncludeLaunchDescription(
        ...,
        launch_arguments={'target_frame': 'carrot1'}.items(),
        )
```

Now rebuild the package, restart the `turtle_tf2_fixed_frame_demo_launch.py`, and you’ll see the second turtle following the carrot instead of the first turtle.

#### Write the dynamic frame broadcaster

Inside the `src/learning_tf2_py/learning_tf2_py` directory download the dynamic frame broadcaster code

```
wget https://raw.githubusercontent.com/ros/geometry_tutorials/rolling/turtle_tf2_py/turtle_tf2_py/dynamic_frame_tf2_broadcaster.py
```

`dynamic_frame_tf2_broadcaster.py`:

```python
import math

from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from tf2_ros import TransformBroadcaster


class DynamicFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('dynamic_frame_tf2_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)

    def broadcast_timer_callback(self):
        seconds, _ = self.get_clock().now().seconds_nanoseconds()
        x = seconds * math.pi

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot1'
        # The offset of carrot1 is constantly changing
        t.transform.translation.x = 10 * math.sin(x)
        t.transform.translation.y = 10 * math.cos(x)
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)


def main():
    try:
        with rclpy.init():
            node = DynamicFrameBroadcaster()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

**Add an entry point**

 Add the entry point to `setup.py`

```python
'dynamic_frame_tf2_broadcaster = learning_tf2_py.dynamic_frame_tf2_broadcaster:main',
```

**Write the launch file**

`turtle_tf2_dynamic_frame_demo_launch.py`

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('learning_tf2_py'), 'launch', 'turtle_tf2_demo_launch.py']),
            launch_arguments={'target_frame': 'carrot1'}.items(),
        ),
        Node(
            package='learning_tf2_py',
            executable='dynamic_frame_tf2_broadcaster',
            name='dynamic_broadcaster',
        ),
    ])
```

**Build and run**

```
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select learning_tf2_py
```

Open a new terminal:

```
cd ~/ros2_ws
. install/setup.bash
```

```
ros2 launch learning_tf2_py turtle_tf2_dynamic_frame_demo_launch.py
```

```
ros2 run turtlesim turtle_teleop_key
```

The second turtle is following the carrot’s position that is constantly changing

The builtin `list` is used in Python

```python
from geometry_msgs.msg import Quaternion
...

# Create a list of floats, which is compatible with tf2
# Quaternion methods
quat_tf = [0.0, 1.0, 0.0, 0.0]

# Convert a list to geometry_msgs.msg.Quaternion
msg_quat = Quaternion(x=quat_tf[0], y=quat_tf[1], z=quat_tf[2], w=quat_tf[3])
```



### Quaternion fundamentals

A quaternion is a 4-tuple representation of orientation. 

The magnitude of a quaternion should always be one.

**Quaternion operations**

**Think in PRY then convert to quaternion**

```python
q = quaternion_from_euler(1.5707, 0, -1.5707)
print(f'The quaternion representation is x: {q[0]} y: {q[1]} z: {q[2]} w: {q[3]}.')
```

**Apply a quaternion rotation**

To apply the rotation of one quaternion to a pose, simply multiply the  previous quaternion of the pose by the quaternion representing the  desired rotation. The order of this multiplication matters.

```python
q_orig = quaternion_from_euler(0, 0, 0)
# Rotate the previous pose by 180* about X
q_rot = quaternion_from_euler(3.14159, 0, 0)
q_new = quaternion_multiply(q_rot, q_orig)
```

**Inverting a quaternion**

An easy way to invert a quaternion is to negate the x-, y-, and z-components:

```python
q[0] = -q[0]
q[1] = -q[1]
q[2] = -q[2]
```

**Relative rotations**

Two quaternions from the same frame, `q_1` and `q_2`:

```
q_2 = q_r * q_1
```

Solve for `q_r`:

```
q_r = q_2 * q_1_inverse
```

```python
def quaternion_multiply(q0, q1):
    """
    Multiplies two quaternions.

    Input
    :param q0: A 4 element array containing the first quaternion (q01, q11, q21, q31)
    :param q1: A 4 element array containing the second quaternion (q02, q12, q22, q32)

    Output
    :return: A 4 element array containing the final quaternion (q03,q13,q23,q33)

    """
    # Extract the values from q0
    x0 = q0[0]
    y0 = q0[1]
    z0 = q0[2]
    w0 = q0[3]

    # Extract the values from q1
    x1 = q1[0]
    y1 = q1[1]
    z1 = q1[2]
    w1 = q1[3]

    # Compute the product of the two quaternions, term by term
    q0q1_w = w0 * w1 - x0 * x1 - y0 * y1 - z0 * z1
    q0q1_x = w0 * x1 + x0 * w1 + y0 * z1 - z0 * y1
    q0q1_y = w0 * y1 - x0 * z1 + y0 * w1 + z0 * x1
    q0q1_z = w0 * z1 + x0 * y1 - y0 * x1 + z0 * w1

    # Create a 4 element array containing the final quaternion
    final_quaternion = np.array([q0q1_w, q0q1_x, q0q1_y, q0q1_z])

    # Return a 4 element array containing the final quaternion (q02,q12,q22,q32)
    return final_quaternion

q1_inv[0] = -prev_pose.pose.orientation.x   # Negate for inverse
q1_inv[1] = -prev_pose.pose.orientation.y   # Negate for inverse
q1_inv[2] = -prev_pose.pose.orientation.z   # Negate for inverse
q1_inv[3] = prev_pose.pose.orientation.w

q2[0] = current_pose.pose.orientation.x
q2[1] = current_pose.pose.orientation.y
q2[2] = current_pose.pose.orientation.z
q2[3] = current_pose.pose.orientation.w

qr = quaternion_multiply(q2, q1_inv)
```

