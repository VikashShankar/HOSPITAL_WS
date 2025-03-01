








                                                                                Operating System: Ubuntu 22.04 LTS
                                                                                ROS Version: ROS 2
                                                                                Distributions: Humble Hawksbill
                                                                                Robot Type: Differential Drive Robot
                                                                                Simulation/Visualization Type: Gazebo, Rviz
                                                                                Tools Used: SLAM, NAV2
                                                                                Components Used: LiDAR, Base Link, Left Wheel, Right Wheel, Castor Wheel
                                                                                Plugins Used: Differential Drive Robot, LiDAR
                                                                                Implementation: Medicine Delivery in Hospital Ward








Information Assets:
Prerequisites: ros2 humble, gazebo, gazebo packages, rviz, teleop twist keyboard

mkdir hospital_ws
cd hospital_ws
colcon build
mkdir src
cd src
ros2 pkg create --build-type ament_python robot
ros2 pkg create --build-type ament_python hospital
mkdir ~/hospital_ws/src/robot/urdf
touch ~/hospital_ws/src/robot/urdf/robot.urdf
1.	Open robot.urdf  and add the code 11.1
2.	Go to setup.py of robot package and add the highlighted code
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', ['urdf/robot.urdf']),
    ],
3.	Go to package.xml and add the highlighted code
  <license>TODO: License declaration</license>
  <depend>rclpy</depend>
  <depend>sensor_msgs</depend>
  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
mkdir ~/hospital_ws/src/hospital/worlds
touch ~/hospital_ws/src/hospital/worlds/apollo_hospital.sdf
Open apollo_hospital.sdf and add the code 15.1
mkdir ~/hospital_ws/src/hospital/launch
touch ~/hospital_ws/src/hospital/launch/apollo_world.launch.py
4.	Open apollo_world.launch.py and add the code 18.1
5.	Go to setup.py of hospital package and add the highlighted code
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/apollo_world.launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/apollo_hospital.sdf']),
    ],

6.	In package.xml of hospital add the highlighted code
<license>TODO: License declaration</license>
  <buildtool_depend>ament_cmake</buildtool_depend>
  <depend>rclpy</depend>
  <depend>launch</depend>
  <depend>launch_ros</depend>
  <depend>gazebo_ros</depend>
  <depend>ros2_control</depend>
  <depend>ros2_controllers</depend>
  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>



TERMINAL 1:
cd ~/hospital_ws
colcon build
source install/setup.bash
ros2 launch hospital apollo_world.launch.py

TERMINAL 2:
1.	ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True

TERMINAL 3:
1.	ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True

TERMINAL 4:
1.	ros2 run rviz2 rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz

TERMINAL 4:
1.	ros2 run teleop_twist_keyboard teleop_twist_keyboard












SCRIPT

11.1	Code To Design Robot

