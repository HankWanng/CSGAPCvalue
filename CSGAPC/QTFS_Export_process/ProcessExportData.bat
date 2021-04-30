REM net use L: \\192.168.218.65\pims_tc\ProcessEXPORT
Cd /d E:\MIS\QTFS\QTFS_Export_process
net use L: \\192.168.218.65\pims_tc\ProcessEXPORT ccp1234 /user:ccp\pimsterm

Del L:\ProcessAPCValues.Txt
QTFS.exe /EQ, L:\ProcessAPCValues.Txt, ExportLog, ProcessAPCTags.Txt
Copy "L:\ProcessAPCValues.Txt" "E:\CCJSPIMS\wwyttest\data\"
net use L: /delete
exit

