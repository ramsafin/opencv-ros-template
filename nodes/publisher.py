#!/usr/bin/env python3
# encoding: utf-8

import rospy
from sensor_msgs.msg import Image

from typing import Final

# constants
ROS_NODE_NAME: Final[str] = "publisher"

ROS_PARAM_PUB_RATE: Final[int] = 30
ROS_PUBLISH_TOPIC: Final[str] = "image"


def main() -> None:
  rospy.init_node(ROS_NODE_NAME)

  # Пример запуска с параметром: rosrun template publisher.py _rate:=10
  pub_frequency: int = rospy.get_param("~rate", ROS_PARAM_PUB_RATE)

  # Обратите внимание: топик "image" может переименоваться при запуске ROS-узла.
  # rosrun template publisher.py image:=image_raw
  # Более подробно об этом можно узнать по ссылке: http://wiki.ros.org/Names
  rospy.loginfo(f"Publishing to '{rospy.resolve_name(ROS_PUBLISH_TOPIC)}' at {pub_frequency} Hz ...")

  # Q: Почему здесь не нужно писать rospy.resolve_name(ROS_IMAGE_TOPIC)?
  publisher = rospy.Publisher(ROS_PUBLISH_TOPIC, Image, queue_size=10)

  rate = rospy.Rate(pub_frequency)

  while not rospy.is_shutdown():
    # Задание 1: сгенерируйте случайное изображение.
    # Разрешение: 320 x 240 (ширина x высота).
    # Формат пикселей: монохром, 8-бит.
    # Создайте функцию для генерации изображения "generate_image(width = 320, height = 240)".
    publisher.publish(Image(width=0, height=0, encoding='mono8'))

    rate.sleep()


if __name__ == '__main__':
    main()
