===================================================


     README.TXT
     DataDirect SequeLink
     Version 5.4
     SequeLink 5.4 Client for ODBC
     May 2004
===================================================

This READ.ME file provides specific information about SequeLink 5.4
Client for ODBC on Windows (05.04.011503).
Topics contained in this README file include:

1.0 Enhancements
2.0 Installation


     1.0 ENHANCEMENTS

The following problems have been fixed or workarounds have been
provided:

R011503
-------
* Fix for PS defect DEF0000912.
  SQLGetData incorrectly returns the length of the data available in the length/
  indicator buffer.
* Implemented Enhancement Request DEF0000920.
  When exporting a table from MS Access that contains Null data in a memo column,
  MS Access will bind the parameter with a columnSize of 4294967295.  
  The SequeLink client attempts to allocate a buffer of this size, which typically
  fails due to lack of memory.
  To get around this application bug, the SequeLink Server can now be configured 
  to limit the parameter bind size for SQL_CHAR, SQL_VARCHAR, SQL_BINARY, SQL_VARBINARY
  values to a reasonable value.
  This value can be configured in "DataSourceWorkaroundsClient2".
  

R011502
-------
* Fix for PS defect DEF0000878.
  Fixed problem in the driver when the application uses
  a large Columnsize parameter in the SQLBindParameter call.
* Fix for PS defect DEF0000899.
  Fixed problem in the driver when application executes
  "SELECT .. INTO <temptable>" when requesting keyset driven cursor.
  Fixed problem in the driver when application re-executes
  a select statement with a keyset driven cursor.

R011501
-------
* Fixed crash when SQLBindParameter is called with
  ParameterValuePtr = NULL and *Strlen_or_indPtr = SQL_NULL_DATA.

* Fixed failure when setting SQL_ATTR_APP_PARAM_DESC through
  SQLSetStmtAttr with a NULL pointer. (PS Failure #15005581)

* Fixed state problem with SQLPrepare when same SQL is passed
  as in previous SQLExecDirect.

* Fixed problem in the driver when the application uses
  a large Columnsize parameter in the SQLBindParameter call.

* Fix for PS defect DEF0000737.
  Worked around problem in Microsoft Office 2002-2003
  "Import External Data" Wizard.  The Wizard failed to retrieve
  a list of tables from the datasource.


     2.0 INSTALLATION

Follow the instructions in "SequeLink Installation Guide",
chapter "Installing the ODBC Client on Windows".

--------------
End of Readme.txt