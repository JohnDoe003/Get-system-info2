#!/usr/bin/env python
# coding: utf-8
def process = "systeminfo".execute()
def output = process.text
def lines = output.split("\n")
def formattedInfo = []
lines.each { line ->
            formattedInfo.add(line[2..-2])
            }

formattedInfo.each { info ->
println info
                   }


