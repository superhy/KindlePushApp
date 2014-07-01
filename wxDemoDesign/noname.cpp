///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Sep  8 2010)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

wxMainFrame::wxMainFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	m_menubarFile = new wxMenuBar( 0 );
	m_menuFile = new wxMenu();
	wxMenuItem* m_menuItemLogin;
	m_menuItemLogin = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("login") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemLogin );
	
	wxMenuItem* m_menuItemRegister;
	m_menuItemRegister = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("register") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemRegister );
	
	wxMenuItem* m_menuItemExit;
	m_menuItemExit = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("exit") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemExit );
	
	m_menubarFile->Append( m_menuFile, wxT("file") ); 
	
	m_menuEdit = new wxMenu();
	wxMenuItem* m_menuItemPush;
	m_menuItemPush = new wxMenuItem( m_menuEdit, wxID_ANY, wxString( wxT("push") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuEdit->Append( m_menuItemPush );
	
	m_menubarFile->Append( m_menuEdit, wxT("edit") ); 
	
	m_menuView = new wxMenu();
	m_menubarFile->Append( m_menuView, wxT("view") ); 
	
	m_menuTools = new wxMenu();
	m_menubarFile->Append( m_menuTools, wxT("tools") ); 
	
	m_menuHelp = new wxMenu();
	m_menubarFile->Append( m_menuHelp, wxT("help") ); 
	
	this->SetMenuBar( m_menubarFile );
	
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );
	
	m_staticTextUserWel = new wxStaticText( this, wxID_ANY, wxT("you haven't logined !"), wxDefaultPosition, wxSize( 500,-1 ), 0 );
	m_staticTextUserWel->Wrap( -1 );
	m_staticTextUserWel->SetFont( wxFont( 10, 70, 93, 92, false, wxEmptyString ) );
	m_staticTextUserWel->SetForegroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_HIGHLIGHTTEXT ) );
	m_staticTextUserWel->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_APPWORKSPACE ) );
	
	bSizer3->Add( m_staticTextUserWel, 0, wxALL, 5 );
	
	this->SetSizer( bSizer3 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	this->Connect( m_menuItemExit->GetId(), wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( wxMainFrame::OnExit ) );
}

wxMainFrame::~wxMainFrame()
{
	// Disconnect Events
	this->Disconnect( wxID_ANY, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( wxMainFrame::OnExit ) );
	
}
