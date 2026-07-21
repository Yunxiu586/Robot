[TOC]

# URDF

URDF (Unified Robot Description Format) is a file format for specifying the geometry and organization of robots in ROS.



### Build a model

`<robot>`: The root element defining the robot model with a unique `name`.

+ `<link>`: Represent a rigid body part of the robot with a unique `name`.
  - `<visual>`: Define the visual appearance of a link.
    - `<geometry>`: Specify the shape of the visual element.
      - `<cylinder>`: A cylinder shape defined by `length`and `radius`.
      - `<box>`: A box shape defined by `size`(x, y, z).
      - `<sphere>`: A sphere shape defined by `radius`.
      - `<mesh>`: Imports a 3D mesh from an external file by `filename`.
    - `<origin>`: Define the position (`xyz`) and orientation (`rpy`- roll, pitch, yaw) of the visual / collision geometry relative to that link's coordinate frame.
    - `<material>`: Define the color or texture of the visual element.
      - `<color>`: Define an RGBA color (values 0-1).
      - Can be defined globally and referenced by `name`, or defined locally within a `<visual>`.
  - `<collision>`: Define the geometry used for collision detection.
    - `<geometry>` `<origin>`: The format of `<geometry>` and `<origin>` is exactly the same as with the `<visual>`. In many cases, collision geometry and origin are same as the visual geometry and origin. For quicker processing and safe zones, a simpler geometry (like a cylinder) is often used.

  - `<inertial>`: Define the dynamic properties that a physics engine (like Gazebo) needs to compute the link's motion.
    - `<mass>`: Specify the mass of the link in kilograms.
    - `<inertia>`: Define the 3x3 rotational inertia matrix represented by six values (`ixx`, `ixy`, `ixz`, `iyy`, `iyz`, `izz`) due to symmetry. 
      - This matrix describes how the mass is distributed relative to the link's center of mass. A reasonable default for a  mid-sized link is a value of `1e-3`or smaller for the diagonal elements (`ixx`, `iyy`, `izz`).


+ `<joint>`: Defines a connection between two links with a `type` and unique `name`.

  + `type`
    + `"fixed"`: Specifies a rigid, non-moving joint.
    + `"continuous"`: A rotational joint that can rotate continuously (from -inf to +inf  radians) around a specified axis. Commonly used for wheels or a freely  swiveling head.
    + `"revolute"`: A rotational joint with strict upper and lower angular limits (in radians), defined within a `<limit>` tag. Used for joints with a finite range of motion, like a gripper.
    + `"prismatic"`: A joint that provides linear translational movement along a specified axis. Its limits are defined in meters within a `<limit>` tag.

  - `<axis>`: Define the unit vector around which a `"continuous"` or `"revolute"` joint rotates or along which a prismatic joint translates. For example, `xyz="0 0 1"` specifies the Z-axis.
  - `<limit>`: Define the bounds of the motion.
  - `<parent>`: The parent `link` of the joint.
  - `<child>`: The child `link` of the joint.
  - `<origin>`: Describes where the child link is attached relative to the parent link by `xyz` and `rpy`. If we don’t specify a `rpy` attribute, the child frame will be default have the same orientation as the parent frame.
  - `<dynamics>`: Define the physical properties governing how the joint moves. If not specified, the default value for both coefficients is 0.
    - `friction`: Specify the physical static friction. The unit is Newtons (N) for prismatic joints and Newton meters (N·m) for rotational joints.
    - `damping`: Specify the physical damping value. The unit is N·s/m for prismatic joints and N·m·s/rad for revolving joints.



The code for base link:

```xml
<link name="base_link">
  <visual>
    <geometry>
      <cylinder length="0.6" radius="0.2"/>
    </geometry>
    <material name="blue">
      <color rgba="0 0 .8 1"/>
    </material>
  </visual>
  <collision>
    <geometry>
      <cylinder length="0.6" radius="0.2"/>
    </geometry>
  </collision>
  <inertial>
    <mass value="10"/>
    <inertia ixx="1e-3" ixy="0.0" ixz="0.0" iyy="1e-3" iyz="0.0" izz="1e-3"/>
  </inertial>
</link>
```

The code for left wheel link:

