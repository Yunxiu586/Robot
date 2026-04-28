# Intermediate

[toc]

### Manage dependencies with `rosdep`

`rosdep` is a **dependency management utility** that can work with packages and external libraries.

The `package.xml` is the file where `rosdep` finds the set of dependencies.

#### `package.xml` files

**`<depend>`**

These are dependencies that should be provided at both build time and run time for your package. For C++ packages, if in doubt, use this tag. Pure Python packages generally don’t have a build phase, so should never use this and should use `<exec_depend>` instead.

**`<build_depend>`**

If you only use a particular dependency for building your package, and not at execution time, you can use the `<build_depend>` tag.

**`<build_export_depend>`**

If you export a header that includes a header from a dependency, it will be needed by other packages that `<build_depend>` on yours. This mainly applies to headers and CMake configuration files. Library packages referenced by libraries you export should normally specify `<depend>`, because they are also needed at execution time.

**`<exec_depend>`**

This tag declares dependencies for shared libraries, executables,  Python modules, launch scripts and other files required when running  your package.

**`<test_depend>`**

This tag declares dependencies needed only by tests. Dependencies here should not be duplicated with keys specified by `<build_depend>`, `<exec_depend>`, or `<depend>`.

#### `rosdep`

`rosdep` will check for `package.xml` files in its path or for a specific package and find the rosdep keys  stored within. These keys are then cross-referenced against a **central index** to find the appropriate ROS package or software library in various package managers. Finally, once the packages are found, they are installed and ready to go.

`rosdep` works by retrieving the central index, `rosdistro` , on to your local machine so that it doesn’t have to access the network every time it runs. On Ubuntu, the configuration for it is stored in `/etc/ros/rosdep/sources.list.d/20-default.list`.

**Use the rosdep tool**

run `rosdep install` to install dependencies:

```
rosdep install --from-paths src -y --ignore-src
```

+ `--from-paths src` specifies the path to check for `package.xml` files to resolve keys for

+ `-y` means to default yes to all prompts from the package manager to install without prompts

+ `--ignore-src` means to ignore installing dependencies, even if a rosdep key exists, if the package itself is also in the workspace.



### Create an action

**Create an interface package**

Navigate into `ros2_ws/src`:

```
ros2 pkg create --build-type ament_cmake --license Apache-2.0 custom_action_interfaces
```

The package can **only be a CMake package**, but this doesn’t restrict in which type of packages you can use your actions.

**Define an action**

Keep `.msg`, `.srv`, and `.action`  files in separate packages from the nodes that use them, which makes it easier to reuse the interface definitions across different packages.

Create an `action` directory in package `custom_action_interfaces`

```
cd custom_action_interfaces
mkdir action
```

Within the `action` directory, create a file called `Fibonacci.action`.

```
int32 order			# Goal
---
int32[] sequence	# Result
---
int32[] sequence	# Feedback
```

**Build an action**

Add the following lines to `CMakeLists.txt` before the `ament_package()` line:

```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Fibonacci.action"
)
```

Add the required dependencies to our `package.xml`:

```xml
<buildtool_depend>rosidl_default_generators</buildtool_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

Navigate into `ros2_ws/src`. Build the package containing the `Fibonacci` action definition:

```
colcon build --packages-select custom_action_interfaces
```

Source the workspace:

```
source install/local_setup.bash
```

Now check that our action definition exists:

```
ros2 interface show custom_action_interfaces/action/Fibonacci
```



### Write an action server and client(Python)

**Python class `Fibonacci` generated from `Fibonacci.action` file:**

```
class: Fibonacci
├── class: Goal
│   ├── __init__(self, order:int=0)
│   └── attr： order
├── class: Result
│   ├── __init__(self, sequence=None)
│   └── attr: sequence # list[int]
└── class: Feedback
    ├── __init__(self, sequence=None)
    └── attr: sequence # list[int]
```

#### Write an action server

Open a new file in your home directory:

`fibonacci_action_server.py`

```python
import time

import rclpy
from rclpy.action import ActionServer
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from custom_action_interfaces.action import Fibonacci


