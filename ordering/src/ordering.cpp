
#include "tsp-ga.cpp"
#include "Point.cpp"
#include <iostream>
#include <fstream>
#include <cstdlib>  	// srand(), atoi()
#include <ctime> 		// time()
#include <getopt.h>
#include "ros/ros.h"
#include "Point.h"
#include "tsp-ga.h"
#include <darknet_ros_msgs/testing_ar.h>
#include <ordering/testing_ar.h>
//#include "darknet_ros/YoloObjectDetector.hpp"
//#include "darknet_ros/BoundingBoxes.h"
#include "darknet_ros_msgs/fruit.h"
#include "darknet_ros_msgs/testing.h"
#include "std_msgs/Int32.h"

using std::ofstream;
using std::cin;
using std::cout;
using std::endl;
using std::vector;

darknet_ros_msgs::testing    msg_recv;       // recv: data recv
darknet_ros_msgs::testing_ar         msg_cal_recv;

//ordering::testing_ar         msg_cal_recv;

void help();

//void msgCallback_order(const darknet_ros_msgs::testing::ConstPtr& fruit_recv);
void position_callback(const darknet_ros_msgs::testing::ConstPtr &msg);
void position_callback_recv(const darknet_ros_msgs::testing_ar::ConstPtr &msg_cal);

//void position_callback_recv(const ordering::testing_ar::ConstPtr &msg_cal);

