#!/bin/bash
python3 Front_end.py $1
python3 Davis_Putnam.py
python3 Back_end.py
rm -rf tmp*
