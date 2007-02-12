Summary:	Virtual keyboard for X Window System
Summary(pl.UTF-8):	Wirtualna klawiatura dla systemu X Window
Name:		xvkbd
Version:	2.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://homepage3.nifty.com/tsato/xvkbd/xvkbd-%{version}.tar.gz
# Source0-md5:	d00d367a8158ccd04ff21f2fc35dafe1
URL:		http://homepage3.nifty.com/tsato/xvkbd/
BuildRequires:	Xaw3d-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/share/X11/app-defaults

%description
xvkbd is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(softwares) by clicking on a keyboard displayed on the screen.

%description -l pl.UTF-8
xvkbd to program z wirtualną (graficzną) klawiaturą dla X Window
System ułatwiającą wprowadzanie znaków na wejście innych klientów
(programów) poprzez klikanie na klawiaturze wyświetlonej na ekranie.

%prep
%setup -q

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=%{_bindir} \
	CONFDIR=%{_datadir}/X11 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_appdefsdir}/*
