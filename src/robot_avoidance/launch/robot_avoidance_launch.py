import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('robot_avoidance'),
        'config',
        'avoidance_config.yaml'
    )
    return LaunchDescription([
        Node(
            package='robot_avoidance',
            executable='avoidance',
            name='avoidance',
            output='screen',
            parameters=[
                config
            ]
        ),
    ])
