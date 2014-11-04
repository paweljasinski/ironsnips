import clr
clr.AddReferenceToFileAndPath("bin/Debug/dotnetenums")
import dotnetenums

pymonday = dotnetenums.DotNetEnums.Days.Mon
pysat = dotnetenums.DotNetEnums.Days.Sat

if pymonday == dotnetenums.DotNetEnums.day:
    print "not OK"

if pysat == dotnetenums.DotNetEnums.day:
    print "OK"

instance = dotnetenums.DotNetEnums()
if instance.instanceDay == dotnetenums.DotNetEnums.Days.Wed:
    print "OK"