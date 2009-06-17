# -*- coding: utf-8 -*-

from translate.storage.placeables import general

def test_placeable_numbers():
    """Check the correct functioning of number placeables"""
    assert general.NumberPlaceable([u"25"]) in general.NumberPlaceable.parse(u"Here is a 25 number")
    assert general.NumberPlaceable([u"-25"]) in general.NumberPlaceable.parse(u"Here is a -25 number")
    assert general.NumberPlaceable([u"+25"]) in general.NumberPlaceable.parse(u"Here is a +25 number")
    assert general.NumberPlaceable([u"25.00"]) in general.NumberPlaceable.parse(u"Here is a 25.00 number")
    assert general.NumberPlaceable([u"2,500.00"]) in general.NumberPlaceable.parse(u"Here is a 2,500.00 number")
    assert general.NumberPlaceable([u"1\u00a0000,99"]) in general.NumberPlaceable.parse(u"Here is a 1\u00a0000,99 number")

def test_placeable_newline():
    assert general.NewlinePlaceable.parse(u"A newline\n")[1] == general.NewlinePlaceable([u"\n"])
    assert general.NewlinePlaceable.parse(u"First\nSecond")[1] == general.NewlinePlaceable([u"\n"])

def test_placeable_alt_attr():
    assert general.AltAttrPlaceable.parse(u'Click on the <img src="image.jpg" alt="Image">')[1] == general.AltAttrPlaceable([u'alt="Image"'])

def test_placeable_qt_formatting():
    assert general.QtFormattingPlaceable.parse(u'One %1 %99 %L1 are all valid')[1] == general.QtFormattingPlaceable([u'%1'])
    assert general.QtFormattingPlaceable.parse(u'One %1 %99 %L1 are all valid')[3] == general.QtFormattingPlaceable([u'%99'])
    assert general.QtFormattingPlaceable.parse(u'One %1 %99 %L1 are all valid')[5] == general.QtFormattingPlaceable([u'%L1'])