<?xml version="1.0"?>
<robot name="hospital_robot">
  <!-- Define materials -->
  <material name="gray">
    <color rgba="0.5 0.5 0.5 1.0"/>
  </material>
  <material name="black">
    <color rgba="0 0 0 1"/>
  </material>

  <!-- Base link of the robot -->
  <link name="base_link">
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 0.1"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0.1"/>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
      <material name="gray"/>
    </visual>
    <collision>
      <origin xyz="0 0 0.1"/>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
    </collision>
  </link>

  <!-- Base footprint joint -->
  <joint name="base_footprint_joint" type="fixed">
    <parent link="base_link"/>
    <child link="base_footprint"/>
    <origin xyz="0 0 0.1" rpy="0 0 0"/>
  </joint>
  <link name="base_footprint"/>

  <!-- Left wheel link -->
  <link name="left_wheel">
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.001" ixy="0.0" ixz="0.0" iyy="0.001" iyz="0.0" izz="0.001"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
    </collision>
  </link>

  <!-- Right wheel link -->
  <link name="right_wheel">
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.001" ixy="0.0" ixz="0.0" iyy="0.001" iyz="0.0" izz="0.001"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
    </collision>
  </link>

  <!-- Caster wheel link -->
  <link name="caster_wheel">
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.0005" ixy="0.0" ixz="0.0" iyy="0.0005" iyz="0.0" izz="0.0005"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <origin xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
    </collision>
  </link>

  <!-- LiDAR sensor -->
  <link name="lidar_link">
    <visual>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.225" radius="0.1"/>
      </geometry>
    </collision>
  </link>

  <!-- LiDAR joint -->
  <joint name="lidar_joint" type="fixed">
    <parent link="base_link"/>
    <child link="lidar_link"/>
    <origin xyz="0.2 0 0.225" rpy="0 0 0"/>
  </joint>

  <!-- Left wheel joint -->
  <joint name="left_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="left_wheel"/>
    <origin xyz="-0.15 0.225 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <!-- Right wheel joint -->
  <joint name="right_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="right_wheel"/>
    <origin xyz="-0.15 -0.225 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <!-- Caster wheel joint -->
  <joint name="caster_wheel_joint" type="fixed">
    <parent link="base_link"/>
    <child link="caster_wheel"/>
    <origin xyz="0.2 0 -0.05" rpy="0 0 0"/>
  </joint>

  <!-- Gazebo plugin for differential drive -->
  <gazebo>
    <plugin name="gazebo_ros_diff_drive" filename="libgazebo_ros_diff_drive.so">
      <!-- Namespace and remapping -->
      <ros>
        <namespace>/</namespace>
        <remapping>cmd_vel:=/cmd_vel</remapping>
      </ros>

      <!-- Wheel info -->
      <left_joint>left_wheel_joint</left_joint>
      <right_joint>right_wheel_joint</right_joint>
      <wheel_separation>0.5</wheel_separation>
      <wheel_diameter>0.2</wheel_diameter>

      <!-- Limits -->
      <max_wheel_torque>200</max_wheel_torque>
      <max_wheel_acceleration>10.0</max_wheel_acceleration>

      <!-- Output -->
      <odometry_frame>odom</odometry_frame>
      <robot_base_frame>base_link</robot_base_frame>

      <!-- Publishing options -->
      <publish_odom>true</publish_odom>
      <publish_odom_tf>true</publish_odom_tf>
      <publish_wheel_tf>true</publish_wheel_tf>
    </plugin>
  </gazebo>

  <!-- Gazebo sensor plugin for LiDAR -->
  <gazebo reference="lidar_link">
    <sensor name="lidar" type="ray">
      <always_on>true</always_on>
      <visualize>true</visualize>
      <update_rate>10</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>720</samples>
            <resolution>1.000000</resolution>
            <min_angle>0</min_angle>
            <max_angle>6.28</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.3</min>
          <max>15.0</max>
          <resolution>0.015</resolution>
        </range>
        <noise>
          <type>gaussian</type>
          <mean>0.0</mean>
          <stddev>0.01</stddev>
        </noise>
      </ray>
      <plugin name="scan" filename="libgazebo_ros_ray_sensor.so">
        <ros>
          <remapping>~/out:=scan</remapping>
        </ros>
        <output_type>sensor_msgs/LaserScan</output_type>
        <frame_name>lidar_link</frame_name>
      </plugin>
    </sensor>
  </gazebo>
</robot>














15.1 CODE TO DESIGN WORLD

