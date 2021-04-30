REM net use L: \\192.168.218.65\bpapimsdata\ELEXPORT
Cd /d E:\MIS\QTFS\QTFS_Export_EL
net use L: \\192.168.218.65\bpapimsdata\ELEXPORT ccp1234 /user:ccp\tankpublic
Del L:\ELAPCValues.Txt
QTFS.exe /EQ, L:\ELAPCValues.Txt, ExportLog, ELAPCTags.Txt
net use L: /delete
exit

