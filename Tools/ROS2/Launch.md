# Launch

[toc]

### Import

**launch module**

- `launch.LaunchDescription`: The main container that describes the contents of a launch file.
- `launch.actions`
  - `IncludeLaunchDescription`: Include and execute another launch file.
  - `DeclareLaunchArgument`: Declare a launch argument that can be passed via the command line.
  - `EmitEvent`: Emit/trigger an event.
  - `ExecuteProcess`: Run a system process/command.
  - `LogInfo`: Log an informational message.
  - `RegisterEventHandler`: Register an event handler.
  - `TimerAction`: Execute an action after a delay or at regular intervals.
  - `GroupAction`: Group actions together to apply conditions or namespaces to them as a whole.
- `launch.conditions`
  - `IfCondition`: Decide whether to execute a group of actions based on a conditional expression.
- `launch.event_handlers`
  - `OnProcessStart`: Triggered when a process starts.
  - `OnProcessIO`: Triggered upon receiving process stdout/stderr.
  - `OnExecutionComplete`: Triggered when an action's execution completes.
  - `OnProcessExit`: Triggered when a process exits.
  - `OnShutdown`: Triggered when the launch system is shutting down.
- `launch.events`
  - `Shutdown`: An event to request the shutdown of the entire launch system.
- `launch.substitutions`
  - `PathJoinSubstitution`: Join path strings.
  - `EnvironmentVariable`: Get the value of an environment variable.
  - `FindExecutable`: Find an executable in the system PATH.
  - `LaunchConfiguration`: Get the value of a launch argument declared by `DeclareLaunchArgument`.
  - `LocalSubstitution`: Perform local string substitution/evaluation at action execution time.
  - `PythonExpression`: Evaluate a Python expression and return the result.

**launch_ros module (ROS 2 Extensions)**

- `launch_ros.actions`
  - `Node`: Launch a ROS 2 node.
  - `PushROSNamespace`: Set or modify the ROS namespace for subsequent nodes.
- `launch_ros.substitutions`
  - `FindPackageShare`: Find the share directory path of a specified ROS 2 package.



### Using XML, YAML, and Python for ROS 2 Launch Files

**Launching**

You can either create a new package and use

```
ros2 launch <package_name> <launch_file_name>
```

or run the file directly by specifying the path to the launch file

```
ros2 launch <path_to_launch_file>
```

**Set arguments**

To set the arguments that are passed to the launch file, use `key:=value` syntax.

```
ros2 launch <package_name> <launch_file_name> background_r:=255
```

or

```
ros2 launch <path_to_launch_file> background_r:=255
```

**Control the turtles**

Starts a `teleop_key` node and remap its namespace to `/turtlesim1` to control the turtle in that namespace.

```
ros2 run turtlesim turtle_teleop_key --ros-args --remap __ns:=/turtlesim1
```



### Create a launch file

Create a new directory to store your launch files:

```
mkdir launch
```

**Write the launch file**

`launch/turtlesim_mimic_launch.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<launch>
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" namespace="turtlesim1" args="--ros-args --log-level info" />
  <node pkg="turtlesim" exec="turtlesim_node" name="sim" namespace="turtlesim2" ros_args="--log-level warn" />
  <node pkg="turtlesim" exec="mimic" name="mimic">
    <remap from="/input/pose" to="/turtlesim1/turtle1/pose" />
    <remap from="/output/cmd_vel" to="/turtlesim2/turtle1/cmd_vel" />
  </node>
</launch>
```

`launch/turtlesim_mimic_launch.yaml`

```yaml
%YAML 1.2
---
launch:
  - node:
      pkg: "turtlesim"
      exec: "turtlesim_node"
      name: "sim"
      namespace: "turtlesim1"
      args: "--ros-args --log-level info"

  - node:
      pkg: "turtlesim"
      exec: "turtlesim_node"
      name: "sim"
      namespace: "turtlesim2"
      ros_args: "--log-level warn"

  - node:
      pkg: "turtlesim"
      exec: "mimic"
      name: "mimic"
      remap:
        - from: "/input/pose"
          to: "/turtlesim1/turtle1/pose"
        - from: "/output/cmd_vel"
          to: "/turtlesim2/turtle1/cmd_vel"
```