<?xml version='1.0'?>
<sdf version='1.7'>
  <world name='default'>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
      <spot>
        <inner_angle>0</inner_angle>
        <outer_angle>0</outer_angle>
        <falloff>0</falloff>
      </spot>
    </light>
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <physics type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <audio>
      <device>default</device>
    </audio>
    <wind/>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='apollo_hos'>
      <pose>4.24025 4.8058 0 0 -0 0</pose>
      <link name='Wall_0'>
        <collision name='Wall_0_Collision'>
          <geometry>
            <box>
              <size>17 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_0_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>17 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-21.325 -5.125 0 0 -0 -1.5708</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_1'>
        <collision name='Wall_1_Collision'>
          <geometry>
            <box>
              <size>43 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_1_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>43 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>0.099999 -13.55 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_10'>
        <collision name='Wall_10_Collision'>
          <geometry>
            <box>
              <size>30.25 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_10_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>30.25 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-6.475 11.65 0 0 -0 3.14159</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_2'>
        <collision name='Wall_2_Collision'>
          <geometry>
            <box>
              <size>27.25 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_2_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>27.25 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>21.525 -0 0 0 -0 1.5708</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_3'>
        <collision name='Wall_3_Collision'>
          <geometry>
            <box>
              <size>7.75 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_3_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>7.75 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>17.725 13.55 0 0 -0 3.14159</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_4'>
        <collision name='Wall_4_Collision'>
          <geometry>
            <box>
              <size>15.75 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_4_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>15.75 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>13.925 5.75 0 0 -0 -1.5708</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_5'>
        <collision name='Wall_5_Collision'>
          <geometry>
            <box>
              <size>7.25 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_5_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>7.25 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>10.375 -2.05 0 0 -0 3.14159</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_6'>
        <collision name='Wall_6_Collision'>
          <geometry>
            <box>
              <size>14.5 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_6_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>14.5 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-0.350001 -2.05 0 0 -0 3.14159</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_7'>
        <collision name='Wall_7_Collision'>
          <geometry>
            <box>
              <size>3.5 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_7_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>3.5 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>-7.525 -0.375 0 0 -0 1.5708</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_8'>
        <collision name='Wall_8_Collision'>
          <geometry>
            <box>
              <size>16.25 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_8_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>16.25 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>0.524999 1.3 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <link name='Wall_9'>
        <collision name='Wall_9_Collision'>
          <geometry>
            <box>
              <size>10.5 0.15 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='Wall_9_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>10.5 0.15 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <ambient>1 1 1 1</ambient>
          </material>
          <meta>
            <layer>0</layer>
          </meta>
        </visual>
        <pose>8.575 6.475 0 0 -0 1.5708</pose>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <static>1</static>
    </model>
    <model name='unit_box'>
      <pose>0.066714 -2.69066 0.5 0 -0 0</pose>
      <link name='link'>
        <inertial>
          <mass>1</mass>
          <inertia>
            <ixx>0.166667</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.166667</iyy>
            <iyz>0</iyz>
            <izz>0.166667</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <collision name='collision'>
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>file://media/materials/scripts/gazebo.material</uri>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <model name='unit_box_0'>
      <pose>-1.68948 -5.71412 0.5 0 -0 0</pose>
      <link name='link'>
        <inertial>
          <mass>1</mass>
          <inertia>
            <ixx>0.166667</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.166667</iyy>
            <iyz>0</iyz>
            <izz>0.166667</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <collision name='collision'>
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual'>
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>file://media/materials/scripts/gazebo.material</uri>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <state world_name='default'>
      <sim_time>36 206000000</sim_time>
      <real_time>36 531599565</real_time>
      <wall_time>1740753714 809329574</wall_time>
      <iterations>36206</iterations>
      <model name='apollo_hos'>
        <pose>4.24025 4.8058 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='Wall_0'>
          <pose>-17.0847 -0.3192 0 0 0 -1.5708</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_1'>
          <pose>4.34025 -8.7442 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_10'>
          <pose>-2.23475 16.4558 0 0 -0 3.14159</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_2'>
          <pose>25.7653 4.8058 0 0 -0 1.5708</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_3'>
          <pose>21.9653 18.3558 0 0 -0 3.14159</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_4'>
          <pose>18.1653 10.5558 0 0 0 -1.5708</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_5'>
          <pose>14.6152 2.7558 0 0 -0 3.14159</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_6'>
          <pose>3.89025 2.7558 0 0 -0 3.14159</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_7'>
          <pose>-3.28475 4.4308 0 0 -0 1.5708</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_8'>
          <pose>4.76525 6.1058 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
        <link name='Wall_9'>
          <pose>12.8153 11.2808 0 0 -0 1.5708</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='ground_plane'>
        <pose>0 0 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose>0 0 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='unit_box'>
        <pose>0.066714 -2.69066 0.499995 -1e-05 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose>0.066714 -2.69066 0.499995 -1e-05 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0.004709 0.011055 -9.78158 -0.022108 0.009414 1e-06</acceleration>
          <wrench>0.004709 0.011055 -9.78158 0 -0 0</wrench>
        </link>
      </model>
      <model name='unit_box_0'>
        <pose>-1.68948 -5.71412 0.5 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose>-1.68948 -5.71412 0.5 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>-0.004709 -9.78112 9.78158 0.712677 -0.009414 -4.3e-05</acceleration>
          <wrench>-0.004709 -9.78112 9.78158 0 -0 0</wrench>
        </link>
      </model>
      <light name='sun'>
        <pose>0 0 10 0 -0 0</pose>
      </light>
    </state>
    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose>26.9492 -3.07863 9.12676 -0 0.327643 2.96419</pose>
        <view_controller>orbit</view_controller>
        <projection_type>perspective</projection_type>
      </camera>
    </gui>
  </world>
