from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="hospital_hardware",
            executable="serial_node",
            name="serial_node",
            output="screen",
        ),
    ])


from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node for serial communication (or encoder control)
        Node(
            package="hospital_hardware",  # Name of your ROS 2 package
            executable="serial_node",     # Name of the executable (check setup.py)
            name="serial_node",           # Name of the node when running
            output="screen",              # Print output to the screen
        ),

        # Node for encoder feedback
        Node(
            package="hospital_hardware",  # Name of your ROS 2 package
            executable="encoder",    # Name of the executable (check setup.py)
            name="encoder",         # Name of the node when running
            output="screen",              # Print output to the screen
        ),
    ])
