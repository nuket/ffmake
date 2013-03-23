// SharedLibrary.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "SharedLibrary.h"


// This is an example of an exported variable
SHAREDLIBRARY_API int nSharedLibrary=0;

// This is an example of an exported function.
SHAREDLIBRARY_API int fnSharedLibrary(void)
{
	return 42;
}

// This is the constructor of a class that has been exported.
// see SharedLibrary.h for the class definition
CSharedLibrary::CSharedLibrary()
{
	return;
}