int main(int argc, char **argv) {

        ros::init(argc, argv, "Ordering_node");
        ros::NodeHandle n;

	ros::Publisher pub = n.advertise<ordering::testing_ar>("/order", 1);


	/*msg_cal_recv.pointsNumber = msg_recv.pointsNumber;
	msg_cal_recv.xpos1 = msg_recv.xpos1;
	msg_cal_recv.ypos1 = msg_recv.ypos1;
	msg_cal_recv.zpos1 = msg_recv.zpos1;

	ROS_INFO("publish: %d", msg_recv.xpos1);
	pub.publish(msg_cal_recv);*/



	//rate rospy.Rate(30);
	ros::Subscriber sub_recv = n.subscribe("/ordering", 1, &position_callback_recv);
        ros::Subscriber sub = n.subscribe<darknet_ros_msgs::testing>("/fruit_position", 1, &position_callback);


	
	// Parsing Arguments

	int populationSize, numGenerations,
			keepPopulation, numMutations;

	int c;

	while(1) {

		static struct option long_options[] = {
			{"population",	required_argument,	0,	'p'},
			{"generation",	required_argument,	0,	'g'},
			{"keep",	required_argument,	0,	'k'},
			{"mutation",	required_argument,	0,	'm'},
			{"help",		no_argument,	0,	'h'},
			{0, 0, 0, 0}
		};

		/* getopt_long stores the option index here. */
		int option_index = 0;

		c = getopt_long (argc, argv, "p:g:k:m:h",
                       long_options, &option_index);
		/* Detect the end of the options. */
    	if (c == -1)
    	break;

    	switch(c)
    		{
    		case 'p':
    			populationSize = atoi(optarg); break;
    		case 'g':
    			numGenerations = atoi(optarg); break;
    		case 'k':
    			keepPopulation = atoi(optarg); break;
    		case 'm':
    			numMutations = atoi(optarg); break;
    		case 'h':
    			help(); exit(0);
    		default :
    			abort ();
    		}
    	}

    //if(argc != 9) {
    //	help();
    //}

	// Setting Input


	srand (unsigned (time (0)));

	int pointsNumber = msg_recv.pointsNumber;
	double inputX, inputY, inputZ;
	vector<Point>pointsCluster;

	//scanf("%d", &pointsNumber);


	double inputX1, inputY1, inputZ1;
	inputX1 = msg_recv.xpos1;
        inputY1 = msg_recv.ypos1;
        inputZ1 = msg_recv.zpos1;
	
	double inputX2, inputY2, inputZ2;
	inputX2 = msg_recv.xpos2;
        inputY2 = msg_recv.ypos2;
        inputZ2 = msg_recv.zpos2;
	
	double inputX3, inputY3, inputZ3;
	inputX3 = msg_recv.xpos3;
        inputY3 = msg_recv.ypos3;
        inputZ3 = msg_recv.zpos3;

	double inputX4, inputY4, inputZ4;
	inputX4 = msg_recv.xpos4;
        inputY4 = msg_recv.ypos4;
        inputZ4 = msg_recv.zpos4;

	while (pointsNumber > 0){
	if (pointsNumber == 1){
		Point Input1 {inputX1, inputY1, inputZ1};
		pointsCluster.push_back(Input1);		
	}
	
	if (pointsNumber == 2){
		Point Input1 {inputX1, inputY1, inputZ1};
		Point Input2 {inputX2, inputY2, inputZ2};
		pointsCluster.push_back(Input1);
		pointsCluster.push_back(Input2);

	}

	if (pointsNumber == 3){
		Point Input1 {inputX1, inputY1, inputZ1};
		Point Input2 {inputX2, inputY2, inputZ2};
		Point Input3 {inputX3, inputY3, inputZ3};
		pointsCluster.push_back(Input1);
		pointsCluster.push_back(Input2);
		pointsCluster.push_back(Input3);
	}

	}

	ros::spin();


	ofstream HzWriteFile("posw.txt");
	HzWriteFile << msg_recv.pointsNumber << endl;
	HzWriteFile << msg_recv.xpos1 << " " << msg_recv.ypos1 << " " << msg_recv.zpos1 << endl;
	HzWriteFile << msg_recv.xpos2 << " " << msg_recv.ypos2 << " " << msg_recv.zpos2 << endl;
	HzWriteFile << msg_recv.xpos3 << " " << msg_recv.ypos3 << " " << msg_recv.zpos3 << endl;
	HzWriteFile << msg_recv.xpos4 << " " << msg_recv.ypos4 << " " << msg_recv.zpos4 << endl;
	HzWriteFile << msg_recv.xpos5 << " " << msg_recv.ypos5 << " " << msg_recv.zpos5 << endl;
	HzWriteFile << msg_recv.xpos6 << " " << msg_recv.ypos6 << " " << msg_recv.zpos6 << endl;
	HzWriteFile << msg_recv.xpos7 << " " << msg_recv.ypos7 << " " << msg_recv.zpos7 << endl;
	HzWriteFile << msg_recv.xpos8 << " " << msg_recv.ypos8 << " " << msg_recv.zpos8 << endl;
	HzWriteFile << msg_recv.xpos9 << " " << msg_recv.ypos9 << " " << msg_recv.zpos9 << endl;
	HzWriteFile.close(); 


	freopen("posw.txt", "rt", stdin);

	cin >> pointsNumber;

	for(int i = 0; i < pointsNumber; i++) {
		cin >> inputX >> inputY >> inputZ ;
		Point inputPoint {inputX, inputY, inputZ};
		pointsCluster.push_back(inputPoint);
	}


	// Run Genetic Algorithm

	TSPGenome goodGenome = findAShortPath(pointsCluster, populationSize,numGenerations,
					keepPopulation, numMutations);
	vector<int> GOrder = goodGenome.getOrder();
	double GLength = goodGenome.getCircuitLength();

	cout << "Shortest Path Found : [";
	ofstream fout("order.txt");
	for(const auto& genome : GOrder) {
		cout << " " << genome;
		fout << genome << endl;
	}
	fout.close();
	cout << "]\nLength is : " << GLength << endl;

	//darknet_ros_msgs::testing_ar	msg_cal;

/*	if (GOrder[0] = 0){
	//ordering::testing_ar msg_cal_recv;
	msg_cal_recv.pointsNumber = msg_recv.pointsNumber;
	msg_cal_recv.xpos1 = msg_recv.xpos1;
	msg_cal_recv.ypos1 = msg_recv.ypos1;
	msg_cal_recv.zpos1 = msg_recv.zpos1;

	//ROS_INFO("publish: %d", msg_recv.xpos1);
	//pub.publish(msg_cal_recv);

	}

	if (GOrder[0] = 1){
	//ordering::testing_ar msg_cal_recv;
	msg_cal_recv.pointsNumber = msg_recv.pointsNumber;
	msg_cal_recv.xpos1 = msg_recv.xpos1;
	msg_cal_recv.ypos1 = msg_recv.ypos1;
	msg_cal_recv.zpos1 = msg_recv.zpos1;

	//ROS_INFO("publish: %d", msg_recv.pointsNumber);
	
	}
	
	if (GOrder[0] = 2){
	msg_cal_recv.xpos1 = msg_recv.xpos3;
	msg_cal_recv.ypos1 = msg_recv.ypos3;
	msg_cal_recv.zpos1 = msg_recv.zpos3;
	}

	// GOrder[1] 
	if (GOrder[1] = 0){
	msg_cal_recv.xpos2 = msg_recv.xpos1;
	msg_cal_recv.ypos2 = msg_recv.ypos1;
	msg_cal_recv.zpos2 = msg_recv.zpos1;
	}

	if (GOrder[1] = 1){
	msg_cal_recv.xpos2 = msg_recv.xpos2;
	msg_cal_recv.ypos2 = msg_recv.ypos2;
	msg_cal_recv.zpos2 = msg_recv.zpos2;
	}
	
	if (GOrder[1] = 2){
	msg_cal_recv.xpos2 = msg_recv.xpos3;
	msg_cal_recv.ypos2 = msg_recv.ypos3;
	msg_cal_recv.zpos2 = msg_recv.zpos3;
	}

	// GOrder[2] 
	if (GOrder[2] = 0){
	msg_cal_recv.xpos3 = msg_recv.xpos1;
	msg_cal_recv.ypos3 = msg_recv.ypos1;
	msg_cal_recv.zpos3 = msg_recv.zpos1;
	}

	if (GOrder[2] = 1){
	msg_cal_recv.xpos3 = msg_recv.xpos2;
	msg_cal_recv.ypos3 = msg_recv.ypos2;
	msg_cal_recv.zpos3 = msg_recv.zpos2;
	}
	
	if (GOrder[2] = 2){
	msg_cal_recv.xpos3 = msg_recv.xpos3;
	msg_cal_recv.ypos3 = msg_recv.ypos3;
	msg_cal_recv.zpos3 = msg_recv.zpos3;
	}
*/




	//pub.publish(msg_cal_recv);

	// GOrder[0] 

	//ROS_INFO_STREAM("publish: " << msg_recv.pointsNumber);

/*	
	for(const auto& genome : GOrder){
		msg_cal_recv.xpos1 = 		
		pub.publish(msg);
		ros::spinOnce();
		

*/	

	return 0;
}


