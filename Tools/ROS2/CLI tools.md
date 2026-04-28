# ROS 2

**Robot Operating System 2**

ROS 2 relies on the notion of combining workspaces using the shell environment. The core ROS 2 workspace is called the **underlay**. Subsequent local workspaces are called **overlays**. When developing with ROS 2, you will typically have several workspaces active concurrently.



# CLI Tools

**Command Line Interface Tools**

[toc]

### nodes

A node is a fundamental ROS 2 element that serves a single, modular purpose in a robotics system. 

Each node can send and receive data from other nodes via topics, services, actions, or parameters. 

Nodes are often a complex combination of publishers, subscribers,  service servers, service clients, action servers, and action clients,  all at the same time.

**ros2 run**

```
ros2 run <package_name> <executable_name>
```

Open a new terminal to run turtlesim.

```
ros2 run turtlesim turtlesim_node
```

**ros2 node list**

The package name is `turtlesim` and the executable name is `turtlesim_node`. Open a new terminal while turtlesim is still running in the other one. Find **node names** by using:

```
ros2 node list
/turtlesim
```

Open another new terminal and start the teleop node.

```
ros2 run turtlesim turtle_teleop_key
```

Return to the terminal where you ran `ros2 node list` and run it again.

```
ros2 node list
/turtlesim
/teleop_turtle
```

**Remapping**

Remapping allows you to reassign default node properties, like node name, topic names, service names, etc., to custom values.

Reassign the name of  `/turtlesim` node. In a new terminal:

```
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```

Return to the terminal where you ran `ros2 node list` and run it again

```
/my_turtle
/turtlesim
/teleop_turtle
```

**ros2 node info**

```
ros2 node info <node_name>
```

`ros2 node info` returns a list of subscribers, publishers, services, and actions. i.e. the ROS graph connections that interact with that node.

```
ros2 node info /turtlesim
```



### Interfaces

ROS applications typically communicate through interfaces of one of three types: **topics**, **services**, or **actions**. ROS 2 uses a simplified description language, the interface definition language (IDL), to describe these interfaces. This description makes it easy for ROS tools to automatically generate  source code for the interface type in several target languages.

+ msg: `.msg` files are simple text files that describe the fields of a ROS message. They are used to generate source code for messages in different languages.

+ srv: `.srv` files describe a service. They are composed of two parts: a request and a response. The request and response are message declarations.

+ action: `.action` files describe actions. They are composed of three parts: a goal, a result, and feedback. Each part is a message declaration itself.

#### Messages

**Fields**

Each field consists of a type and a name, separated by a space, i.e:

```
fieldtype fieldname
```

**Field default values**

```
fieldtype fieldname fielddefaultvalue
```

For example:

```
uint8 x 42
string full_name "John Doe"
int32[] samples [-200, -100, 0, 100, 200]
```

String values must be defined in single `'` or double `"` quotes.

**Constants**

Constants names have to be UPPERCASE.

```
constanttype CONSTANTNAME=constantvalue
```

```
int32 X=123
string EXAMPLE='bar'
```

#### Services

Services are described and defined in `.srv` files in the `srv/` directory of a ROS package.

A service description file consists of a request and a response msg type, separated by `---`. Any two `.msg` files concatenated with a `---` are a legal service description. For example:

```
string str
---
string str
```

#### Actions

Action definitions have the following form:

```
<request_type> <request_fieldname>
---
<response_type> <response_fieldname>
---
<feedback_type> <feedback_fieldname>
```

For instance, the `Fibonacci` action definition contains the following:

```
int32 order
---
int32[] sequence
---
int32[] sequence
```



### topics

Nodes publish information over topics, which allows any number of other nodes to subscribe to and access that information. 

Start up the two turtlesim nodes, `/turtlesim` and `/teleop_turtle`.

Open a new terminal and run:

```
ros2 run turtlesim turtlesim_node
```

Open another terminal and run:

```
ros2 run turtlesim turtle_teleop_key
```

**ros2 topic list** 

Running the `ros2 topic list` command in a new terminal.

```
ros2 topic list
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

`ros2 topic list -t` will return **the same list of topics** with the **topic type** appended in brackets. These attributes, particularly the type, are how nodes know they’re talking about the same information as it moves over topics.

```
ros2 topic list -t
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/turtle1/cmd_vel [geometry_msgs/msg/Twist]
/turtle1/color_sensor [turtlesim_msgs/msg/Color]
/turtle1/pose [turtlesim_msgs/msg/Pose]
```

```
# topic_name [topic_type]
```

**ros2 topic echo**

To see the data being published on a topic:

```
ros2 topic echo <topic_name>
```

`/teleop_turtle` publishes data to `/turtlesim` over the `/turtle1/cmd_vel` topic, use `echo` to introspect that topic:

```
ros2 topic echo /turtle1/cmd_vel
```

Return to the terminal where `turtle_teleop_key` is running and use the arrows to move the turtle around.

```
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: -2.0
---
```

**ros2 topic info**

```
ros2 topic info /turtle1/cmd_vel
Type: geometry_msgs/msg/Twist
Publisher count: 1
Subscription count: 1
```

For more detailed information about a topic

```
ros2 topic info /turtle1/cmd_vel --verbose
```

**ros2 interface show**

Nodes send data over topics using **messages**. Publishers and subscribers must send and receive the same type of message to communicate.

The topic types we saw earlier after running `ros2 topic list -t`. The `cmd_vel` topic has the type

```
geometry_msgs/msg/Twist
```

This means that in the package `geometry_msgs` there is a `msg` called `Twist`.

Run `ros2 interface show <msg_type>` on this type to learn what **message type** is used on each topic, in another words, **what structure of data the message expects**.

```
ros2 interface show geometry_msgs/msg/Twist
# This expresses velocity in free space broken into its linear and angular parts.
    Vector3  linear
            float64 x
            float64 y
            float64 z
    Vector3  angular
            float64 x
            float64 y
            float64 z
```

The `/turtlesim` node is expecting a message with two vectors, `linear` and `angular`, of three elements each.

**ros2 topic pub**

Publish data to a topic directly from the command line using

```
ros2 topic pub <topic_name> <msg_type> '<args>'
```

There are four main ways to use the `pub` command

a.**Publish dictionary strings**

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
```

b.**Publish an empty message**

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist
```

This will publish the default values for the message type at 1 Hz. In this case, this equivalent to

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" --rate 1
```

c.**Using autocomplete**

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist <TAB>
```

d.**Using the raw autocompleted string**

```
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist \'linear:\^J\ \ x:\ 0.0\^J\ \ y:\ 0.0\^J\ \ z:\ 0.0\^Jangular:\^J\ \ x:\ 0.0\^J\ \ y:\ 0.0\^J\ \ z:\ 0.0\^J\'
```

To publish your command just once add the `--once` option.

```
ros2 topic pub --once -w 2 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

`--once` is an optional argument meaning “publish one message then exit”.

`-w 2` is an optional argument meaning “wait for two matching subscriptions”. This is needed because we have both turtlesim and the topic echo subscribed.

**ros2 topic hz**

View the rate at which data is published

```
ros2 topic hz /turtle1/pose
```

Return data on the rate at which the `/turtlesim` node is publishing data to the `pose` topic.

**ros2 topic bw**

The bandwidth used by a topic can be viewed using:

```
ros2 topic bw /turtle1/pose
```

Return the bandwidth utilization and number of messages being published to the `/turtle1/pose` topic.

The rate/bandwidth reflects the receiving rate on the subscription created by the `ros2 topic hz` command, which might be affected by platform resources and QoS configuration, and may not exactly match the publisher rate/bandwidth.

**ros2 topic find**

To list a list of available topics of a given type