# Define a class FibonacciActionServer that is a subclass of Node
class FibonacciActionServer(Node):

    # Define the class constructor method
    def __init__(self):
        # Initialization: call the Node constructor, name the node fibonacci_action_server
        super().__init__('fibonacci_action_server')
        # Instantiate a new action server object
        self._action_server = ActionServer(
            self,					# current node instance
            Fibonacci,				# action type
            'fibonacci',			# action name		
            self.execute_callback)	# callback function

    # Receive a goal_handle object
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        # Instantiate a feedback message object
        feedback_msg = Fibonacci.Feedback()
        # Initialize the sequence field
        feedback_msg.sequence = [0, 1]

        # Publish feedback （order-1） times
        for i in range(1, goal_handle.request.order):
            feedback_msg.sequence.append(
                feedback_msg.sequence[i] + feedback_msg.sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        # Indicate that the goal was successful
        goal_handle.succeed()

        # Instantiate a result message object
        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        return result


def main(args=None):
    try:
        with rclpy.init(args=args):
            fibonacci_action_server = FibonacciActionServer()

            rclpy.spin(fibonacci_action_server)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
```

`goal_handle` is an object (instance) of the `ServerGoalHandle` class.

`goal_handle.request` is an attribute of the `goal_handle` object and points to an instance of the `Fibonacci.Goal` class.

`goal_handle.request.order` is a chained attribute access expression.

```python
goal_handle.request.order
```

```
goal_handle => ServerGoalHandle
├── attr: request => Fibonacci.Goal
│	└── attr: order
├── method: publish_feedback(feedback_msg)
├── method: succeed()
└── method: abort()
```

Hierarchy diagram of `execute_callback`

```
execute_callback(self, goal_handle)
├── feedback_msg => Fibonacci.Feedback
├── feedback_msg.sequence
├── goal_handle => rclpy.action.server.ServerGoalHandle
│	├── for i in range(1, goal_handle.request.order)
│	│	└──goal_handle.request => Fibonacci.Goal
│	├── goal_handle.publish_feedback(feedback_msg)
│	└── goal_handle.succeed()
├── result => Fibonacci.Result
└── result.sequence = feedback_msg.sequence
```

**Comment-free code**:

```python
import time

import rclpy
from rclpy.action import ActionServer
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from custom_action_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(self, Fibonacci, 'fibonacci', self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.sequence.append(
                feedback_msg.sequence[i] + feedback_msg.sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        return result


def main(args=None):
    try:
        with rclpy.init(args=args):
            fibonacci_action_server = FibonacciActionServer()

            rclpy.spin(fibonacci_action_server)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
```

 Run our action server:

```
python3 fibonacci_action_server.py
```

In another terminal, use the command line interface to send a goal. The feedback is now published by using the command line tool with the `--feedback` option:

```
ros2 action send_goal --feedback fibonacci custom_action_interfaces/action/Fibonacci "{order: 5}"
```



#### Write an action client

`fibonacci_action_client.py`

```python
import rclpy
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from custom_action_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        # Wait for the action server to be available
        self._action_client.wait_for_server()

        # ActionClient.send_goal_async() method returns a future object to a goal handle
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg, 
            feedback_callback=self.feedback_callback)

        # Register a callback for when the future is complete
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        # Get a goal handle object
        goal_handle = future.result()
        # Check to see if the goal was rejected and return early
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        # Request the result
        self._get_result_future = goal_handle.get_result_async()
        # Registers a callback function to handle the result when it becomes available
        self._get_result_future.add_done_callback(self.get_result_callback)

    # callback function
    def get_result_callback(self, future):
        result = future.result().result
        # Log the result sequence
        self.get_logger().info('Result: {0}'.format(result.sequence))
        # Shutdown ROS 2 for a clean exit
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.sequence))


def main(args=None):
    try:
        with rclpy.init(args=args):
            action_client = FibonacciActionClient()

            action_client.send_goal(10)

            rclpy.spin(action_client)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
```

`Future` object acts as a placeholder and handle for the result of an asynchronous operation.

+ Enable Non-Blocking Calls: Methods like `send_goal_async()` return a `Future` immediately, allowing your program to continue without waiting for the operation to finish.

+ Manage Result Delivery: It holds the state of the async operation (pending, completed) and eventually contains the result or exception.

+ Facilitate Callback-Based Handling: You can attach a callback function (e.g., `goal_response_callback`) to the `Future` using `add_done_callback()`.

```
_action_client => ActionClient
└── method: send_goal_async()
	└── return: future => Future
        ├── method: add_done_callback()
        └── method: result()
            └── return: goal_handle => ClientGoalHandle
            	├── attr: accepted
               	├── attr: result => Fibonacci.Result
                │	└── attr： sequence
				└── method： get_result_async()
					└── return: future => Future
