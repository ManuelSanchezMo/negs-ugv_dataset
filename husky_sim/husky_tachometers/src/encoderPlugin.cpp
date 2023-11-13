
#include "ros/ros.h"
#include <gazebo/common/Plugin.hh>
#include <sensor_msgs/MagneticField.h>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/transport/transport.hh>
#include <gazebo/msgs/msgs.hh>
#include <thread>
#include "ros/ros.h"
#include "ros/callback_queue.h"
#include "ros/subscribe_options.h"
#include "std_msgs/Float32.h"
#include "std_msgs/String.h"
#include "std_msgs/Header.h"
#include <gazebo/physics/physics.hh>
#include <husky_tachometers/Encoder.h>
#include <stdlib.h> 
#include <hector_gazebo_plugins/update_timer.h>
namespace gazebo
{
  /// \brief A plugin to control a Velodyne sensor.
  class HusckyEncoderPlugin : public ModelPlugin
  {
    /// \brief Constructor
    public: HusckyEncoderPlugin() {}

    /// \brief The load function is called by Gazebo when the plugin is
    /// inserted into simulation
    /// \param[in] _model A pointer to the model that this plugin is
    /// attached to.
    /// \param[in] _sdf A pointer to the plugin's SDF element.
    public: void OnUpdate(){}
    public: void Update()
    {
    double now = ros::Time::now().toSec();
       #if (GAZEBO_MAJOR_VERSION >= 8)
         common::Time cur_time = world->SimTime();
       #else
         common::Time cur_time = world->GetSimTime();
       #endif
          double dt = updateTimer.getTimeSinceLastUpdate().Double();
          result_fr=this->joint_fr->GetVelocity (0);
          encoder_msg.angular_speed=result_fr;
          std_msgs::Header header;
          header.stamp= ros::Time::now();
          header.frame_id="fr" ;
          encoder_msg.header=header;
         this->pub_fr.publish(encoder_msg);
          result_fl=this->joint_fl->GetVelocity (0);
          encoder_msg.angular_speed=result_fl;
          header.stamp= ros::Time::now();
          header.frame_id="fl";
          encoder_msg.header=header;
          pub_msgfloat.data=result_fl;
         this->pub_fl.publish(encoder_msg);
          result_rl=this->joint_rl->GetVelocity (0);
          encoder_msg.angular_speed=result_rl;
          header.stamp= ros::Time::now();
          header.frame_id="rl";
          pub_msgfloat.data=result_rl;
          encoder_msg.header=header;
         this->pub_bl.publish(encoder_msg);
          result_rr=this->joint_rr->GetVelocity (0);
          encoder_msg.angular_speed=result_fl;
          header.stamp= ros::Time::now();
          header.frame_id="rr";
          pub_msgfloat.data=result_rr;
          encoder_msg.header=header;
         this->pub_br.publish(encoder_msg);



	}
    
    public: virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      // Safety check
      if (_model->GetJointCount() == 0)
      {
        std::cerr << "Invalid joint count, encoder plugin not loaded\n";
        return;
      }
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          std::bind(&HusckyEncoderPlugin::OnUpdate, this));
      // Store the model pointer for convenience.
      this->model = _model;
      
      // Get the first joint. We are making an assumption about the model
      // having one joint that is the rotational joint.
      this->joint = _model->GetJoints()[0];

      // Setup a P-controller, with a gain of 0.1.
      this->pid = common::PID(0.1, 0, 0);

      // Apply the P-controller to the joint.
      this->model->GetJointController()->SetVelocityPID(
          this->joint->GetScopedName(), this->pid);
      this->joint_fr = this->model->GetJoint("front_right_wheel");
      this->joint_fl = this->model->GetJoint("front_left_wheel");
      this->joint_rl = this->model->GetJoint("rear_left_wheel");
      this->joint_rr = this->model->GetJoint("rear_right_wheel");



      // Create the node
      this->node = transport::NodePtr(new transport::Node());
      #if GAZEBO_MAJOR_VERSION < 8
      this->node->Init(this->model->GetWorld()->GetName());
      #else
      this->node->Init(this->model->GetWorld()->Name());
      #endif



// Initialize ros, if it has not already bee initialized.
if (!ros::isInitialized())
{
  int argc = 0;
  char **argv = NULL;
  ros::init(argc, argv, "gazebo_client",
      ros::init_options::NoSigintHandler);
}

// Create our ROS node. This acts in a similar manner to
// the Gazebo node
this->rosNode.reset(new ros::NodeHandle("gazebo_client"));



this->pub_fr = this->rosNode->advertise<husky_tachometers::Encoder>("front_right_speed", 1000);
this->pub_fl = this->rosNode->advertise<husky_tachometers::Encoder>("front_left_speed", 1000);
this->pub_bl = this->rosNode->advertise<husky_tachometers::Encoder>("back_left_speed", 1000);
this->pub_br = this->rosNode->advertise<husky_tachometers::Encoder>("back_right_speed", 1000);
// Spin up the queue helper thread.
this->rosQueueThread =
  std::thread(std::bind(&HusckyEncoderPlugin::QueueThread, this));
world = _model->GetWorld();
  updateTimer.setUpdateRate(10.0);
 updateTimer.Load(world, _sdf);
  updateConnection = updateTimer.Connect(boost::bind(&HusckyEncoderPlugin::Update, this));
    }
    /// \brief Handle an incoming message from ROS
/// \param[in] _msg A float value that is used to set the velocity
/// of the Velodyne.


/// \brief ROS helper function that processes messages
private: void QueueThread()
{
  static const double timeout = 0.01;
  while (this->rosNode->ok())
  {
    this->rosQueue.callAvailable(ros::WallDuration(timeout));
  }
}
    /// \brief Set the velocity of the Velodyne
    /// \param[in] _vel New target velocity

     /// \brief A node use for ROS transport
private: std::unique_ptr<ros::NodeHandle> rosNode;

/// \brief A ROS subscriber
private: physics::JointPtr joint_fr ;
private: double result_fr;

private: physics::JointPtr joint_fl ;
private: double result_fl;

private: physics::JointPtr joint_rl;
private: double result_rl;

private: physics::JointPtr joint_rr ;
private: double result_rr;
private: std_msgs::Float32  pub_msgfloat;
private: husky_tachometers::Encoder  encoder_msg;
private: ros::Subscriber rosSub;
private: ros::Subscriber sub_mag_;
private: ros::Publisher chatter_pub;
private: ros::Publisher pub_fr;
private: ros::Publisher pub_fl;
private: ros::Publisher pub_br;
private: ros::Publisher pub_bl;
/// \brief A ROS callbackqueue that helps process messages
private: ros::CallbackQueue rosQueue;

/// \brief A thread the keeps running the rosQueue
private: float angle;  
    /// \brief A node used for transport
private: transport::NodePtr node;
private: std::thread rosQueueThread;  
    /// \brief A subscriber to a named topic.
private: transport::SubscriberPtr sub;

    /// \brief Pointer to the model.
private: physics::ModelPtr model;

    /// \brief Pointer to the joint.
private: physics::JointPtr joint;

    /// \brief A PID controller for the joint.
private: common::PID pid;
private: event::ConnectionPtr updateConnection;
private: float last_time=0; 
private: UpdateTimer updateTimer; 
private: physics::WorldPtr world;
private:   boost::mutex lock;
  };

  // Tell Gazebo about this plugin, so that Gazebo can call Load on this plugin.
  GZ_REGISTER_MODEL_PLUGIN(HusckyEncoderPlugin)
}

