#!/bin/bash
gunicorn -w 4 app:app --bind 0.0.0.0:5000