```

Hierarchy diagram of the `FibonacciActionClient` class methods:

```
send_goal(self, order)
├── goal_msg => Fibonacci.Goal
├── goal_msg.order = order
├── self._action_client.wait_for_server()
├── self._send_goal_future => Future = self._action_client.send_goal_async(
│		goal_msg, feedback_callback=self.feedback_callback)
│	└── feedback_callback(self, feedback_msg => FeedbackMessage)
│		└── feedback => Fibonacci.Feedback = feedback_msg.feedback
└── self._send_goal_future.add_done_callback(self.goal_response_callback)
    └── goal_response_callback(self, future)
        ├── goal_handle => rclpy.action.client.ClientGoalHandle = future.result()
        ├── if not goal_handle.accepted
        │   └── return
        ├── self._get_result_future => Future = goal_handle.get_result_async()
        └── self._get_result_future.add_done_callback(self.get_result_callback)
            └── get_result_callback(self, future)
                ├── result => Fibonacci.Result = future.result().result
                └── rclpy.shutdown()
```

**Comment-free code**:

```python
import rclpy
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from custom_action_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.sequence))


def main(args=None):
    try:
        with rclpy.init(args=args):
            action_client = FibonacciActionClient()

            action_client.send_goal(10)

            rclpy.spin(action_client)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
```

 Run the action server

```
python3 fibonacci_action_server.py
```

```
[INFO] [fibonacci_action_server]: Executing goal...
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

In another terminal, run the action client.

```
python3 fibonacci_action_client.py
```

```
[INFO] [fibonacci_action_client]: Goal accepted :)
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5, 8])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
[INFO] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
[INFO] [fibonacci_action_client]: Result: array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
```

The server's **goal** is to compute a Fibonacci sequence of length **order + 1**(2+order-1), i.e., from F_0 to F_(order-1).  And the server sends feedback **order-1** times in this process.

For example, an `action_client.send_goal(10)` requests the first 11 numbers.



### Publishing messages using YAML files

```
ros2 run turtlesim turtlesim_node
```

```
ros2 run turtlesim turtle_teleop_key
```

Use the `echo` verb to capture the message and save it in a YAML file `cmd_vel.yaml` using the output redirection operator `>`.

```
ros2 topic echo --once  turtle1/cmd_vel > cmd_vel.yaml
```

Use the arrows to move the turtle around. This creates a `cmd_vel.yaml` file with the following content in the directory the command was executed:

```yaml
linear:
    x: 1.0
    y: 0.0
    z: 0.0
angular:
    x: 0.0
    y: 0.0
    z: 0.0
---
```

To publish a message, utilize the `--yaml-file` option available with the `pub` verb of the `ros2 topic` command.

First, specify the target topic, `/cmd_vel`, followed by the message type `geometry_msgs/msg/Twist`.

 Lastly, specify the YAML file containing the message data. 

The following command will publish the message contained in the `YAML` file to the designated `topic` once.

```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist --yaml-file cmd_vel.yaml
```

```
publisher: beginning loop
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.0))
```

Publish more than once by adding more data to the YAML file.

```yaml
linear:
    x: 1.0
    y: 0.0
    z: 0.0
angular:
    x: 0.0
    y: 0.0
    z: 0.0
---
linear:
    x: 2.0
    y: 0.0
    z: 0.0
angular:
    x: 0.0
    y: 0.0
    z: 0.0
---
linear:
    x: 3.0
    y: 0.0
    z: 0.0
angular:
    x: 0.0
    y: 0.0
    z: 0.0
---
```

Publish three different messages to the `/cmd_vel` topic.

```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist --yaml-file cmd_vel.yaml
```

```
publisher: beginning loop
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.0))

publishing #2: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=2.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.0))

publishing #3: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=3.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.0))
```



### Monitoring for parameter changes (Python)

Navigate into `ros2_ws/src` and create the package.

```
ros2 pkg create --build-type ament_python --license Apache-2.0 python_parameter_event_handler --dependencies rclpy
```

Update `package.xlm`

```xml
<description>Python parameter events client tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

**Write the Python node**

Inside the `ros2_ws/src/python_parameter_event_handler/python_parameter_event_handler` directory, create a new file called `parameter_event_handler.py`

```python
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler


