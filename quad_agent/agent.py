import sys
sys.path.append('../')

import rospy
import tf

from d_erg_lib import DErgControl
from model import Model
from rendering import Visual


class Agent(Model, Visual):

    def __init__(self, agent_name):

        self.agent_name = agent_name
        rospy.init_node(agent_name)
        self._rate = rospy.Rate(10)
        Model.__init__(self)
        Visual.__init__(self, agent_name)
        self.ctrllr = DErgControl(agent_name, Model())
        self.__br = tf.TransformBroadcaster()

    def step(self):
        ctrl = self.ctrllr(self.state)
        pred_path = self.ctrllr.pred_path
        super(Agent, self).step(ctrl)
        self.update_rendering(pred_path)
        self.__br.sendTransform(
            (self.state[0]*10, self.state[1]*10, 0.),
            (0.,0.,0.,1.),
            rospy.Time.now(),
            self.agent_name,
            "world"
        )

    def run(self):
        while not rospy.is_shutdown():
            self.step()
            self._rate.sleep()