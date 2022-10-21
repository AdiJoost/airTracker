#!/bin/bash
activate(){
	. /home/pi/airTracker/airTracker/bin/activate
	cd /home/pi/airTracker
	python3 /home/pi/airTracker/app.py
}
activate
