#!/bin/bash

timestamp=$(date +"%Y%m%d-%H%M")
base_path="/home/harun/bootcamp-final/app"

if [ -f "$base_path/logs/app.log" ]; then
    cp "$base_path/logs/app.log" "$base_path/log_archive/app-$timestamp.log"
    echo " $timestamp - log kopyalandı" >> "$base_path/cron.log"
else
    echo " $timestamp - logs/app.log bulunamadı" >> "$base_path/cron.log"
fi