```
ros2 topic find <topic_type>
```

```
ros2 topic find geometry_msgs/msg/Twist
/turtle1/cmd_vel
```



### services

A service is a **request/response pattern** where a client makes a request to a node providing the service and the service processes the request and generates a response. There can be many service clients using same service. But there can **only be one service server** for a service. 

Services only provide data when they are specifically called by a client. We generally don’t want to use a service for continuous calls; topics or even actions would be better suited.

Open a new terminal and run:

```
ros2 run turtlesim turtlesim_node
```

Open another terminal and run:

```
ros2 run turtlesim turtle_teleop_key
```

**ros2 service list**

Running the `ros2 service list` command in a new terminal will return a list of all the services currently active in the system.

```
ros2 service list
/clear
/kill
...
/turtle1/set_pen
/turtle1/teleport_absolute
...
```

**ros2 service type**

Service types have two parts: one message for the request and another for the response.

```
ros2 service type <service_name>
```

In a new terminal:

```
os2 service type /clear
std_srvs/srv/Empty
```

The `Empty` type means the service call sends no data when making a request and receives no data when receiving a response.

**ros2 service list -t**

See the types of all the active services at the same time, append the `--show-types` option, abbreviated as `-t`.

```
ros2 service list -t
/clear [std_srvs/srv/Empty]
/kill [turtlesim_msgs/srv/Kill]
...
/turtle1/set_pen [turtlesim_msgs/srv/SetPen]
/turtle1/teleport_absolute [turtlesim_msgs/srv/TeleportAbsolute]
...
```

**ros2 service info**

```
ros2 service info <service_name>
```

```
ros2 service info /clear
Type: std_srvs/srv/Empty
Clients count: 0
Services count: 1
```

**ros2 service info -verbose**

```
ros2 service info --verbose <service_name>
```

The `Endpoint count` will be 2 for DDS based ROS middleware interface (RMW) because DDS creates two endpoints (one for request and one for response) for each service server. Where as for non-DDS based RMW implementations will be 1 because it uses a single endpoint for both request and response.

**ros2 service find**

Find all the services of a specific type.

```
ros2 service find <type_name>
```

```
ros2 service find std_srvs/srv/Empty
/clear
/reset
```

**ros2 interface show**

```
ros2 interface show <type_name>
```

To see the request and response arguments of the `/spawn` service:

```
ros2 interface show turtlesim_msgs/srv/Spawn
float32 x
float32 y
float32 theta
string name # Optional.  A unique name will be created and returned if this is empty
---
string name
```

The information above the `---` line tells us the arguments needed to call `/spawn`. `x`, `y` and `theta` determine the 2D pose of the spawned turtle, and `name` is clearly optional. 

The information below the line represents the data type of the response.

**ros2 service call**

```
ros2 service call <service_name> <service_type> <arguments>
```

The `<arguments>` part is optional. For example, you know that `Empty` typed services don’t have any arguments.

```
ros2 service call /clear std_srvs/srv/Empty
```

This command will clear the turtlesim window of any lines your turtle has drawn.

Spawn a new turtle by calling `/spawn` and setting arguments,

```
ros2 service call /spawn turtlesim_msgs/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
waiting for service to become available...
requester: making request: turtlesim_msgs.srv.Spawn_Request(x=2.0, y=2.0, theta=0.2, name='')

response:
turtlesim_msgs.srv.Spawn_Response(name='turtle2')
```

**ros2 service echo**

To see the data communication between a service client and a service server:

```
ros2 service echo <service_name | service_type> <arguments>
```

`ros2 service echo` depends on service **introspection** of a service client and server, that is disabled by default. To enable it, users must call `configure_introspection` after creating a service client or server.



### parameters

Nodes have parameters to define their default configuration values.

Open a new terminal and run:

```
ros2 run turtlesim turtlesim_node
```

Open another terminal and run:

```
ros2 run turtlesim turtle_teleop_key
```

