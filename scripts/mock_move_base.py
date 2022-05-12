#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import (
    MoveBaseGoal,
    MoveBaseAction,
    MoveBaseResult,
    MoveBaseFeedback,
)


class MockMoveBase:
    def __init__(self):
        rospy.init_node("move_base_node")
        self._as = actionlib.SimpleActionServer("move_base", MoveBaseAction, self.cb)

    def cb(self, goal: MoveBaseGoal):
        rospy.loginfo("{}".format(goal))
        feedback = MoveBaseFeedback()
        self._as.publish_feedback(feedback)
        result = MoveBaseResult()
        self._as.set_succeeded(result)


if __name__ == "__main__":
    MockMoveBase()
    rospy.spin()
