Summary:	Virtual keyboard for X Window System
Summary(pl):	Wirtualna klawiadura dla systemu X Window
Name:		xvkbd
Version:	2.5
%define	rel	a
Release:	0.%{rel}.1
License:	GPL
Group:		X11/Applications
Source0:	http://homepage3.nifty.com/tsato/xvkbd/xvkbd-%{version}%{rel}.tar.gz
# Source0-md5:	792cbca00c96b6ff54828a0a02f3a621
URL:		http://homepage3.nifty.com/tsato/xvkbd/
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
%setup -q -n %{name}-%{version}%{rel}

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_appdefsdir}/X11/app-defaults/*
