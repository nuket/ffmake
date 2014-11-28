// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the SHAREDLIBRARYEXPORTEDSYMBOLS_EXPORTS
// symbol defined on the command line. This symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// SHAREDLIBRARYEXPORTEDSYMBOLS_API functions as being imported from a DLL, whereas this DLL sees symbols
// defined with this macro as being exported.
#ifdef SHAREDLIBRARYEXPORTEDSYMBOLS_EXPORTS
#define SHAREDLIBRARYEXPORTEDSYMBOLS_API __declspec(dllexport)
#else
#define SHAREDLIBRARYEXPORTEDSYMBOLS_API __declspec(dllimport)
#endif

// This class is exported from the SharedLibraryExportedSymbols.dll
class SHAREDLIBRARYEXPORTEDSYMBOLS_API CSharedLibraryExportedSymbols {
public:
	CSharedLibraryExportedSymbols(void);
	// TODO: add your methods here.
};

extern SHAREDLIBRARYEXPORTEDSYMBOLS_API int nSharedLibraryExportedSymbols;

SHAREDLIBRARYEXPORTEDSYMBOLS_API int fnSharedLibraryExportedSymbols(void);