`launch/turtlesim_mimic_launch.py`

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim',
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim',
            ros_arguments=['--log-level', 'warn']
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ])
```

**Examine the launch file**

All of the launch files above are launching a system of three nodes from the `turtlesim` package. The goal of the system is to launch two turtlesim windows, and have one turtle mimic the movements of the other.

The first two actions launch the two turtlesim windows with different argument passing approaches.

+ The first node uses `args` to pass arguments directly to the executable, requiring the `--ros-args` flag for ROS-specific arguments.
+ The second node uses `ros_args` (`ros_arguments` in Python), designed specifically for ROS arguments.
+ Use `args` when mixing ROS and non-ROS arguments (e.g., `my_custom_arg --ros-args --log-level info`), or `ros_args` for cleaner syntax with only ROS arguments like remappings, parameters, or log levels.

The final action launches the mimic node with the remaps.

+ The final node is also from the `turtlesim` package, but a different executable: `mimic`.
+ `mimic`’s `/input/pose` topic is remapped to `/turtlesim1/turtle1/pose` and it’s `/output/cmd_vel` topic to `/turtlesim2/turtle1/cmd_vel`.
+ `mimic` will subscribe to `/turtlesim1/sim`’s pose topic and republish it for `/turtlesim2/sim`’s velocity command topic to subscribe to.

 **ros2 launch**

To run the launch file:

```
cd launch
ros2 launch turtlesim_mimic_launch.xml
```

```
cd launch
ros2 launch turtlesim_mimic_launch.yaml
```

```
cd launch
ros2 launch turtlesim_mimic_launch.py
```

To see the system in action, open a new terminal and run the `ros2 topic pub` command on the `/turtlesim1/turtle1/cmd_vel` topic to get the first turtle moving:

```
ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"
```

The second turtle will mimic the movements of the it.

**Note**

For packages with launch files, add an `exec_depend` dependency on the `ros2launch` package in package’s `package.xml`:

```xml
<exec_depend>ros2launch</exec_depend>
```

This helps make sure that the `ros2 launch` command is available after building your package. It also ensures that all launch file formats are recognized.

**Introspect the system with rqt_graph**

While the system is still running, open a new terminal and run `rqt_graph` to get a better idea of the relationship between the nodes in your launch file.

```
ros2 run rqt_graph rqt_graph
```

![ab9c5259-917d-4485-88b7-71a4a96021aa](/home/yunxiu/Desktop/ROS2_study/Pictures/ab9c5259-917d-4485-88b7-71a4a96021aa.png)

A hidden node (the `ros2 topic pub`) is publishing data to the `/turtlesim1/turtle1/cmd_vel` topic on the left, which the `/turtlesim1/sim` node is subscribed to.



### Integrating launch files into ROS 2 packages

Create a workspace for the package to live in:

```
mkdir -p launch_ws/src
cd launch_ws/src
```

```
ros2 pkg create --build-type ament_python --license Apache-2.0 py_launch_example
```

**Create the structure to hold launch files**

By convention, all launch files for a package are stored in the `launch` directory inside of the package. Make sure to create a `launch` directory at the top-level of the package you created above.

```
src/
  py_launch_example/
    launch/
    package.xml
    py_launch_example/
    resource/
    setup.cfg
    setup.py
    test/
```

Inform Python’s setup tools of the presence of launch files. Open the `setup.py` file, add the necessary `import` statements at the top, and include the launch files into the `data_files` parameter of `setup`

```python
import os
from glob import glob
# Other imports ...

