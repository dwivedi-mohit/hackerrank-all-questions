# Reading FILE using XSD 

## Metadata

- **ID:** 1638559
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Hard, Mapping and Transformations
- **Skills:** Oracle Integration Cloud

## Summary

This multiple choice question evaluates XSD structure, data mapping, and integration concepts, ideal for senior-level roles. The problem requires identifying mistakes in an XSD document used for processing fixed-length invoice records in Oracle Integration Cloud.

## Problem Statement

The source files from the third-party system come in fixed-length text format. It contains invoice records in header and line format. Below is the specification of the file.

Header Records:

Record Type - 1 character (Fixed value H)

Invoice number - 10 characters long

Total Invoice Amount -10 characters

Invoice Header Description - 50 characters

Line Records:

Record Type - 1 character (Fixed value L)

Line Number- 10 characters long

Line Amount - 10 characters

Line description - 50 characters

Sample content of the file

H100234121A    100000  This is the Invoice for multiple items for the school

L        01     50000      Airconditioners for classrooms of the school

L        02     50000      Furniture items for classrooms of the school

H100234121B    200000 This is the Invoice for multiple items in the Hospital

L        01    100000 Diagnostic equipments for laboratories in the hospital

L        02    100000 Furniture items in various departments in a hospital

Below is the XSD used to read the file in OIC.

`<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:complexType name="HeaderType">
    <xsd:sequence>
      <xsd:element name="RecordType" type="xsd:string" fixed="H" />
      <xsd:element name="InvoiceNumber" type="xsd:string" />
      <xsd:element name="InvoiceAmount" type="xsd:integer"  />
      <xsd:element name="InvoiceHeaderDescription" type="xsd:string"  />
    </xsd:sequence>
  </xsd:complexType>
  <xsd:complexType name="LineType">
    <xsd:sequence>
      <xsd:element name="RecordType" type="xsd:string" fixed="L" />
      <xsd:element name="LineNumber" type="xsd:integer" />
      <xsd:element name="LineAmount" type="xsd:integer" />
      <xsd:element name="LineDescription" type="xsd:integer" />
    </xsd:sequence>
  </xsd:complexType>
  <xsd:element name="Data">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="Header" type="HeaderType" minOccurs="1" maxOccurs="unbounded" />
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>`
```

​​​​​What is the mistake in the XSD document?

## Preview

The source files from the third-party system come in fixed-length text format. I
