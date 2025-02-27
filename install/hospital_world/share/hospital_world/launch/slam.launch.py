from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to the robot URDF file
    urdf_file = os.path.join(get_package_share_directory('hospital_robot'), 'urdf', 'robot.urdf')

    # Path to the SLAM toolbox configuration file
    slam_config_file = os.path.join(get_package_share_directory('hospital_world'), 'config', 'mapper_params_online_async.yaml')

    return LaunchDescription([
        # Launch the robot state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),

        # Launch the SLAM toolbox with remapped topics
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',  # Asynchronous SLAM
            name='slam_toolbox',
            output='screen',
            parameters=[slam_config_file],
            remappings=[('/scan', '/scan'),  # Ensure this matches your laser scan topic
                        ('/odom', '/odom')]  # Ensure this matches your odometry topic
        ),

        # Static transform from base_link to lidar_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_lidar',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'lidar_link'],
            output='screen'
        ),

        # Static transform from base_link to caster_wheel
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_caster',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'caster_wheel'],
            output='screen'
        ),

        # Optionally, launch RViz for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('hospital_world'), 'rviz', 'slam_config.rviz')]
        ),
    ])