</sdf>





































18.1 CODE TO INTEGRATE URDF IN WORLD 

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        # Specify the world file to load
        launch_arguments={'world': os.path.join(
            get_package_share_directory('hospital'), 'worlds', 'apollo_hospital.sdf')}.items(),
    )

    # Node to spawn the robot in the Gazebo simulation
    spawn_robot = Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-entity', 'robot', '-file', os.path.join(
            get_package_share_directory('robot'), 'urdf', 'robot.urdf')],
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Node to publish the robot description
    robot_description_path = os.path.join(
        get_package_share_directory('robot'), 'urdf', 'robot.urdf')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(robot_description_path).read()},
        {'use_sim_time': True}
        ]
    )

    # Return the launch description with Gazebo, robot spawn, LiDAR, and robot_state_publisher nodes
    return LaunchDescription([
        gazebo,
        spawn_robot,
        robot_state_publisher_node,
    ])
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



                                                                                        HARDWARE INTERFACE









Operating System: Ubuntu 22.04 LTS
ROS Version: ROS 2
Distributions: Humble Hawksbill
Robot Type: Differential Drive Robot
Visualization Type: Rviz,Plotjuggler
Tools Used: SLAM, NAV2
Implementation: Surveillance in controlled environment


















Information Assets:
Prerequisites: Bring_simulation


•	cd ~/hospital_ws/src
•	ros2 pkg create --build-type ament_python Hardware_interface
•	mkdir ~/hospital_ws/src/Hardware_interface/urdf
•	mkdir ~/hospital_ws/src/Hardware_interface/launch
•	touch ~/hospital_ws/src/Hardware_interface/urdf/robot.urdf
•	touch ~/hospital_ws/src/Hardware_interface/hardware_interface/motor_control_with_encoder.py
•	touch ~/hospital_ws/src/Hardware_interface/launch/visualize.launch.py


Open loop control with encoder (Arduino)
// Motor control pins
#define IN1 2  // Motor 1 control
#define IN2 3  // Motor 1 control
#define IN3 4  // Motor 2 control
#define IN4 5  // Motor 2 control
#define ENA 6  // PWM speed control for Motor 1
#define ENB 9  // PWM speed control for Motor 2

// Encoder pins (using analog pins as digital inputs)
#define ENCODER1_A A0  // Encoder 1 channel A
#define ENCODER1_B A1  // Encoder 1 channel B
#define ENCODER2_A A2  // Encoder 2 channel A
#define ENCODER2_B A3  // Encoder 2 channel B

// Encoder counters
volatile long encoder1Count = 0;
volatile long encoder2Count = 0;

// Serial communication
char command;
int pwmValue1 = 0; // PWM value for Motor 1
int pwmValue2 = 0; // PWM value for Motor 2

// Variables for encoder state
int lastEncoder1AState = LOW;
int lastEncoder2AState = LOW;

void setup() {
  // Set motor control pins as outputs
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  // Set encoder pins as inputs
  pinMode(ENCODER1_A, INPUT);
  pinMode(ENCODER1_B, INPUT);
  pinMode(ENCODER2_A, INPUT);
  pinMode(ENCODER2_B, INPUT);

  // Initialize serial communication
  Serial.begin(57600);
}

