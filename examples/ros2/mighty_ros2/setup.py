import sys

from setuptools import setup

package_name = "mighty_ros2"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name, "mighty_sdk"],
    package_dir={"mighty_sdk": "../../../python/mighty_sdk"},
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", ["launch/mighty_ros2.launch.py"]),
        (
            f"lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages",
            [
                "../../../python/mighty_protocol.py",
                "../../../python/dispatcher.py",
                "../../../python/decoded_dispatcher.py",
            ],
        ),
    ],
    install_requires=["setuptools", "Pillow>=9.0"],
    zip_safe=True,
    maintainer="Mighty Camera",
    maintainer_email="hello@mightycamera.com",
    description="ROS 2 publisher wrapper for Mighty Camera SDK streams.",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "mighty_ros2_publisher = mighty_ros2.publisher:main",
        ],
    },
)
