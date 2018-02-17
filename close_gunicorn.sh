#!/bin/bash
ID=`ps -ef|grep gunicorn|awk '{print $2}'`
echo "Kill belows Process..."
for id in $ID
do
echo "$id"
kill -9 $id
echo "killed $id"
done