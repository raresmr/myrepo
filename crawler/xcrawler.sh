#!/bin/bash -x
touch output
python crawl
sed -i "1s/^/Subject: Crawler report `date`\n\n/" output
sed -i "2s/^/Content-type: text\/html; charset=\"iso-8859-1\"\n\n/" output
#ssmtp rares@visual.ly < output
ssmtp rares.mironeasa@scribblelive.com < output
ssmtp stas.filippov@scribblelive.com < output
sleep 10
rm output
