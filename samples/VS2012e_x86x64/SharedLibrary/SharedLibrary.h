// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the SHAREDLIBRARY_EXPORTS
// symbol defined on the command line. This symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// SHAREDLIBRARY_API functions as being imported from a DLL, whereas this DLL sees symbols
// defined with this macro as being exported.
#ifdef SHAREDLIBRARY_EXPORTS
#define SHAREDLIBRARY_API __declspec(dllexport)
#else
#define SHAREDLIBRARY_API __declspec(dllimport)
#endif

// This class is exported from the SharedLibrary.dll
class SHAREDLIBRARY_API CSharedLibrary {
public:
	CSharedLibrary(void);
	// TODO: add your methods here.
};

extern SHAREDLIBRARY_API int nSharedLibrary;

SHAREDLIBRARY_API int fnSharedLibrary(void);