package_name = 'py_launch_example'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ]
)
```

Install all files from the local `launch/` directory into the system's `share/<package_name>/launch/` directory, enabling ROS 2 to locate these launch files during runtime.

**Write the launch file**

Inside your `launch` directory, create a new launch file called `my_script_launch.py`. `_launch.py` is recommended, but not required, as the file suffix for Python launch files. However, the launch file name needs to end with `launch.py` to be recognized and auto-completed by `ros2 launch`.

Your launch file should define the `generate_launch_description()` function which returns a `launch.LaunchDescription()` to be used by the `ros2 launch` verb.

```python
import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker'),
    ])
```

**Build and run the launch file**

Go to the top-level of the workspace, and build it:

```
colcon build
```

Source the workspace:

```
. install/setup.bash
```

Run the launch file:

```
ros2 launch py_launch_example my_script_launch.py
```

```
[INFO] [launch]: All log files can be found below /home/yunxiu/.ros/log/2026-03-12-10-17-48-998887-yunxiu-OMEN-by-HP-Gaming-Laptop-16-xf0xxx-8316
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [8319]
[talker-1] [INFO] [1773281870.069526800] [talker]: Publishing: 'Hello World: 1'
[talker-1] [INFO] [1773281871.069480131] [talker]: Publishing: 'Hello World: 2'
[talker-1] [INFO] [1773281872.069518117] [talker]: Publishing: 'Hello World: 3'
...
```



### Using substitutions

**Create and setup package**

Create a new package of build_type `ament_python`:

```
ros2 pkg create --build-type ament_python --license Apache-2.0 launch_tutorial
```

Inside of that package, create a directory called `launch`:

```
mkdir launch_tutorial/launch
```

Finally, make sure to install the launch files:

Add in following changes to the `setup.py` of the package:

```python
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'launch_tutorial'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ]
)
```

#### Parent launch file

Create the file `launch/example_main_launch.py`

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('launch_tutorial'),
                'launch',
                'example_substitutions_launch.py'
            ]),
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': colors['background_r'],
            }.items()
        )
    ])
```

The `FindPackageShare` substitution is used to find the path to the `launch_tutorial` package. The `PathJoinSubstitution` substitution is then used to join the path to that package path with the `example_substitutions_launch.py` file name.

```python
            PathJoinSubstitution([
                FindPackageShare('launch_tutorial'),
                'launch',
                'example_substitutions_launch.py'
            ]),
```

The `launch_arguments` dictionary with `turtlesim_ns` and `use_provided_red` arguments is passed to the `IncludeLaunchDescription` action.

```python
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': colors['background_r'],
            }.items()
```

+ In ROS 2 launch files, **arguments** are used to pass configurable parameters from the external console or other launch files during runtime. 

+ While **variables** are used internally within the launch file to store and reuse values, simplifying maintenance and avoiding repetition.

**Tip**: A list of substitutions or strings gets concatenated into a single string.

For example, with `PathJoinSubstitution`, if the file name prefix depended on a launch argument named `file`, a list of substitutions and strings could be used to create the file name:

```python
# Make sure to import LaunchConfiguration:
# from launch.substitutions import LaunchConfiguration

PathJoinSubstitution([
    FindPackageShare('launch_tutorial'),
    'launch',
    [LaunchConfiguration('file', default='example_substitutions'), '_launch', '.py']
])
```

In this case, by default, the last path component provided to `PathJoinSubstitution` would resolve to `example_substitutions_launch.py` and would then be joined with the other path components.

#### Substitutions example launch file