**ros2 param list**

To see the parameters belonging to your nodes, open a new terminal and enter:

```
ros2 param list
/teleop_turtle:
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  ...
/turtlesim:
  background_b
  background_g
  ...
```

Return the node namespaces, `/teleop_turtle` and `/turtlesim`, followed by each node’s parameters.

The namespaces of the parameter and its name are separated using dots, for example, in `parameter_events.publisher.depth`. Every node has the parameter `use_sim_time`.

**ros2 param get**

To display the type and current value of a parameter:

```
ros2 param get <node_name> <parameter_name>
```

```
ros2 param get /turtlesim background_g
Integer value is: 86
```

```
ros2 param get /turtlesim use_sim_time
Boolean value is: False
```

**ros2 param set**

Change parameters in current session, not permanently.

```
ros2 param set <node_name> <parameter_name> <value>
```

```
ros2 param set /turtlesim background_r 150
Set parameter successful
```

**ros2 param dump**

View all of a node’s current parameter values.

```
ros2 param dump <node_name>
```

To save your current configuration of `/turtlesim`’s parameters into the file `turtlesim.yaml` in the current working directory.

```
ros2 param dump /turtlesim > turtlesim.yaml
```

**ros param load**

Load parameters from a file to a currently running node.

```
ros2 param load <node_name> <parameter_file>
```

**load parameter file on node startup**

Read-only parameters can only be modified at startup and not afterwards. When a parameter file is used at node startup, all parameters, including the read-only ones, will be updated.

```
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
```

```
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim.yaml
```



### actions

Actions allow to execute **long running tasks**, provide regular **feedback**, and are **cancelable**. While the robot navigates to the position, it can send updates along the way (i.e. feedback), and then a final result message once it’s reached  its destination.

Actions are built on topics and services.

Actions use a client-server model.

Open a new terminal and run:

```
ros2 run turtlesim turtlesim_node
```

Open another terminal and run:

```
ros2 run turtlesim turtle_teleop_key
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
```

**Use actions**

The `/teleop_turtle` node sends rotation goals to the `/turtlesim` action server using keys G|B|V|C|D|E|R|T around the 'F' key, which correspond to absolute orientations. 

```
[INFO] [1772617071.711716511] [turtlesim]: Rotation goal completed successfully
```

The 'F' key cancels a goal from the **client side**. 

```
[INFO] [1772617100.499884251] [turtlesim]: Rotation goal canceled
```

The **action server** can complete goals successfully, or **abort** a current goal if it receives a new one before the previous  finishes. It could have chosen something else, like reject the new goal or execute the second goal after the first one finished.

```
[WARN] [1772617159.747444224] [turtlesim]: Rotation goal received before a previous goal finished. Aborting previous goal
```

**ros2 node info**

```
ros2 node info /turtlesim
/turtlesim
  ...
  Action Servers:
    /turtle1/rotate_absolute: turtlesim_msgs/action/RotateAbsolute
  Action Clients:
```

The `/turtle1/rotate_absolute` action for `/turtlesim` is under `Action Servers`. This means `/turtlesim` responds to and provides feedback for the `/turtle1/rotate_absolute` action.

**ros2 action list**

To identify all the actions in the ROS graph,

```
ros2 action list
/turtle1/rotate_absolute
```

**ros2 action list -t**

To find `/turtle1/rotate_absolute`’s type,

```
ros2 action list -t
/turtle1/rotate_absolute [turtlesim_msgs/action/RotateAbsolute]
```

**ros2  action type**

To check the action type for the action,

```
ros2 action type /turtle1/rotate_absolute
turtlesim_msgs/action/RotateAbsolute
```

**ros2  action info**

Further introspect the `/turtle1/rotate_absolute` action 

```
ros2 action info /turtle1/rotate_absolute
Action: /turtle1/rotate_absolute
Action clients: 1
    /teleop_turtle
Action servers: 1
    /turtlesim
```

