Summary:	Virtual keyboard for X Window System
Summary(pl):	Wirtualna klawiatura dla systemu X Window
Name:		xvkbd
Version:	2.7a
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://homepage3.nifty.com/tsato/xvkbd/xvkbd-%{version}.tar.gz
# Source0-md5:	8e8d4d7fba0b1d90a17ade0c65af727c
URL:		http://homepage3.nifty.com/tsato/xvkbd/
BuildRequires:	Xaw3d-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
xvkbd is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(softwares) by clicking on a keyboard displayed on the screen.

%description -l pl
xvkbd to program z wirtualn± (graficzn±) klawiatur± dla X Window
System u³atwiaj±c± wprowadzanie znaków na wej¶cie innych klientów
(programów) poprzez klikanie na klawiaturze wy¶wietlonej na ekranie.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_appdefsdir}/*