void loop() {
  // Read encoder values
  readEncoders();

  // Send encoder data to the ROS 2 node
  static unsigned long lastSendTime = 0;
  if (millis() - lastSendTime > 100) {  // Send every 100ms
    Serial.print("ENC1:");
    Serial.print(encoder1Count);
    Serial.print(",ENC2:");
    Serial.println(encoder2Count);
    lastSendTime = millis();
  }

  // Check for incoming serial data
  if (Serial.available() > 0) {
    command = Serial.read();

    // Control motors based on the command
    switch (command) {
      case 'F': // Move forward (both motors)
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'B': // Move backward (both motors)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'L': // Turn left (Motor 1 backward, Motor 2 forward)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'R': // Turn right (Motor 1 forward, Motor 2 backward)
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'S': // Stop (both motors)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 0);
        analogWrite(ENB, 0);
        break;

      case '0' ... '9': // Set PWM value (0-255) for both motors
        pwmValue1 = map(command - '0', 0, 9, 0, 255);
        pwmValue2 = map(command - '0', 0, 9, 0, 255);
        break;

      default:
        // Invalid command
        break;
    }
  }
}

// Non-interrupt-based encoder reading
void readEncoders() {
  int encoder1AState = digitalRead(ENCODER1_A);
  int encoder2AState = digitalRead(ENCODER2_A);

  // Encoder 1
  if (encoder1AState != lastEncoder1AState) {
    if (digitalRead(ENCODER1_B) != encoder1AState) {
      encoder1Count++;
    } else {
      encoder1Count--;
    }
    lastEncoder1AState = encoder1AState;
  }

  // Encoder 2
  if (encoder2AState != lastEncoder2AState) {
    if (digitalRead(ENCODER2_B) != encoder2AState) {
      encoder2Count++;
    } else {
      encoder2Count--;
    }
    lastEncoder2AState = encoder2AState;
  }
}

Python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
import serial
import time
import math

