# Concert Bracelet

## Concept
This product is a bracelet designed for concerts to provide a fun way to further immerse yourself with the artist when he/ she is performing. The product is an LED strip in the shape of a bracelet to put on your wrist, and it's meant to be light and simple so it doesn't get in the way while you are having fun. It also has a motion sensor that you keep in your hand so that the color can change based on the movement of your wrist. The bracelet has two colors for the purpose of this assignment - BLACK and RED, but you can program it to have any range of colors.

In Protopie, the code also sends a signal to your phone so that the artist name and album comes to display on your phoen screen like at concert when you want to display messages on your phone. In a way, this is a two-in-one product meant to take your concert experience to the next level. I decided to use the colors black and red because it is the signature colors of Jennie's new album "Ruby", which I will be using as an example throughout this project.

## Flow Chart

![Flow Chart - Concert Bracelet](https://github.com/user-attachments/assets/959601c3-e87d-4fd7-b2e0-bf90a0b28b5d)

## Process

First, I coded the micropython file so that the IMU and LED strips interacted accordingly with each other. Then, I connnected the actions of the UI (Protopie) matched with the functions of the bracelet.

## Code

![Code - Assignment 4](https://github.com/user-attachments/assets/5f46eb68-02b9-46e8-9136-48c5db61cc19)

## Stages

### Stage 1 
Bracelet is in idle state. -> In Protopie, it will have a black screen until the wrist is tilted in either direction.

![IMG_4279](https://github.com/user-attachments/assets/0b3adee0-dd68-497a-8194-3cf69a461787)
![IMG_3102](https://github.com/user-attachments/assets/996174d5-74a5-4176-8cfc-543f92a7c1f8)

### Stage 2
Moving the wrist in certain ways will trigger the LED lights to react in various ways.

For example, if you tilt your wrist to the left, the LED strip will turn red and your phone screen will say the artist name.

![IMG_3103](https://github.com/user-attachments/assets/d3f13cd2-92b7-4e82-a926-5528159c037c)
![IMG_4282](https://github.com/user-attachments/assets/6c9751f6-e826-4cc9-ae2c-c0be9eb89dcc)

If you tilt your wrist the other way, the LED strip will turn red once again and your phone screen will display the album name.

![IMG_3103](https://github.com/user-attachments/assets/16ae6c4b-5abf-467c-95e2-d488481e7e06)
![IMG_4281](https://github.com/user-attachments/assets/209fd034-9c65-43b8-b82c-ca531a39da9a)

### Stage 3

Once you are finished, you can take off the bracelet and it will turn off.

![IMG_3101](https://github.com/user-attachments/assets/9920a997-0900-4343-ae3d-5bc9da05241f)

## Final Product
