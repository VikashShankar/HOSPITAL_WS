import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Declare the launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('my_lidar_package'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'lidar.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

    # Create the robot_state_publisher node
    params_robot_state_publisher = {
        'robot_description': robot_description_config.toxml(),
        'use_sim_time': use_sim_time
    }
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params_robot_state_publisher]
    )

    # Create the rplidar_ros node
    params_rplidar_ros = {
        'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',
        'frame_id': 'laser_frame',
        'angle_compensate': True,
        'scan_mode': 'Standard'
    }
    node_rplidar_ros = Node(
        package='rplidar_ros',
        executable='rplidar_composition',
        output='screen',
        parameters=[params_rplidar_ros]
    )

    # Return the LaunchDescription
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),
        node_robot_state_publisher,
        node_rplidar_ros
    ])

if __name__ == '__main__':
    generate_launch_description()
