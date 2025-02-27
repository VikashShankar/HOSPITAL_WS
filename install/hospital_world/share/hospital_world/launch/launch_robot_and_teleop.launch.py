from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo and spawn the robot
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
        Node(
            package='gazebo_ros', executable='spawn_entity.py',
            arguments=['-entity', 'my_robot', '-file', '/home/vikash/Hospital_ws/install/hospital_robot/share/hospital_robot/urdf/robot.urdf'],
            output='screen'),
        # Launch teleop_twist_keyboard node
        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='teleop_twist_keyboard',
            output='screen',
            remappings=[('/cmd_vel', '/cmd_vel')]
        ),
    ])