Create the file `launch/example_substitutions_launch.py`

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    return LaunchDescription([
        DeclareLaunchArgument(
            'turtlesim_ns',
            default_value='turtlesim1'
        ),
        DeclareLaunchArgument(
            'use_provided_red',
            default_value='False'
        ),
        DeclareLaunchArgument(
            'new_background_r',
            default_value='200'
        ),
        Node(
            package='turtlesim',
            namespace=turtlesim_ns,
            executable='turtlesim_node',
            name='sim'
        ),
        ExecuteProcess(
            cmd=[[
                'ros2 service call ',
                turtlesim_ns,
                '/spawn ',
                'turtlesim_msgs/srv/Spawn ',
                '"{x: 2, y: 2, theta: 0.2}"'
            ]],
            shell=True
        ),
        ExecuteProcess(
            cmd=[[
                'ros2 param set ',
                turtlesim_ns,
                '/sim background_r ',
                '120'
            ]],
            shell=True
        ),
        TimerAction(
            period=2.0,
            actions=[
                ExecuteProcess(
                    condition=IfCondition(
                        PythonExpression([
                            new_background_r,
                            ' == 200',
                            ' and ',
                            use_provided_red
                        ])
                    ),
                    cmd=[[
                        'ros2 param set ',
                        turtlesim_ns,
                        '/sim background_r ',
                        new_background_r
                    ]],
                    shell=True
                ),
            ],
        )
    ])
```

The `turtlesim_ns`, `use_provided_red`, and `new_background_r` launch configurations are defined. They are used to represent values of launch arguments in the above variables and to pass them to required actions. These `LaunchConfiguration` substitutions allow us to acquire the value of the launch argument in any part of the launch description.

`DeclareLaunchArgument` is used to define the launch argument that can be passed from the above launch file or from the console.

```python
        DeclareLaunchArgument(
            'turtlesim_ns',
            default_value='turtlesim1'
        ),
        DeclareLaunchArgument(
            'use_provided_red',
            default_value='False'
        ),
        DeclareLaunchArgument(
            'new_background_r',
            default_value='200'
        ),
```

The `turtlesim_node` node with the `namespace` set to `turtlesim_ns` `LaunchConfiguration` substitution is defined.

```python
        Node(
            package='turtlesim',
            namespace=turtlesim_ns,
            executable='turtlesim_node',
            name='sim'
        ),
```

`ExecuteProcess`  is defined with the corresponding `cmd` argument to call the spawn service of the turtlesim node. `LaunchConfiguration` substitution is used to provide the value of the `turtlesim_ns` launch argument in the command string.

```python
        ExecuteProcess(
            cmd=[[
                'ros2 service call ',
                turtlesim_ns,
                '/spawn ',
                'turtlesim_msgs/srv/Spawn ',
                '"{x: 2, y: 2, theta: 0.2}"'
            ]],
            shell=True
        ),
```

The next action is only executed if the provided `new_background_r` argument equals `200` and the `use_provided_red` launch argument is set to `True`. The evaluation inside the `IfCondition` is done using the `PythonExpression` substitution.

```python
        TimerAction(
            period=2.0,
            actions=[
                ExecuteProcess(
                    condition=IfCondition(
                        PythonExpression([
                            new_background_r,
                            ' == 200',
                            ' and ',
                            use_provided_red
                        ])
                    ),
                    cmd=[[
                        'ros2 param set ',
                        turtlesim_ns,
                        '/sim background_r ',
                        new_background_r
                    ]],
                    shell=True
                ),
            ],
        )
```

**Build the package**

Go to the root of the workspace, and build the package:

```
colcon build --packages-select launch_tutorial
```

Source the workspace:

```
. install/setup.bash
```

**Launch exmple**

```
ros2 launch launch_tutorial example_main_launch.py
```

+ Start a turtlesim node with a blue background

+ Spawn the second turtle

+ Change the color to purple

+ Change the color to pink after two seconds if the provided `background_r` argument is `200` and `use_provided_red` argument is `True`

#### Modify launch arguments

If you want to change the provided launch arguments, you can either update them in `launch_arguments` dictionary in the `example_main_launch.py` or launch the `example_substitutions_launch.py` with preferred arguments.

```
ros2 launch launch_tutorial example_substitutions_launch.py --show-args
```

This will show the arguments that may be given to the launch file and their default values.

```
Arguments (pass arguments as '<name>:=<value>'):

    'turtlesim_ns':
        no description given
        (default: 'turtlesim1')

    'use_provided_red':
        no description given
        (default: 'False')

    'new_background_r':
        no description given
        (default: '200')
