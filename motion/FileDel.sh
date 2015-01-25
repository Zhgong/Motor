#!/bin/bash
# delete files older than 30 days
#

DIR=/home/pi/motion/video

find $DIR -name '*.avi' -mtime +30 -exec rm {} \;
find $DIR -name '*.jpg' -mtime +30 -exec rm {} \;
find $DIR -name '*.mpg' -mtime +30 -exec rm {} \;