class SampleNodeWithParameters(Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        # Declare an integer parameter an_int_param, with a default value of 0
        self.declare_parameter('an_int_param', 0)

        # Create a ParameterEventHandler object to monitor changes to parameters
        self.handler = ParameterEventHandler(self)

        # Register a callback to monitor changes in the parameter
        # Return a callback handler(object) for the new callback
        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name="node_with_parameters",
            callback=self.callback,
        )

    # Use the callback method of the SampleNodeWithParameters class
    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")


def main():
    try:
        with rclpy.init():
            node = SampleNodeWithParameters()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```

It is very important to save the handle that is returned by `add_parameter_callback`; otherwise, the callback will not be properly registered.

**Add an entry point**

Open the `setup.py` file.

```python
maintainer='YourName',
maintainer_email='you@email.com',
description='Python parameter tutorial',
license='Apache-2.0',
```

```python
entry_points={
    'console_scripts': [
        'node_with_parameters = python_parameter_event_handler.parameter_event_handler:main',
    ],
},
```

**Build and run**

In the root of your workspace (`ros2_ws`),  run `rosdep` to check for missing dependencies before building.

```
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
```

Navigate back to the root of your workspace, `ros2_ws`, and build your new package:

```
colcon build --packages-select python_parameter_event_handler
```

Open a new terminal, navigate to `ros2_ws`, and source the setup files:

```
. install/setup.bash
```

Run the node:

```
ros2 run python_parameter_event_handler node_with_parameters
```

The node is now active and has a single parameter and will print a message whenever this parameter is updated. Open up another terminal and source the setup file and execute the following command:

```
ros2 param set node_with_parameters an_int_param 43
```

The terminal running the node will display a message:

```
[INFO] [1773225745.091377131] [node_with_parameters]: Received an update to parameter: an_int_param: 43
```

**Extensions**

**Monitor changes to another node's parameters**

To monitor parameter changes of the `a_double_param` parameter in the external node `parameter_blackboard`, update the `SampleNodeWithParameters` constructor to add the following code:

```python
def __init__(...):
    ...
    self.callback_handle2 = self.handler.add_parameter_callback(
        parameter_name="a_double_param",
        node_name="parameter_blackboard",
        callback=self.callback,
    )
```

The current node only declares the parameters it needs, but it can monitor parameter changes of other nodes via the `ParameterEventHandler`.

```
colcon build --packages-select python_parameter_event_handler
```

```
. install/setup.bash
```

First run the newly-built parameter_event_handler code:

```
ros2 run python_parameter_event_handler node_with_parameters
```

From another terminal (with ROS initialized), run the parameter_blackboard demo application:

```
ros2 run demo_nodes_cpp parameter_blackboard
```

From a third terminal (with ROS initialized), set a parameter on the parameter_blackboard node:

```
ros2 param set parameter_blackboard a_double_param 3.45
```

Upon executing this command, you should see output in the  parameter_event_handler window, indicating that the callback function  was invoked upon the parameter update:

```
[INFO] [1773226053.181959882] [node_with_parameters]: Received an update to parameter: a_double_param: 3.45
```

**Monitor all node parameters simultaneously**

Use `add_parameter_event_callback` to register a single callback that fires when any parameters of any nodes change. Update the `SampleNodeWithParameters` constructor to add the following code:

```python
def __init__(...):
    self.declare_parameter("another_double_param", 0.0)
    ...
    self.event_calback_handle = self.handler.add_parameter_event_callback(
        callback=self.event_callback,
    )
```

Declare a new double parameter `another_double_param` and add an event callback that will monitor both parameters.

```python
def event_callback(self, parameter_event):
    self.get_logger().info(f"Received parameter event from node {parameter_event.node}")

    for p in parameter_event.changed_parameters:
        self.get_logger().info(
            f"Inside event: {p.name} changed to: {rclpy.parameter.parameter_value_to_python(p.value)}"
        )