```

Pass the desired arguments to the launch file:

```
ros2 launch launch_tutorial example_substitutions_launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```



### Using event handlers

+ In ROS 2 launch, an **event** is a notification signaling a change in the state of the system or its processes，like a node starting or exiting.
+ An **event handler** is a callback function registered with the launch system to monitor, report, and react to specific events, enabling  dynamic control and complex automation of the launch process.

**Event handler example launch file**

Create a new file called `example_event_handlers_launch.py` file in the `launch` folder of the `launch_tutorial` package.

```python
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    EmitEvent,
    ExecuteProcess,
    LogInfo,
    RegisterEventHandler,
    TimerAction
)
from launch.conditions import IfCondition
from launch.event_handlers import (
    OnExecutionComplete,
    OnProcessExit,
    OnProcessIO,
    OnProcessStart,
    OnShutdown
)
from launch.events import Shutdown
from launch.substitutions import (
    EnvironmentVariable,
    FindExecutable,
    LaunchConfiguration,
    LocalSubstitution,
    PythonExpression
)
from launch_ros.actions import Node


def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        'turtlesim_ns',
        default_value='turtlesim1'
    )
    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False'
    )
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )

    turtlesim_node = Node(
        package='turtlesim',
        namespace=turtlesim_ns,
        executable='turtlesim_node',
        name='sim'
    )
    spawn_turtle = ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            ' service call ',
            turtlesim_ns,
            '/spawn ',
            'turtlesim_msgs/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
    )
    change_background_r = ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            ' param set ',
            turtlesim_ns,
            '/sim background_r ',
            '120'
        ]],
        shell=True
    )
    change_background_r_conditioned = ExecuteProcess(
        condition=IfCondition(
            PythonExpression([
                new_background_r,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[[
            FindExecutable(name='ros2'),
            ' param set ',
            turtlesim_ns,
            '/sim background_r ',
            new_background_r
        ]],
        shell=True
    )

    return LaunchDescription([
        turtlesim_ns_launch_arg,
        use_provided_red_launch_arg,
        new_background_r_launch_arg,
        turtlesim_node,
        RegisterEventHandler(
            OnProcessStart(
                target_action=turtlesim_node,
                on_start=[
                    LogInfo(msg='Turtlesim started, spawning turtle'),
                    spawn_turtle
                ]
            )
        ),
        RegisterEventHandler(
            OnProcessIO(
                target_action=spawn_turtle,
                on_stdout=lambda event: LogInfo(
                    msg='Spawn request says "{}"'.format(
                        event.text.decode().strip())
                )
            )
        ),
        RegisterEventHandler(
            OnExecutionComplete(
                target_action=spawn_turtle,
                on_completion=[
                    LogInfo(msg='Spawn finished'),
                    change_background_r,
                    TimerAction(
                        period=2.0,
                        actions=[change_background_r_conditioned],
                    )
                ]
            )
        ),
        RegisterEventHandler(
            OnProcessExit(
                target_action=turtlesim_node,
                on_exit=[
                    LogInfo(msg=(EnvironmentVariable(name='USER'),
                            ' closed the turtlesim window')),
                    EmitEvent(event=Shutdown(
                        reason='Window closed'))
                ]
            )
        ),
        RegisterEventHandler(
            OnShutdown(
                on_shutdown=[LogInfo(
                    msg=['Launch was asked to shutdown: ', LocalSubstitution('event.reason')]
                )]
            )
        ),
    ])
```

`RegisterEventHandler` actions for the `OnProcessStart`, `OnProcessIO`, `OnExecutionComplete`, `OnProcessExit`, and `OnShutdown` events were defined in the launch description.

The `OnProcessStart` event handler is used to register a callback function that is executed when the turtlesim node starts. It logs a message to the console and executes the `spawn_turtle` action when the turtlesim node starts.

```python
        RegisterEventHandler(
            OnProcessStart(
                target_action=turtlesim_node,
                on_start=[
                    LogInfo(msg='Turtlesim started, spawning turtle'),
                    spawn_turtle
                ]
            )
        ),
```

The `OnProcessIO` event handler is used to register a callback function that is executed when the `spawn_turtle` action writes to its standard output. It logs the result of the spawn request.

```python
        RegisterEventHandler(
            OnProcessIO(
                target_action=spawn_turtle,
                on_stdout=lambda event: LogInfo(
                    msg='Spawn request says "{}"'.format(
                        event.text.decode().strip())
                )
            )
        ),
```

The `OnExecutionComplete` event handler is used to register a callback function that is executed when the `spawn_turtle` action completes. It logs a message to the console and executes the `change_background_r` and `change_background_r_conditioned` actions when the spawn action completes.

```python
        RegisterEventHandler(
            OnExecutionComplete(
                target_action=spawn_turtle,
                on_completion=[
                    LogInfo(msg='Spawn finished'),
                    change_background_r,
                    TimerAction(
                        period=2.0,
                        actions=[change_background_r_conditioned],
                    )
                ]
            )
        ),
```

The `OnProcessExit` event handler is used to register a callback function that is executed when the turtlesim node exits. It logs a message to the console and executes the `EmitEvent` action to emit a `Shutdown` event when the turtlesim node exits. It means that the launch process will shutdown when the turtlesim window is closed.

```python
        RegisterEventHandler(
            OnProcessExit(
                target_action=turtlesim_node,
                on_exit=[
                    LogInfo(msg=(EnvironmentVariable(name='USER'),
                            ' closed the turtlesim window')),
                    EmitEvent(event=Shutdown(
                        reason='Window closed'))
                ]
            )
        ),
```

Finally, the `OnShutdown` event handler is used to register a callback function that is executed when the launch file is asked to shutdown. It logs a message to the console why the launch file is asked to shutdown. It logs the message with a reason for shutdown like the closure of turtlesim window or ctrl-c signal made by the user.

```python
        RegisterEventHandler(
            OnShutdown(
                on_shutdown=[LogInfo(
                    msg=['Launch was asked to shutdown: ', LocalSubstitution('event.reason')]
                )]
            )
        ),
```

**Build the package**

Go to the root of the workspace, and build the package:

```
colcon build --packages-select launch_tutorial
```

Source the workspace:

```
. install/setup.bash
```

**Launch exmple**

```
ros2 launch launch_tutorial example_event_handlers_launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```

+ Start a turtlesim node with a blue background
+ Spawn the second turtle
+ Change the color to purple
+ Change the color to pink after two seconds if the provided `background_r` argument is `200` and `use_provided_red` argument is `True`
+ Shutdown the launch file when the turtlesim window is closed

log messages to the console when:

+ The turtlesim node starts
+ The spawn action is executed
+ The `change_background_r` action is executed
+ The `change_background_r_conditioned` action is executed
+ The turtlesim node exits
+ The launch process is asked to shutdown.



### Managing large projects

In large robot systems, many interconnected nodes each require numerous parameters. ROS 2 launch files allow us to start all nodes and set corresponding parameters in one place.

#### Top-level organization

The key to reusable ROS 2 launch files is a modular design. By clustering related components into separate launch files and using a top-level launch file for specific configurations, you can easily switch between identical robots or between simulation and real hardware with minimal or no changes to the launch files themselves.

`launch/launch_turtlesim_launch.py` file:

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    launch_dir = PathJoinSubstitution([FindPackageShare('launch_tutorial'), 'launch'])
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_world_1_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'broadcaster_listener_launch.py']),
            launch_arguments={'target_frame': 'carrot1'}.items()
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'mimic_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'fixed_broadcaster_launch.py'])
        ),
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'turtlesim_rviz_launch.py'])
        ),
    ])
```

**Note**: Design Tip: Top-level launch files should be short, consist of includes to other files corresponding to subcomponents of the application, and commonly changed parameters.

**Note**: Be aware of the tradeoffs when deciding how many top-level launch files your application requires.

#### Parameters

**Setting parameters in the launch file**

`launch/turtlesim_world_1_launch.py` file:

This launch file starts the `turtlesim_node` node, which starts the turtlesim simulation, with simulation configuration parameters that are defined and passed to the nodes.

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('background_r', default_value='0'),
        DeclareLaunchArgument('background_g', default_value='84'),
        DeclareLaunchArgument('background_b', default_value='122'),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            parameters=[{
                'background_r': LaunchConfiguration('background_r'),
                'background_g': LaunchConfiguration('background_g'),
                'background_b': LaunchConfiguration('background_b'),
            }]
        ),
    ])