class MotorControlEncoderNode(Node):
    def __init__(self):
        super().__init__('motor_control_encoder_node')

        # Parameters
        self.declare_parameters(namespace='', parameters=[
            ('serial_port', '/dev/ttyUSB0'),
            ('baud_rate', 57600),
            ('wheel_radius', 0.05),
            ('wheel_base', 0.45),
            ('encoder_counts_per_rev', 1000),
            ('encoder_counts_per_rev_2', 1000)
        ])

        self.serial_port = self.get_parameter('serial_port').value
        self.baud_rate = self.get_parameter('baud_rate').value
        self.wheel_radius = self.get_parameter('wheel_radius').value
        self.wheel_base = self.get_parameter('wheel_base').value
        self.encoder_counts_per_rev = self.get_parameter('encoder_counts_per_rev').value
        self.encoder_counts_per_rev_2 = self.get_parameter('encoder_counts_per_rev_2').value

        # Serial connection to Arduino
        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            time.sleep(2)
            self.ser.reset_input_buffer()
            self.get_logger().info(f"Connected to Arduino on {self.serial_port}")
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to connect to Arduino: {e}")
            exit(1)

        # Subscribers and Publishers
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.twist_callback, 10)
        self.encoder_pub = self.create_publisher(Float32MultiArray, '/encoder_rpm', 10)
        self.joint_state_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)

        # Joint State
        self.joint_state = JointState()
        self.joint_state.name = ['left_wheel_joint', 'right_wheel_joint']
        self.joint_state.position = [0.0, 0.0]
        self.joint_state.velocity = [0.0, 0.0]
        self.joint_state.effort = [0.0, 0.0]

        # Odometry
        self.odom = Odometry()
        self.odom.header.frame_id = 'odom'
        self.odom.child_frame_id = 'base_link'
        self.odom.pose.pose.orientation.w = 1.0

        # Encoder Data
        self.last_enc1 = 0
        self.last_enc2 = 0
        self.last_time = self.get_clock().now()

        # Robot State
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Timer
        self.timer = self.create_timer(0.1, self.read_encoder_data)  # 10Hz

    def twist_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        # Send motor commands
        if linear_x > 0:
            self.ser.write(b'F')  # Forward
        elif linear_x < 0:
            self.ser.write(b'B')  # Backward
        elif angular_z > 0:
            self.ser.write(b'L')  # Left
        elif angular_z < 0:
            self.ser.write(b'R')  # Right
        else:
            self.ser.write(b'S')  # Stop

        # Send PWM value (0-9)
        pwm_value = min(int((abs(linear_x) + abs(angular_z)) * 9), 9)
        self.ser.write(str(pwm_value).encode())

    def read_encoder_data(self):
        if self.ser.in_waiting > 0:
            try:
                serial_data = self.ser.readline().decode('utf-8').strip()
                if "ENC1:" in serial_data and "ENC2:" in serial_data:
                    enc1 = int(serial_data.split("ENC1:")[1].split(",")[0])
                    enc2 = int(serial_data.split("ENC2:")[1])

                    current_time = self.get_clock().now()
                    dt = (current_time - self.last_time).nanoseconds / 1e9

                    if dt == 0:
                        return

                    # Calculate RPM
                    rpm1 = ((enc1 - self.last_enc1) / self.encoder_counts_per_rev) * (60 / dt)
                    rpm2 = ((enc2 - self.last_enc2) / self.encoder_counts_per_rev_2) * (60 / dt)

                    # Log RPM values
                    self.get_logger().info(f"RPM Left: {rpm1:.2f}, RPM Right: {rpm2:.2f}")

                    # Update joint states (radians)
                    delta_theta_left = (enc1 - self.last_enc1) * (2 * math.pi / self.encoder_counts_per_rev)
                    delta_theta_right = (enc2 - self.last_enc2) * (2 * math.pi / self.encoder_counts_per_rev_2)
                    self.joint_state.position[0] += delta_theta_left
                    self.joint_state.position[1] += delta_theta_right

                    # Update joint velocities (rad/s)
                    self.joint_state.velocity[0] = rpm1 * (2 * math.pi / 60)
                    self.joint_state.velocity[1] = rpm2 * (2 * math.pi / 60)

                    # Publish joint states
                    self.joint_state.header.stamp = self.get_clock().now().to_msg()
                    self.joint_state_pub.publish(self.joint_state)

                    # Update odometry
                    self.update_odometry(enc1 - self.last_enc1, enc2 - self.last_enc2, dt)

                    # Publish RPM
                    rpm_msg = Float32MultiArray()
                    rpm_msg.data = [rpm1, rpm2]
                    self.encoder_pub.publish(rpm_msg)

                    self.last_enc1 = enc1
                    self.last_enc2 = enc2
                    self.last_time = current_time

            except (UnicodeDecodeError, ValueError) as e:
                self.get_logger().warn(f"Encoder data error: {e}")

    def update_odometry(self, delta_enc1, delta_enc2, dt):
        # Calculate wheel distances
        distance_left = (delta_enc1 / self.encoder_counts_per_rev) * (2 * math.pi * self.wheel_radius)
        distance_right = (delta_enc2 / self.encoder_counts_per_rev_2) * (2 * math.pi * self.wheel_radius)

        # Calculate linear and angular velocity
        linear_velocity = (distance_right + distance_left) / 2.0
        angular_velocity = (distance_right - distance_left) / self.wheel_base

        # Update pose
        self.x += linear_velocity * math.cos(self.theta)
        self.y += linear_velocity * math.sin(self.theta)
        self.theta += angular_velocity

        # Normalize theta
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

        # Update odometry message
        self.odom.header.stamp = self.get_clock().now().to_msg()
        self.odom.pose.pose.position.x = self.x
        self.odom.pose.pose.position.y = self.y
        self.odom.pose.pose.orientation.z = math.sin(self.theta / 2.0)
        self.odom.pose.pose.orientation.w = math.cos(self.theta / 2.0)
        self.odom.twist.twist.linear.x = linear_velocity / dt
        self.odom.twist.twist.angular.z = angular_velocity / dt
        self.odom_pub.publish(self.odom)

        # Broadcast TF
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_link'
        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.rotation.z = math.sin(self.theta / 2.0)
        transform.transform.rotation.w = math.cos(self.theta / 2.0)
        self.tf_broadcaster.sendTransform(transform)

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlEncoderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.ser.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


visualize.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    return LaunchDescription([
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open('/home/vikash/Hospital_ws/src/hospital_hardware/urdf/robot.urdf').read()}]
        ),
        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            name="joint_state_publisher"
        ),
        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/vikash/Hospital_ws/src/hospital_hardware/config/config.rviz']
        ),


    ])