```xml
<link name="left_wheel">
  <visual>
    <geometry>
      <cylinder length="0.1" radius="0.15"/>
    </geometry>
    <material name="black">
      <color rgba="0.1 0.1 0.1 1"/>
    </material>
  </visual>
  <collision>
    <geometry>
      <cylinder length="0.1" radius="0.15"/>
    </geometry>
  </collision>
  <inertial>
    <mass value="2.0"/>
    <inertia ixx="1e-2" ixy="0.0" ixz="0.0" iyy="1e-2" iyz="0.0" izz="2e-2"/>
  </inertial>
</link>
```

The code for the joint:

```xml
<joint name="left_wheel_joint" type="continuous">
  <parent link="base_link"/>
  <child link="left_wheel"/>
  <origin xyz="0 0.25 -0.2" rpy="1.5708 0 0"/>
  <axis xyz="0 1 0"/>
  <dynamics damping="0.1" friction="0.5"/>
</joint>
```



### Use Xacro to clean up your code

The xacro is a macro language for XML. The xacro program runs all of the macros and outputs the result.

#### Contants

Xacro allows you to specify properties which act as constants.

```xml
<xacro:property name="robotname" value="marvin" />
<link name="${robotname}s_leg" />
```

```xml
<link name="marvins_leg" />
```

#### Math

You can build up arbitrarily complex expressions in the ${} construct  using the four basic operations (+,-,*,/), the unary minus, and parenthesis

```xml
<cylinder radius="${wheeldiam/2}" length="0.1"/>
<origin xyz="${reflect*(width+.02)} 0 0.25" />
```

#### Macros

Macros are defined using the `<xacro:macro>` tag with a specified `name` and optional `params`. 

Every instance of a macro call (e.g., `<xacro:macro_name />`) is replaced with the contents of the macro tag during processing, generating equivalent XML.

```xml
<xacro:macro name="default_origin">
    <origin xyz="0 0 0" rpy="0 0 0"/>
</xacro:macro>

<xacro:default_origin />
```

```xml
<origin rpy="0 0 0" xyz="0 0 0"/>
```

Parameters defined in the `params` attribute can be referenced within the macro body using the `${}` syntax.

```xml
<xacro:macro name="default_inertial" params="mass">
    <inertial>
            <mass value="${mass}" />
            <inertia ixx="1e-3" ixy="0.0" ixz="0.0"
                 iyy="1e-3" iyz="0.0"
                 izz="1e-3" />
    </inertial>
</xacro:macro>

<xacro:default_inertial mass="10"/>
```

A block parameter is defined in `params` using the format `*parameter_name`. Inside the macro, this block is inserted using `<xacro:insert_block name="parameter_name" />`.

```xml
<xacro:macro name="blue_shape" params="name *shape">
    <link name="${name}">
        <visual>
            <geometry>
                <xacro:insert_block name="shape" />
            </geometry>
            <material name="blue"/>
        </visual>
        <collision>
            <geometry>
                <xacro:insert_block name="shape" />
            </geometry>
        </collision>
    </link>
</xacro:macro>

<xacro:blue_shape name="base_link">
    <cylinder radius=".42" length=".01" />
</xacro:blue_shape>
```

**Leg macro**

This macro defines a parameterized robot leg (link and joint). By calling it with `prefix="right", reflect="1"`and `prefix="left", reflect="-1"`, it efficiently generates two mirrored leg instances for the left and right sides of the robot body.

```xml
<xacro:macro name="leg" params="prefix reflect">
    <link name="${prefix}_leg">
        <visual>
            <geometry>
                <box size="${leglen} 0.1 0.2"/>
            </geometry>
            <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
            <material name="white"/>
        </visual>
        <collision>
            <geometry>
                <box size="${leglen} 0.1 0.2"/>
            </geometry>
            <origin xyz="0 0 -${leglen/2}" rpy="0 ${pi/2} 0"/>
        </collision>
        <xacro:default_inertial mass="10"/>
    </link>

    <joint name="base_to_${prefix}_leg" type="fixed">
        <parent link="base_link"/>
        <child link="${prefix}_leg"/>
        <origin xyz="0 ${reflect*(width+.02)} 0.25" />
    </joint>
    <!-- A bunch of stuff cut -->
</xacro:macro>

<xacro:leg prefix="right" reflect="1" />
<xacro:leg prefix="left" reflect="-1" />
```

+ Use a name prefix to get two similarly named objects.
+ Use math to calculate joint origins.
+ Using a reflect parameter, and setting it to 1 or -1.



### Use URDF with `robot_state_publisher`