```

**Loading parameters from YAML file**

Create a configuration file, `turtlesim.yaml`, in the `/config` folder of our package `launch_tutorial`.

```YAML
/turtlesim2/sim:
   ros__parameters:
      background_b: 255
      background_g: 86
      background_r: 150
```

`launch/turtlesim_world_2_launch.py` file:

This launch file will launch the same `turtlesim_node` with parameter values that are loaded directly from the YAML configuration file.

```python
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            namespace='turtlesim2',
            name='sim',
            parameters=[PathJoinSubstitution([
                FindPackageShare('launch_tutorial'), 'config', 'turtlesim.yaml'])
            ],
        ),
    ])
```

Use a YAML configuration file to set parameters for the `turtlesim_node` launched from the launch file. Defining node parameters in YAML files make it easy to store and load a large number of configuration values. The YAML file is a node-specific parameter file, not a launch file, and such files can be conveniently exported from the current `ros2 param list`.

**Using wildcards in YAML files**

When multiple nodes with different names or namespaces require identical parameters, creating separate YAML files for each is inefficient. A  better solution is to use wildcard characters in parameter files, which  apply the same parameter values to multiple matching nodes by substituting for unknown parts of their names.

`launch/turtlesim_world_3_launch.py` file:

```python
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            namespace='turtlesim3',
            name='sim',
            parameters=[
                PathJoinSubstitution([
                    FindPackageShare('launch_tutorial'), 'config', 'turtlesim.yaml']),
            ],
        ),
    ])