```

```
colcon build --packages-select python_parameter_event_handler
```

```
. install/setup.bash
```

First run the parameter_event_handler node

```
ros2 run python_parameter_event_handler node_with_parameters
```

From a new terminal (with ROS sourced), set the original int parameter:

```
ros2 param set node_with_parameters an_int_param 44
```

You should see both the single-parameter callback, as well as the event callback being fired:

```
[INFO] [1773226381.804174878] [node_with_parameters]: Received an update to parameter: an_int_param: 44
[INFO] [1773226381.804521237] [node_with_parameters]: Received parameter event from node /node_with_parameters
[INFO] [1773226381.804790632] [node_with_parameters]: Inside event: an_int_param changed to: 44
```

Set the new double parameter:

```
ros2 param set node_with_parameters another_double_param 4.4
```

Since no single-parameter callback was added via `add_parameter_callback` for the double parameter, we should see only the event callback fire:

```
[INFO] [1773226421.555087866] [node_with_parameters]: Received parameter event from node /node_with_parameters
[INFO] [1773226421.555357511] [node_with_parameters]: Inside event: another_double_param changed to: 4.4
```

**Complete comment-free code:**

```python
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler


class SampleNodeWithParameters(Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        self.declare_parameter('an_int_param', 0)
        self.declare_parameter("another_double_param", 0.0)

        self.handler = ParameterEventHandler(self)

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name="node_with_parameters",
            callback=self.callback,
        )
        
        self.callback_handle2 = self.handler.add_parameter_callback(
            parameter_name="a_double_param",
            node_name="parameter_blackboard",
            callback=self.callback,
        )
        
        self.event_calback_handle = self.handler.add_parameter_event_callback(
        callback=self.event_callback,
    )

    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")

    def event_callback(self, parameter_event):
        self.get_logger().info(f"Received parameter event from node {parameter_event.node}")

        for p in parameter_event.changed_parameters:
            self.get_logger().info(
                f"Inside event: {p.name} changed to: {rclpy.parameter.parameter_value_to_python(p.value)}"
            )
            
            
def main():
    try:
        with rclpy.init():
            node = SampleNodeWithParameters()
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
```



### Domain ID

ROS 2 uses **DDS** as its default communication middleware. Within DDS, the **Domain ID** is the primary mechanism for isolating different logical networks on the same physical network. 

Nodes sharing the same Domain ID can discover and communicate with each other, while nodes on different domains cannot. By default, all ROS 2 nodes use Domain ID 0. To prevent interference between separate groups of computers running ROS 2 on a shared network, a unique Domain ID should be configured for each group.

To just choose a safe number, simply choose a domain ID between 0 and 101, inclusive.



### Testing

#### Running tests in ROS 2 from command line

To compile and run the tests, run the `test` verb from `colcon` at the root of your workspace.

```
colcon test --ctest-args tests [package_selection_args]
```

Where `package_selection_args` are optional package selection arguments for `colcon` to limit which packages are built and run.

`colcon test` makes sure that the tests run with the right environment, have access to their dependencies, etc.

To see the results, simply run the `test-result` verb from `colcon`.

```
colcon test-result --all
```

To see the exact test cases which fail, use the `--verbose` flag:

```
colcon test-result --all --verbose
```

#### Writing basic tests with Python

`setup.py` must have a test dependency on `pytest` within the call to `setup(...)`:

```python
tests_require=['pytest'],
```

Test code needs to go in a folder named `tests` in the root of your package.

```
ros_package/
  ros_package/
      __init__.py
      fozzie.py
  package.xml
  setup.cfg
  setup.py
  tests/
      test_init.py
      test_copyright.py
      test_fozzie.py
```

You can write functions with the `test_` prefix and include whatever assert statements.

```python
def test_math():
    assert 2 + 2 == 5   # This should fail for most mathematical systems
```

You can also specify arguments to the `pytest` framework from the command line with the `--pytest-args` flag. For example, you can specify the name of the function to run with

```
colcon test --packages-select <name-of-pkg> --pytest-args -k name_of_the_test_function
```

To see the pytest output while running the tests, use these flags:

```
colcon test --event-handlers console_cohesion+
```

#### Writing basic integration tests with Python

Where **unit tests** focus on validating a very specific piece of  functionality, **integration tests** focus on validating the interaction  between pieces of code.

A key aspect of integration testing is to prevent nodes from different tests from communicating, even when run in parallel. This will be achieved here using a specific test runner that picks unique ROS domain IDs.

Integration tests can be part of any ROS package. Create one or more packages solely for integration testing, or add the tests to the package of which they test the  functionality. The tutorial creates a new package to test the existing `turtlesim` node.

```
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake test_turtlesim
cd test_turtlesim
mkdir -p test
cd test
touch test_integration.py
```

**Describe the test in the test launch file**

Integration tests in ROS 2 are typically launched using Python launch files, conventionally named following the pattern **`test/test_\*.py`**.

There are two common types of tests in integration testing: **active  tests**, which run while the nodes under test are running, and  **post-shutdown** tests, which are run after exiting the nodes.

Only two modules are specific to testing: the general-purpose `unittest`, and `launch_testing`.

`test_integration.py`:

```python
import os
import sys
import time
import unittest

