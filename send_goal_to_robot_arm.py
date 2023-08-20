#!/usr/bin/env python
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint

def move_robot_arm(joint_values):
    rospy.init_node('robot_arm_controller')

    arm_client = actionlib.SimpleActionClient('/arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
    arm_client.wait_for_server()

    arm_goal = FollowJointTrajectoryGoal()

    # Set the joint names based on your YAML configuration
    arm_goal.trajectory.joint_names = [
        'revolute1', 'revolute2', 'revolute3', 'revolute4', 'revolute5', 'revolute6', 'revolute7', 'Revolute 8'
    ]

    point = JointTrajectoryPoint()
    point.positions = joint_values
    point.time_from_start = rospy.Duration(3)

    arm_goal.trajectory.points.append(point)

    exec_timeout = rospy.Duration(10)
    prmpt_timeout = rospy.Duration(5)

    arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)

if __name__ == '__main__':
    try:
        rospy.init_node('send_goal_to_robot_arm')
        move_robot_arm([-0.1, 0.5, 0.02, 0, 0, 0, 0, 0])
        print("Robot arm has successfully reached the goal!")
    except rospy.ROSInterruptException:
        print("Program interrupted before completion.")
