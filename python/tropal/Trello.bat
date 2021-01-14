@echo off

curl -X POST "https://trello.com/1/organizations/{tropalerp}/exports?key={34fc8c60f8adc6a5065b3164efd629e0}&token={271bce676bf1a7a040f05058d412dae83144c75a2ec23cf428b9bab178d15e69}" --data 'attachments=false'

curl "https://trello.com/1/organizations/{tropalerp}/exports/{60000ea5311b1a7040143ca7}?key={34fc8c60f8adc6a5065b3164efd629e0}&token={271bce676bf1a7a040f05058d412dae83144c75a2ec23cf428b9bab178d15e69}"

:get_download_link
curl "https://trello.com/1/organizations/{tropalerp}/?exports=true&key={34fc8c60f8adc6a5065b3164efd629e0}&token={271bce676bf1a7a040f05058d412dae83144c75a2ec23cf428b9bab178d15e69}"

set result=CALL :get_download_link
%result%>lien_trello.txt
EXIT