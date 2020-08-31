# heterogeneous-traffic
Here are all the python scripts used in the master thesis project "Safety Evaluation of Heterogeneous traffic".

--Calibration
  -- find_initial_stats.py       Extract the initial stats from the highD dataset
  -- write_xml.py                Transform the initial stats into xml files used in SUMO simulation
  -- read_thw.py                 Read the THW from highD dataset
  -- sumo_full_output_parser.py  Read data from the SUMO's "full_output" file and save them into csv files
  -- compare_highd_sumo.py       Calculate the speed performance indicator
  
--Final simulation
  -- randomv.py                  Generate random vehicles and write into route files used in SUMO simulation
  -- output_processing.py        read the number of conflicts, number of lane-changing and simulation time from simulation output then write them into an excel file
  