Setup.py

from setuptools import find_packages, setup
package_name = 'hospital_hardware'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/visualize.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/robot.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vikash',
    maintainer_email='vikash@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_control_with_encoder = hospital_hardware.motor_control_with_encoder:main'
            
        ],
    },
)

Robot.urdf
<?xml version="1.0"?>
<robot name="hospital_robot">
  <!-- Define materials -->
  <material name="gray">
    <color rgba="0.7 0.7 0.7 1"/>
  </material>
  <material name="black">
    <color rgba="0.00 0.59 0.53 1"/>
  </material>
  <material name="purple">
    <color rgba="0.5 0 0.5 1"/>
  </material>


  <!-- Base footprint link -->
  <link name="base_footprint"/>



  <!-- Base link of the robot -->
  <link name="base_link">
    <visual>
      <origin xyz="0 0 0.1"/>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
      <material name="gray"/>
    </visual>
  </link>
  
  <!-- Odom frame -->


  <!-- Joint between base_footprint and base_link -->
  <joint name="base_footprint_joint" type="fixed">
    <parent link="base_link"/>
    <child link="base_footprint"/>
    <origin xyz="0 0 0.1" rpy="0 0 0"/>
  </joint>

  <!-- Left wheel link -->
  <link name="left_wheel">
    <visual>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.12"/>
      </geometry>
      <material name="black"/>
    </visual>
  </link>

  <!-- Right wheel link -->
  <link name="right_wheel">
    <visual>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <cylinder length="0.05" radius="0.12"/>
      </geometry>
      <material name="black"/>
    </visual>
  </link>

  <!-- Left wheel joint -->
  <joint name="left_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="left_wheel"/>
    <origin xyz="0 0.225 0.1" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <!-- Right wheel joint -->
  <joint name="right_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="right_wheel"/>
    <origin xyz="0 -0.225 0.1" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>


  <!-- LiDAR sensor -->
  <link name="lidar_link">
    <visual>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="purple"/>
    </visual>
  </link>
 
  <!-- LiDAR joint -->
  <joint name="lidar_joint" type="fixed">
    <parent link="base_link"/>
    <child link="lidar_link"/>
    <origin xyz="0.2 0 0.225" rpy="0 0 0"/>
  </joint>

  <!-- Castor wheel link (optional) -->
  <link name="castor_wheel">
    <visual>
      <origin xyz="0 0 0" rpy="1.57 0 0"/>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="black"/>
    </visual>
  </link>

  <!-- Castor wheel joint (optional) -->
  <joint name="castor_wheel_joint" type="fixed">
    <parent link="base_link"/>
    <child link="castor_wheel"/>
    <origin xyz="0.3 0 0.05" rpy="0 0 0"/>
  </joint>
</robot>

















Code To check Encoder count(Arduino) 

// Motor control pins
#define IN1 2  
#define IN2 3  
#define IN3 4  
#define IN4 5  
#define ENA 6  
#define ENB 9  

// Encoder pins
#define ENCODER1_A A0  
#define ENCODER1_B A1  
#define ENCODER2_A A2  
#define ENCODER2_B A3  

// Encoder counters
volatile long encoder1Count = 0;
volatile long encoder2Count = 0;

// Variables for encoder state
int lastEncoder1AState = LOW;
int lastEncoder2AState = LOW;

unsigned long startTime;
bool running = true;

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  pinMode(ENCODER1_A, INPUT);
  pinMode(ENCODER1_B, INPUT);
  pinMode(ENCODER2_A, INPUT);
  pinMode(ENCODER2_B, INPUT);

  Serial.begin(57600);

  // Start motors at full speed
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);

  startTime = millis();
}

void loop() {
  if (running) {
    readEncoders();

    static unsigned long lastSendTime = 0;
    if (millis() - lastSendTime > 100) {
      Serial.print("ENC1:");
      Serial.print(encoder1Count);
      Serial.print(", ENC2:");
      Serial.println(encoder2Count);
      lastSendTime = millis();
    }

    if (millis() - startTime >= 5000) {
      stopMotors();
      Serial.println("Motors stopped.");
      running = false;
    }
  }
}

