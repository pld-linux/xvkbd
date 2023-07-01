Summary:	Virtual keyboard for X Window System
Summary(pl.UTF-8):	Wirtualna klawiatura dla systemu X Window
Name:		xvkbd
Version:	4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://t-sato.in.coocan.jp/xvkbd/xvkbd-%{version}.tar.gz
# Source0-md5:	64324fe3b4827eb022377c27844dfa8f
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://t-sato.in.coocan.jp/xvkbd/
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdefsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -Dp %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/xvkbd
%{_datadir}/xvkbd
%{_appdefsdir}/XVkbd*
%{_desktopdir}/xvkbd.desktop
%{_pixmapsdir}/xvkbd.png
%{_mandir}/man1/xvkbd.1*
