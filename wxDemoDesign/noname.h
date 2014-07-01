///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Sep  8 2010)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __noname__
#define __noname__

#include <wx/string.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/menu.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/stattext.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class wxMainFrame
///////////////////////////////////////////////////////////////////////////////
class wxMainFrame : public wxFrame 
{
	private:
	
	protected:
		wxMenuBar* m_menubarFile;
		wxMenu* m_menuFile;
		wxMenu* m_menuEdit;
		wxMenu* m_menuView;
		wxMenu* m_menuTools;
		wxMenu* m_menuHelp;
		wxStaticText* m_staticTextUserWel;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OnExit( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		wxMainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("KindlePush"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 800,550 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		~wxMainFrame();
	
};

#endif //__noname__
