# 🚮**Smart-Trash-Bins**
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/trashbin.png)
## Follow us! Here is our social media links. We will continue to update the latest developments...🚀🔗
🔗Youtube channel:
https://www.youtube.com/channel/UC5s7DoMgMNC2AQGXQb5fd2A

📺Blibili channel:
https://www.bilibili.com/video/BV1Dg4y1T7k5/?spm_id_from=333.999.0.0&vd_source=94061f667896bb0f2cfcd84204b0bf78

👽Hackaday channel:
https://hackaday.io/project/190551-smart-trash-bins

💃Tiktok channel:
https://vm.tiktok.com/ZMYWkrSJs/

## Take a look at our demo first！🧩
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/test.gif)
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/IMG_8612.GIF)
The full demo video can be seen in our social media!

## Project introduction and background
Waste classification is an important practice in waste management that involves sorting different types of waste materials based on their composition and properties. The practice of waste classification has gained significance due to the increasing concerns about environmental pollution and sustainability.

Based on the above knowledge, our team hopes to make a device that uses camera recognition for garbage classification. This project uses a Raspberry Pi 3B, Raspberry Pi camera, and four servos to create a trash sorting bin that can automatically separate different types of garbage. The principle of the project is to use the camera to identify the type of garbage being thrown away, and then use the servos to open the corresponding bin for proper disposal.
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/draftdrawing.jpg)

## Project Components
This project uses the following components:
1. Raspberry Pi 3B
2. Raspberry Pi HD camera
3. Four servos
4. Four trash bins
5. Laptop with GPU

The Raspberry Pi 3B is used to run the image recognition algorithm and control the servos. The Raspberry Pi camera is used to capture images of the garbage being thrown away. The four servos are used to open the corresponding bin for disposal. The four trash bins are labeled and the servo uses a simple device to open and close the lid of the trash can.

## Required Environment
The environment and software required for this project:
1. Ncnn
2. Qt Creator 4.6.2 (Enterprise)
3. Google Test
4. Opencv 4.7.0

## How it Works
#### Implement of garbage recognition 
The Raspberry Pi camera is mounted above the trash bin and connected to the Raspberry Pi 3B. The Raspberry Pi runs an image recognition algorithm to identify the type of garbage being thrown away. The four servos are connected to the Raspberry Pi and are used to open the corresponding bin for disposal.

We uses YOLOv5 and a trash dataset of over 4000 images to train our model.
Here is our model performance.
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/master/img/PR_curve.png)
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/master/img/results.png)
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/master/img/val_batch0_pred.jpg)

#### Implementation of servos
PCA9685 can drive 16 servos at the same time. In addition to connecting to the Raspberry Pi, it needs to be powered externally with 5V to drive the servos.

#### How to use:

PCA9685 can generate 16 PWM waveforms with the same frequency through I2C communication.

The angle of the servo is controlled by the pulse width.For example, we want to set the rotation to 90 degrees.

The bandwidth can be derived by equation: B = 0.5+(90/180)*(2.5-0.5)ms = 1.5ms

Use function void set_pwm_ms(const int channel, const double ms) to enable the channel and control the angle.

#### How to connect:
For PCA9685:

![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/pindesc.jpeg)
![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/pindesc2.jpeg)

Connect the VCC pin of the PCA9685 to the 3.3V pin of the Raspberry Pi.

Connect the GND pin of the PCA9685 to the GND pin of the Raspberry Pi.

Connect the SDA pin of the PCA9685 to the SDA pin of the Raspberry Pi.

Connect the SCL pin of PCA9685 to the SCL pin of Raspberry Pi.


![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/driverboard.jpg)

For MG996R:
The four MG996R servos are respectively connected to the VCC pin, GND pin, and signal pin of the driver board.

