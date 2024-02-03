@echo off

rem Run duarouter command to generate initial route file
duarouter -n left_network.net.xml --route-files trip.trips.xml -o route.rou.xml --ignore-errors

rem Run Python script to modify the route file with random depart times in sorted order
python modify_routes.py

echo Script completed.