import launch
import launch_ros
import launch_testing.actions
import rclpy
from turtlesim_msgs.msg import Pose
```

`generate_test_description` describes what to launch:

```python
def generate_test_description():
    return (
        launch.LaunchDescription(
            [
                # Nodes under test
                launch_ros.actions.Node(
                    package='turtlesim',
                    namespace='',
                    executable='turtlesim_node',
                    name='turtle1',
                ),
                # Launch tests 0.5 s later
                launch.actions.TimerAction(
                    period=0.5, actions=[launch_testing.actions.ReadyToTest()]),
            ]
        ), {},
    )
```

In more complex integration test setups, you will probably want to launch a system of several nodes, together with additional nodes that perform mocking or must otherwise interact with the nodes under test.

```python
# Active tests
class TestTurtleSim(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = rclpy.create_node('test_turtlesim')

    def tearDown(self):
        self.node.destroy_node()

    def test_publishes_pose(self, proc_output):
        """Check whether pose messages published"""
        msgs_rx = []
        sub = self.node.create_subscription(
            Pose, 'turtle1/pose',
            lambda msg: msgs_rx.append(msg), 100)
        try:
            # Listen to the pose topic for 10 s
            end_time = time.time() + 10
            while time.time() < end_time:
                # spin to get subscriber callback executed
                rclpy.spin_once(self.node, timeout_sec=1)
            # There should have been 100 messages received
            assert len(msgs_rx) > 100
        finally:
            self.node.destroy_subscription(sub)

    def test_logs_spawning(self, proc_output):
        """Check whether logging properly"""
        proc_output.assertWaitFor(
            'Spawning turtle [turtle1] at x=',
            timeout=5, stream='stderr')
```

The classes marked with the `launch_testing.post_shutdown_test` decorator are run after letting the nodes under test exit. A typical test here is whether the nodes exited cleanly, for which `launch_testing` provides the method `asserts.assertExitCodes`.

```python
# Post-shutdown tests
@launch_testing.post_shutdown_test()
class TestTurtleSimShutdown(unittest.TestCase):
    def test_exit_codes(self, proc_info):
        """Check if the processes exited normally."""
        launch_testing.asserts.assertExitCodes(proc_info)
```

**Register the test in the CMakeLists.txt**

Registering the test in the `CMakeLists.txt` fulfills two functions:

+ It integrates test in the `CTest` framework ROS 2 CMake-based packages rely on

+ It specifies how the test should be launched, in this case, with a unique domain id to ensure test isolation.

```cmake
if(BUILD_TESTING)
  # Integration tests
  find_package(ament_cmake_ros REQUIRED)
  find_package(launch_testing_ament_cmake REQUIRED)
  function(add_ros_isolated_launch_test path)
    set(RUNNER "${ament_cmake_ros_DIR}/run_test_isolated.py")
    add_launch_test("${path}" RUNNER "${RUNNER}" ${ARGN})
  endfunction()
  add_ros_isolated_launch_test(test/test_integration.py)
endif()
```

**Dependencies and packages organization**

Add the dependencies to your `package.xml`:

```xml
    <test_depend>ament_cmake_ros</test_depend>
    <test_depend>launch</test_depend>
    <test_depend>launch_ros</test_depend>
    <test_depend>launch_testing</test_depend>
    <test_depend>launch_testing_ament_cmake</test_depend>
    <test_depend>rclpy</test_depend>
    <test_depend>turtlesim</test_depend>
    <test_depend>turtlesim_msgs</test_depend>
```

After following the above steps, your package ought to look as follows:

```
CMakeLists.txt
package.xml
tests/
  test_integration.py
```

**Running test and report generation**

```
cd ~/ros2_ws
colcon build --packages-select test_turtlesim
colcon test --packages-select test_turtlesim
colcon test-result --verbose
```