```

Loading the same YAML file, however, will not affect the appearance of the third turtlesim world because its parameters are stored under another namespace.

```
/turtlesim3/sim:
   background_b
   background_g
   background_
```

Therefore, instead of creating a new configuration for the same node that use the same parameters, we can use wildcards syntax. `/**` will assign all the parameters in every node, despite differences in node names and namespaces.

```yaml
/**:
   ros__parameters:
      background_b: 255
      background_g: 86
      background_r: 150
```

Using that configuration file in our launch descriptions will assign `background_b`, `background_g`, and `background_r` parameters to specified values in `turtlesim3/sim` and `turtlesim2/sim` nodes.

#### Namespaces

We have defined the namespace for the turlesim world in the `turtlesim_world_2_launch` file. Unique namespaces allow the system to start two similar nodes without node name or topic name conflicts.

```python
namespace='turtlesim2',
```

If the launch file contains a large number of nodes, defining namespaces for each of them can become tedious. `PushROSNamespace` action can be used to define the global namespace for each launch file description. Every nested node will inherit that namespace automatically.

**Attention**: `PushROSNamespace` has to be the first action in the list for the following actions to apply the namespace.

+ Firstly, remove the `namespace='turtlesim2'` line from the `turtlesim_world_2_launch` file. 

+ Afterwards, update the `launch_turtlesim_launch` to change the include statement to the following:

```python
from launch.actions import GroupAction
from launch_ros.actions import PushROSNamespace

   ...
   GroupAction(
     actions=[
         PushROSNamespace('turtlesim2'),
         IncludeLaunchDescription(PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])),
      ]
   ),
```

As a result, each node in the `turtlesim_world_2_launch` launch description will have a `turtlesim2` namespace.

#### Reusing nodes

Create a `launch/broadcaster_listener_launch.py` file:

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.',
        ),
        Node(
            package='turtle_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ],
        ),
        Node(
            package='turtle_tf2_py',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ],
        ),
        Node(
            package='turtle_tf2_py',
            executable='turtle_tf2_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ],
        ),
    ])
```

In this file, we have declared the `target_frame` launch argument with a default value of `turtle1`. The default value means that the launch file can receive an argument to forward to its nodes, or in case the argument is not provided, it will pass the default value to its nodes.

Use the `turtle_tf2_broadcaster` node two times using different names and parameters during launch. This allows us to duplicate the same node without conflicts.

Start a `turtle_tf2_listener` node and set its `target_frame` parameter that we declared and acquired above.

#### Parameter overrides

```python
        IncludeLaunchDescription(
            PathJoinSubstitution([launch_dir, 'broadcaster_listener_launch.py']),
            launch_arguments={'target_frame': 'carrot1'}.items()
        ),
```

This syntax allows us to change the default goal target frame to `carrot1`. If you would like `turtle2` to follow `turtle1` instead of the `carrot1`, just remove the line that passes the `target_frame` argument. This will assign `target_frame` its default value, which is `turtle1`.

#### Remapping

Create a `launch/mimic_launch` file:

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtle2/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ])
```

This launch file will start the `mimic` node, which will give commands to one turtlesim to follow the other. The node is designed to receive the target pose on the topic `/input/pose`. In our case, we want to remap the target pose from `/turtle2/pose` topic. Finally, we remap the `/output/cmd_vel` topic to `/turtlesim2/turtle1/cmd_vel`. This way `turtle1` in our `turtlesim2` simulation world will follow `turtle2` in our initial turtlesim world.

#### Config files

Create a `launch/turtlesim_rviz_launch.py` file:

```python
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', PathJoinSubstitution([
                FindPackageShare('turtle_tf2_py'), 'rviz', 'turtle_rviz.rviz'])],
        ),
    ])
```

This launch file will start the RViz with the configuration file defined in the `turtle_tf2_py` package. This RViz configuration will set the world frame, enable TF visualization, and start RViz with a top-down view.

#### Environment variables

Environment variables are key-value pairs stored in the operating system that are accessible to all programs. 

Create a `launch/fixed_broadcaster_launch.py` file:

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'node_prefix',
            default_value=[EnvironmentVariable('USER'), '_'],
            description='prefix for node name'
        ),
        Node(
            package='turtle_tf2_py',
            executable='fixed_frame_tf2_broadcaster',
            name=[LaunchConfiguration('node_prefix'), 'fixed_broadcaster'],
        ),
    ])
```

`EnvironmentVariable('USER')` reads the environment variable named `USER` from the operating system and uses it as the prefix for the node name when starting the node.

This launch file shows the way environment variables can be called inside the launch files. Environment variables can be used to define or push namespaces for distinguishing nodes on different computers or robots.

**Note**: If you are running the launch file where the `USER` environment variable is not defined (like in the ROS docker file), then you can replace the environment variable reference above with any other word of your liking.

#### Update `setup.py`

```python
import os
from glob import glob
from setuptools import setup
...

data_files=[
      ...
      (os.path.join('share', package_name, 'launch'),
         glob('launch/*')),
      (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml')),
      (os.path.join('share', package_name, 'rviz'),
         glob('config/*.rviz')),
   ],
```

#### Build and run

Build the package and launch the top-level launch file:

```
cd ~/launch_ws
colcon build --packages-select launch_tutorial
. install/setup.bash
```

```
ros2 launch launch_tutorial launch_turtlesim_launch.py
```

The `turtle2` 's aim is to reach the `carrot1` frame which is five meters away on the x-axis relative to the `turtle1` frame.

The `turtlesim2/turtle1` is designed to mimic the behavior of the `turtle2`.

RViz will show all turtle frames relative to the `world` frame, whose origin is at the bottom-left corner.
