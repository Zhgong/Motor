#!/bin/sh
# 1. change date to the past
# 2. run parallels
# 3. change date back



# old date

o_month=01
o_day=10
o_year=15

# get currentdate
month=`date +'%m'`
day=`date +"%d"`
hour=`date +"%H"`
minute=`date +"%M"`
year=`date +"%y"`

curr_dty=$month$day$hour$minute$year
old_dty=$o_month$o_day$hour$minute$o_year


changeback(){
    # change it back
    echo "changing date back"
    sudo date $curr_dty

    # synct date back
    sudo ntpdate -u time.apple.com

}


echo "current date is:"
date

# change date
echo "changing date to old one"
sudo date $old_dty

# start PD
open /Applications/Parallels\ Desktop.app/

# wait for 5 seconds
sleep 8

# chage date back
changeback
