#include <ros/package.h>
#include <ros/ros.h>

#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/Image.h>  // sensor_msgs::Image

#include <opencv2/highgui/highgui.hpp>  // imshow
#include <opencv2/imgproc/imgproc.hpp>  // cvtColor, ...

static constexpr double TOPIC_WAIT_DURATION_SECS = 3.0;

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  auto image = cv_bridge::toCvCopy(msg);
  // ... imshow
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "subscriber_cpp");
  ros::NodeHandle handle;

  if (!ros::topic::waitForMessage<sensor_msgs::Image>("image", handle, ros::Duration(TOPIC_WAIT_DURATION_SECS))) {
    ROS_ERROR("Could not recieve an image message");
    return 0;
  }

  ros::Subscriber subscriber = handle.subscribe("image", 10, imageCallback);
  ros::spin();

  return 0;
}