![image](https://github.com/qlkaaron/Smart-Trash-Bin/blob/HistoryFile/img/motor.jpg)

## Getting Started
To get started with this project, you will need a Raspberry Pi 3B, Raspberry Pi camera, four servos, and four trash bins. You will also need to install the image recognition algorithm on the Raspberry Pi and connect the servos to the Raspberry Pi.
Then you need to install Open-cv, Ncnn and QT in your system. You can find how to install them on their official website or Github.
Once everything is set up, you can start using the trash sorting bin by throwing away different types of garbage and watching as the bin automatically separates and sorts the garbage for you.
```commandline
git clone https://github.com/qlkaaron/Smart-Trash-Bin
cd Smart-Trash-Bin
cmake ..
make
.\SmartTrashBin
```

## Conclusion
This is a project of the Real Time Embedded Programming (2022-23) at the University of Glasgow. The Smart-trash-bins project can have many benefits for protecting the environment, such as:
1. Reducing landfill waste: By automatically sorting different types of garbage, the project can help reduce the amount of waste that ends up in landfills. For example, organic waste can be composted, while plastics and other materials can be recycled.
2. Promoting recycling: The project can help promote recycling by making it easier for people to properly dispose of their recyclable materials. By providing a convenient and efficient way to sort and dispose of recyclable materials, the project can encourage more people to recycle.
3. Improving waste management: The project can help improve waste management by reducing the amount of waste that needs to be sorted manually by waste management workers. This can help save time and resources, and make waste management more efficient.
4. Raising awareness: By showcasing the benefits of proper waste management and recycling, the project can help raise awareness about the importance of protecting the environment. This can help encourage more people to adopt eco-friendly habits and reduce their impact on the environment.

Finally, we sincerely hope that our project can help the cause of environmental protection to a higher level.

## We A Team #21 👨‍👩‍👧‍👦
|  Name   | GUID  | Project roles |
|  ----  | ----  | ---- |
| Likun Qian  | 2741162Q | Image Recognition Engineer |
| Hongyu Chen  | 2778437C | Software Engineer |
| Yitao Zhang  | 2728975Z | Electronics Engineer |
| Yuwen Yao  | 2729768Y | Mechanical Engineers |

### [Likun Qian](https://github.com/qlkaaron)👷‍♂️
Responsible for developing and training object detection algorithms using YOLOv5 algorithm and OpenCV library.

1. Collect and organize relatively complete garbage image datasets on the Internet.
2. Develop and test computer vision models to identify and classify different types of trash.
3. Tune and optimize object detection algorithms for better accuracy and performance.
4. Integrate object detection algorithms with the rest of the system.
5. Deploy the trained model to the Raspberry Pi system.

### [Hongyu Chen](https://github.com/CHYMU)👷
Responsible for the development of software architecture for garbage classification and Qt-based graphical user interface.

1. Design and implement the software architecture of the system.
2. Develop and test software modules to control servos, cameras, and other hardware components.
3. Create a user-friendly interface for users to interact with the system.
4. Integrate object detection algorithms with software systems.
5. Test and debug software to ensure proper functionality.

### [Yitao Zhang](https://github.com/YitaoZz)👨‍🔧
Responsible for the design and implementation of the electronic hardware components for the waste sorting bins.

1. Select and source the appropriate electronic components for the project.
2. Design and test circuits for servos, cameras, and other hardware components.
3. Create a power system for the Raspberry Pi and other electronic components.
4. Integrate electronic hardware with software systems.


### [Yuwen Yao](https://github.com/Yuwenyao)👨‍💻
Responsible for the design and implementation of the mechanical hardware components for the waste sorting bins.

1. Responsible for connecting to the Qt system to realize the monitoring of garbage classification results on the computer.
2. Design and test power management systems to ensure proper functioning of all electronic components and optimize power usage.
3. Work with software engineers and image recognition engineers to integrate electronic hardware with software systems and object detection algorithms.
4. Test and debug electronic hardware to ensure proper function.

## Documentation📚
1. Initial presentation of the project: https://github.com/qlkaaron/Smart-Trash-Bin/blob/master/team21.pptx
2. Requirements document: https://docs.google.com/document/d/1v_nFBcVMhV61sFpqelyqPs9qTDsMhMfhK4uxnItb3NU/edit?usp=sharing

## Copyright©
The project is signed under the MIT License, see [LICENSE.md](https://github.com/qlkaaron/Smart-Trash-Bin/blob/master/LICENSE) for details.

## Welcome to contact us!📧
smarttrashbin_uog@gmail.com
