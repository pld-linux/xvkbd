%define		rel		a

Summary:	Virtual keyboard for X window system
Name:		xvkbd
Version:	2.5
Release:	0.%{rel}.1
License:	GPL
Group:		X11/Applications
Source0:	http://homepage3.nifty.com/tsato/xvkbd/xvkbd-%{version}%{rel}.tar.gz
# Source0-md5:	792cbca00c96b6ff54828a0a02f3a621
URL:		http://homepage3.nifty.com/tsato/xvkbd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xvkbd is a virtual (graphical) keyboard program for X Window System which provides
facility to enter characters onto other clients (softwares) by clicking on a keyboard
displayed on the screen.

%prep
%setup -q -n %{name}-%{version}%{rel}

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