The `/teleop_turtle` node has an action client and the `/turtlesim` node has an action server for the `/turtle1/rotate_absolute` action.

**ros2 interface show**

```
ros2 interface show turtlesim_msgs/action/RotateAbsolute
# The desired heading in radians
float32 theta
---
# The angular displacement in radians to the starting position
float32 delta
---
# The remaining rotation in radians
float32 remaining
```

The section of this message above the first `---` is the structure (data type and name) of the **goal request**. The next section is the structure of the **result**. The last section is the structure of the **feedback**.

**ros2  action send_goal**

Send an action goal from the command line.

```
ros2 action send_goal <action_name> <action_type> <values>
```

```
ros2 action send_goal /turtle1/rotate_absolute turtlesim_msgs/action/RotateAbsolute "{theta: 1.57}"
waiting for an action server to become available...
Sending goal:
     theta: 1.57

Goal accepted with ID: 6245d39154684bafba8f765b2dcc1576

Result:
    delta: -1.5520000457763672

Goal finished with status: SUCCEEDED
```

All goals have a unique ID in the return message. The result, a field with the name `delta`,  is the displacement to the starting position.

To see the feedback of this goal, add `--feedback` to the `ros2 action send_goal` command

```
ros2 action send_goal /turtle1/rotate_absolute turtlesim_msgs/action/RotateAbsolute "{theta: -1.57}" --feedback
```

**ros2 action echo**

To see the data communication between an action client and an action server

```
ros2 action echo <action_name> <optional arguments/action_type>
```

`ros2 action echo` depends on action **introspection** of an action client and server, that is disabled by default. To enable it, users must call `configure_introspection` after creating an action client or server.



### Using `rqt_console` to view logs

`rqt_console` can help you closely examine the log messages from the system.

```
ros2 run rqt_console rqt_console
```

**Logger Level**

`Fatal` messages indicate the system is going to terminate to try to protect itself from detriment.

`Error` messages indicate significant issues that won’t necessarily damage the system, but are preventing it from functioning properly.

`Warn` messages indicate unexpected activity or non-ideal results that might represent a deeper issue, but don’t harm functionality outright.

`Info` messages indicate event and status updates that serve as a visual verification that the system is running as expected.

`Debug` messages detail the entire step-by-step process of the system execution.

**Set the default logger level**

Set the default logger level when you first run the `/turtlesim` node using remapping. 

```
ros2 run turtlesim turtlesim_node --ros-args --log-level WARN
```

Now you won’t see the `Info` level messages that came up in the console last time you started `turtlesim`. That’s because `Info` messages are lower priority than the new default severity, `Warn`.



### Launching nodes

Launch files allow you to start up and configure a number of executables containing ROS 2 nodes simultaneously.

**Running a launch file**

Open a new terminal and run:

```
ros2 launch turtlesim multisim.launch.py
```

This command will run the following launch file:

```python
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            namespace='turtlesim1', package='turtlesim',
            executable='turtlesim_node', output='screen'),
        launch_ros.actions.Node(
            namespace='turtlesim2', package='turtlesim',
            executable='turtlesim_node', output='screen'),
    ])
```

Now that these nodes are running. Open up additional terminals and you can control them like any other ROS 2 nodes.



### Recording and playing back data

#### Managing topic data

Open a new terminal and run:

```
ros2 run turtlesim turtlesim_node
```

Open another terminal and run:

```
ros2 run turtlesim turtle_teleop_key
```

Make a new **directory** to store our saved recordings:

```
mkdir bag_files
cd bag_files
```

**Record  a single topic**

`ros2 bag` can record data from messages published to topics. Move into the `bag_files` directory. 

```
ros2 bag record --topics <topic_name>
```

```
ros2 bag record --topics /turtle1/cmd_vel
```

Press Ctrl+C to stop recording.