Model a walking robot, publish the state as a tf2 message and view the simulation in Rviz.

#### Create a package

Create the directory:

```
mkdir -p second_ros2_ws/src
```

Then create the package:

```
cd second_ros2_ws/src
ros2 pkg create --build-type ament_python --license Apache-2.0 urdf_tutorial_r2d2 --dependencies rclpy
cd urdf_tutorial_r2d2
```

#### Create the URDF file

Create the directory where we will store some assets:

```
mkdir -p urdf
```

#### Publish the state

`second_ros2_ws/src/urdf_tutorial_r2d2/urdf_tutorial_r2d2/state_publisher.py`

```python
from math import sin, cos, pi
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped


class StatePublisher(Node):

    def __init__(self):
        super().__init__('state_publisher')

        qos_profile = QoSProfile(depth=10)
        # Create a publisher for JointStatemessages on the 'joint_states' topic
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
        # Create a timer to call the updatemethod at 30 Hz
        self.timer = self.create_timer(1/30, self.update)

        self.degree = pi / 180.0

        # robot state
        self.tilt = 0.
        self.tinc = self.degree	# Tilt angle increment per update
        self.swivel = 0.
        self.angle = 0.
        self.height = 0.
        self.hinc = 0.005		# Height increment per update

        # message declarations
        self.odom_trans = TransformStamped()
        self.odom_trans.header.frame_id = 'odom'
        self.odom_trans.child_frame_id = 'axis'
        self.joint_state = JointState()	# Create a JointState message object

        self.get_logger().info("{0} started".format(self.get_name()))

    def update(self):
        # update joint_state
        now = self.get_clock().now()
        self.joint_state.header.stamp = now.to_msg()
        self.joint_state.name = ['swivel', 'tilt', 'periscope']
        self.joint_state.position = [self.swivel, self.tilt, self.height]

        # update transform from 'odom' to 'axis'
        # (moving in a circle with radius=2)
        self.odom_trans.header.stamp = now.to_msg()
        self.odom_trans.transform.translation.x = cos(self.angle)*2
        self.odom_trans.transform.translation.y = sin(self.angle)*2
        self.odom_trans.transform.translation.z = 0.7
        # Make the robot's forward direction (x-axis) tangent to the circular path
        self.odom_trans.transform.rotation = \
            euler_to_quaternion(0, 0, self.angle + pi/2) # roll,pitch,yaw

        # send the joint state and transform
        self.joint_pub.publish(self.joint_state)
        self.broadcaster.sendTransform(self.odom_trans)

        # Create new robot state
        self.tilt += self.tinc
        if self.tilt < -0.5 or self.tilt > 0.0:	# Reverse tilt direction at limits
            self.tinc *= -1
        self.height += self.hinc
        if self.height > 0.2 or self.height < 0.0:	# Reverse height direction at limits
            self.hinc *= -1
        self.swivel += self.degree
        self.angle += self.degree/4


def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)


def main():
    try:
        with rclpy.init():
            node = StatePublisher()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
```

#### Create a launch file

`second_ros2_ws/src/urdf_tutorial_r2d2/launch/demo_launch.py`

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FileContent, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf = FileContent(
        PathJoinSubstitution([FindPackageShare('urdf_tutorial_r2d2'), 'r2d2.urdf.xml']))

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': urdf}],
            arguments=[urdf]),
        Node(
            package='urdf_tutorial_r2d2',
            executable='state_publisher',
            name='state_publisher',
            output='screen'),
    ])
```

#### Edit the `setup.py` file

```python
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
```

```python
data_files=[
  ...
  (os.path.join('share', package_name, 'launch'), glob('launch/*')),
  (os.path.join('share', package_name), glob('urdf/*')),
],
```

```python
'console_scripts': [
    'state_publisher = urdf_tutorial_r2d2.state_publisher:main'
],
```

#### Build and run

```
cd ~/second_ros2_ws
colcon build --symlink-install --packages-select urdf_tutorial_r2d2
. install/setup.bash
```

Launch the package

```
ros2 launch urdf_tutorial_r2d2 demo_launch.py
```

Open a new terminal, the run Rviz using

```
. install/setup.bash
rviz2 -d `ros2 pkg prefix urdf_tutorial_r2d2 --share`/r2d2.rviz
```



# RViz

RViz is a 3D visualizer for the Robot Operating System (ROS) framework.

```
ros2 run rviz2 rivz2
```

