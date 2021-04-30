REM net use L: \\192.168.218.65\pims_tc
Cd /d E:\MIS\QTFS\QTFS_Export
net use L: \\192.168.218.65\pims_tc ccp1234 /user:ccp\pimsterm
Del L:\APCValues.Txt
QTFS.exe /EQ, L:\APCValues.Txt, ExportLog, APCTags.Txt
net use L: /delete
exit

