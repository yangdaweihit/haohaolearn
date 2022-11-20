#!/bin/bash

killall conky
sleep 2s
		
conky -c $HOME/.config/conky/simple-conky-clcok/conky.conf &> /dev/null &
conky -c $HOME/.config/conky/system/conky.conf &> /dev/null &

exit