void help() {
    	cout <<
    		"Usage: ./tsp-ga [OPTIONS]\n"
    		"ALL OPTIONS ARE REQUIRED\n"
    		"where options are :\n"
    		"-p <value>, --population <value>\n"
    		"population is a positive integer specifying the population size.\n\n"

    		"-g <value>, --generation <value>\n"
    		"generations is a positive integer specifying how many generations to run the GA for.\n\n"

    		"-k <value>, --keep <value>\n"
    		"the number of the population that should be preserved from generation to generation.\n\n"

    		"-m <value>, --mutation <value>\n"
    		"specifies how many mutations to apply to each member of the population."
    		<< endl;
}


void position_callback(const darknet_ros_msgs::testing::ConstPtr &msg){

    msg_recv = *msg;

    //ROS_INFO_STREAM("publish: " << msg_recv.pointsNumber);
    //ROS_INFO_STREAM("publish: " << msg_recv.xpos1;);
    //ROS_INFO_STREAM("publish: " << msg_recv.xpos2;);

}

//void position_callback_recv(const ordering::testing_ar::ConstPtr &msg_cal)
void position_callback_recv(const darknet_ros_msgs::testing_ar::ConstPtr &msg_cal)
{
    msg_cal_recv = *msg_cal;
    //ROS_INFO_STREAM("publish: " << msg_cal_recv.xpos1);
    //recv_received = true;
}


