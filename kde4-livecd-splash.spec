
Summary:	PLD-LiveCD KDE4 splash screen
Summary(pl.UTF-8):	Splash do PLD-LiveCD z KDE4
Name:		kde4-livecd-splash
Version:	0
Release:	1
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	5ee0d3c5ff1fd2ac75458b477ab38fac
URL:		http://livecd.pld-linux.pl
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD-LiveCD KDE4 splash screen.

%description -l pl.UTF-8
Splash do PLD-LiveCD z KDE4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
cp -ar LiveCD $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/LiveCD
