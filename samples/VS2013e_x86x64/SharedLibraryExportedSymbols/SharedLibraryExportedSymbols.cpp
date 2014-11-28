// SharedLibraryExportedSymbols.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "SharedLibraryExportedSymbols.h"


// This is an example of an exported variable
SHAREDLIBRARYEXPORTEDSYMBOLS_API int nSharedLibraryExportedSymbols=0;

// This is an example of an exported function.
SHAREDLIBRARYEXPORTEDSYMBOLS_API int fnSharedLibraryExportedSymbols(void)
{
	return 42;
}

// This is the constructor of a class that has been exported.
// see SharedLibraryExportedSymbols.h for the class definition
CSharedLibraryExportedSymbols::CSharedLibraryExportedSymbols()
{
	return;
}
