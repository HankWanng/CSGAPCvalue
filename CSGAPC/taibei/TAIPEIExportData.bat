REM net use L: \\192.168.218.241\pims\TAIPEIEXPORT
Cd /d E:\MIS\QTFSTAIPEI\QTFS_Export_TAIPEI
net use L: \\192.168.218.241\pims ccp1234 /user:ccp\tankpublic
Del L:\TAIPEIAPCValues.Txt
QTFS.exe /EQ, L:\TAIPEIAPCValues.Txt, ExportLog, TAIPEIAPCTags.Txt
net use L: /delete
exit