void readEncoders() {
  int encoder1AState = digitalRead(ENCODER1_A);
  int encoder2AState = digitalRead(ENCODER2_A);

  if (encoder1AState != lastEncoder1AState) {
    encoder1Count += (digitalRead(ENCODER1_B) != encoder1AState) ? 1 : -1;
    lastEncoder1AState = encoder1AState;
  }

  if (encoder2AState != lastEncoder2AState) {
    encoder2Count += (digitalRead(ENCODER2_B) != encoder2AState) ? 1 : -1;
    lastEncoder2AState = encoder2AState;
  }
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

////////////////////////////////////////////////////////////////////////////////////////////////////
Open loop control Motor_control (Arduino to Ros2 communication)
// Motor control pins
#define IN1 2  // Motor 1 control
#define IN2 3  // Motor 1 control
#define IN3 4  // Motor 2 control
#define IN4 5  // Motor 2 control
#define ENA 6  // PWM speed control for Motor 1
#define ENB 9  // PWM speed control for Motor 2
//d11,d12    d7,d8 encoder pinout
// Serial communication
char command;
int pwmValue1 = 0; // PWM value for Motor 1
int pwmValue2 = 0; // PWM value for Motor 2

void setup() {
  // Set motor control pins as outputs
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  // Initialize serial communication
  Serial.begin(115200);
}

void loop() {
  // Check for incoming serial data
  if (Serial.available() > 0) {
    command = Serial.read();

    // Control motors based on the command
    switch (command) {
      case 'F': // Move forward (both motors)
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'B': // Move backward (both motors)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'L': // Turn left (Motor 1 backward, Motor 2 forward)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'R': // Turn right (Motor 1 forward, Motor 2 backward)
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
        analogWrite(ENA, pwmValue1);
        analogWrite(ENB, pwmValue2);
        break;

      case 'S': // Stop (both motors)
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        analogWrite(ENA, 0);
        analogWrite(ENB, 0);
        break;

      case '0' ... '9': // Set PWM value (0-255) for both motors
        pwmValue1 = map(command - '0', 0, 9, 0, 255);
        pwmValue2 = map(command - '0', 0, 9, 0, 255);
        break;

      default:
        // Invalid command
        break;
    }
  }
}

Motor_control.py (Arduino to Ros2 communication)
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class MotorControlNode(Node):
    def _init_(self):
        super()._init_('motor_control_node')

        # Serial port configuration
        self.serial_port = '/dev/ttyUSB0'  # Change this to your Arduino's serial port
        self.baud_rate = 115200

        # Initialize serial connection
        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            self.get_logger().info(f"Connected to Arduino on {self.serial_port}")
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to connect to Arduino: {e}")
            exit(1)

        # Subscribe to the /cmd_vel topic
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.twist_callback,
            10
        )
        self.subscription  # Prevent unused variable warning

    def twist_callback(self, msg):
        """
        Callback function for the /cmd_vel topic.
        Converts Twist messages to motor commands and sends them to the Arduino.
        """
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        if linear_x > 0:  # Move forward
            self.ser.write(b'F')
        elif linear_x < 0:  # Move backward
            self.ser.write(b'B')
        elif angular_z > 0:  # Turn left
            self.ser.write(b'L')
        elif angular_z < 0:  # Turn right
            self.ser.write(b'R')
        else:  # Stop
            self.ser.write(b'S')

        # Map linear and angular velocities to PWM values (0-9)
        pwm_value = int((abs(linear_x) + abs(angular_z)) * 9)
        if pwm_value > 9:
            pwm_value = 9
        self.ser.write(str(pwm_value).encode())

def main(args=None):
    rclpy.init(args=args)

    motor_control_node = MotorControlNode()

    try:
        rclpy.spin(motor_control_node)
    except KeyboardInterrupt:
        pass
    finally:
        # Close serial connection on shutdown
        motor_control_node.ser.close()
        motor_control_node.destroy_node()
        rclpy.shutdown()

if _name_ == '_main_':
    main()

////////////////////////////////////////////////////////////////////////////////////////////////////


