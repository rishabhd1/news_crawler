#!/bin/bash
trap break INT
while :
do  
	sleep 60 && scrapy crawl timesofindia && scrapy crawl ndtv
done