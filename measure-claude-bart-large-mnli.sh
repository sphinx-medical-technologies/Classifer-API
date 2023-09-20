#!/bin/sh

count=20
i=0
tot=0
# rm gen-measure.json

TEST_URL="http://0.0.0.0:8000"

while [ $i -lt $count ];do
	response_time=$(curl -X "GET" -w "$i: %{time_total} %{http_code} %{size_download} %{url_effective}\n" -H "accept: application/json" -o gen-measure.json -s "http://0.0.0.0:8000/classify?text=I%20am%20very%20happy%20right%20now&categories=positive&categories=negative")
	echo "response_time [$response_time]"
	val=$(echo $response_time | cut -f2 -d' ')
	echo $val
	tot=$(echo "scale=3;${tot}+${val}" | bc)
	echo $tot
	jshon < gen-measure.json
	rm gen-measure.json
	i=$((i+1))
done

avg=$(echo "scale=3; ${tot}/${count}" |bc)
echo "   ........................."
echo "   AVG: $tot/$count = $avg"

sleep 30