The data will be accumulated in a new **bag directory** with a **name** in the pattern of `rosbag2_year_month_day-hour_minute_second`. This directory will contain a `metadata.yaml` along with the bag file in the recorded format.

**Record multiple topics**

The `-o` or  `--output` option allows you to choose a unique name for your bag directory. The `subset` is the **bag directory name**.

```
ros2 bag record -o subset --topics /turtle1/cmd_vel /turtle1/pose
```

Record all topics

```
ros2 bag record -o all_topics_bag *
```

**Split recording into multiple files**

`-d <max_bag_duration>` ensures that each file only lasts `<max_bag_duration>` seconds before it starts writing to a new file, or `-b <max_bag_size>` ensures that each file does not exceed `<max_bag_size>` bytes in file size.

```
ros2 bag record -o subset_split -d 5 --topics /turtle1/cmd_vel /turtle1/pose
```

**Inspect topic data**

See details about your recording.

```
ros2 bag info <bag_name>
```

**Play a single bag**

Before replaying the bag, enter Ctrl+C in the terminal where the teleop is running.

```
ros2 bag play subset
```

**Play multiple bags**
As an example, we can record `/turtle1/cmd_vel` and `/turtle1/pose` each to their own bag.

Create two terminal instances. In the first one, run the following:

```
ros2 bag record -o subset_cmd_vel --topics /turtle1/cmd_vel
```

In the second terminal, run this:

```
ros2 bag record -o subset_pose --topics /turtle1/pose
```

To have these two recordings play in parallel with correct timing, call `ros2 bag play` with `-i <bag_name>` for each bag you want to include.

```
ros2 bag play -i subset_cmd_vel -i subset_pose
```

#### Managing service data

To record service data between service client and server, `Service Introspection` must be enabled on the node.

**Record services**

To record specific services:

```
ros2 bag record --service <service_names>
```

To record all services:

```
ros2 bag record --all-services
```

**Inspect service data**

```
ros2 bag info <bag_file_name>
```

**Play service bag**

```
ros2 bag play --publish-service-requests <bag_file_name>
```

#### Managing action data

To record action data between action client and server, `Action Introspection` must be enabled on the nodes.

Let’s start `fibonacci_action_client` and `fibonacci_action_server` nodes and enable `Action Introspection`.

Open a new terminal and run `fibonacci_action_server`, enabling `Action Introspection`:

```
ros2 run action_tutorials_py fibonacci_action_server --ros-args -p action_server_configure_introspection:=contents
```

Open another terminal and run `fibonacci_action_client`, enabling `Action Introspection`:

```
ros2 run action_tutorials_cpp fibonacci_action_client --ros-args -p action_client_configure_introspection:=contents
```

**Check action availability**

`ros2 bag` can only record data from available actions. Open a new terminal

```
ros2 action list
/fibonacci
```

```
ros2 action echo --flow-style /fibonacci
interface: STATUS_TOPIC
status_list: [{goal_info: {goal_id: {uuid: [28, 80, 233, 191, 140, 64, 198, 170, 52, 13, 52, 97, 17, 123, 62, 193]}, stamp: {sec: 1772676332, nanosec: 148579520}}, status: 4}]
---
```

**Record actions**

To record specific actions:

```
ros2 bag record --action <action_names>
```

To record all actions:

```
ros2 bag record --all-actions
```

```
ros2 bag record --action /fibonacci
```

Now `ros2 bag` is recording the action data for the `/fibonacci` action: goal, result, and feedback.

The data will be accumulated in a new bag directory with a name in the pattern of `rosbag2_year_month_day-hour_minute_second`. This directory will contain a `metadata.yaml` along with the bag file in the recorded format.

**Inspect action data**

```
ros2 bag info <bag_file_name>
```

**Play action bag**

Before replaying the bag file, enter Ctrl+C in the terminal where `fibonacci_action_client` is running.

```
ros2 bag play --send-actions-as-client <bag_file_name>
```

