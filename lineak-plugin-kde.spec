#
# TODO:
# - seperate each plugin
#
%define		packagename	lineak_kdeplugins

Summary:	KDE related plugins for the lineakd daemon
Summary(pl):	Wtyczki do demona lineakd związane z KDE
Name:		lineak-plugin-kde
Version:	0.8.4
Release:	0.9
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
# Source0-md5:	4ddfc475e4df27f8822e0b08c0f701b5
URL:		http://lineak.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lineakd-devel >= %{version}
BuildRequires:	sed >= 4.0
Requires:	lineakd >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of plugins for lineakd. The plugins allow binding
actions to special keys.

This package contains the following plugins:
 amarok_plugin
 juk_plugin
 kdesktop_plugin
 kmail_plugin
 kmix_plugin
 konqueror_plugin

These plugins support the following macros:
 amarok_plugin:	AMAROK_PLAY, AMAROK_PAUSE, AMAROK_STOP, AMAROK_PLAYPAUSE,
		AMAROK_BACK, AMAROK_FORWARD, AMAROK_SEEK, AMAROK_ADDMEDIA,
		AMAROK_VOLUMEUP, AMAROK_VOLUMEDOWN, AMAROK_VOLUMEMUTE,
		AMAROK_TOGGLEPLAYLIST, AMAROK_ENABLERANDOM

 juk_plugin:	JUK_PLAY, JUK_PAUSE, JUK_STOP, JUK_PLAYPAUSE, JUK_BACK,
		JUK_FORWARD, JUK_SEEKBACK, JUK_SEEKFORWARD, JUK_VOLUMEUP,
		JUK_VOLUMEDOWN, JUK_VOLUMEMUTE, JUK_STARTPLAYINGPLAYLIST,
		JUK_OPENFILE

 kdesktop_plugin:	KDE_LOCK_DESKTOP, KMENU, KDESKTOP_NEXT,
			KDESKTOP_PREVIOUS, KDESKTOP_EXECUTE, KDE_LOGOUT

 kmail_plugin:	KMAIL_COMPOSE

 kmix_plugin: KMIX_VOLUP, KMIX_VOLDOWN, KMIX_MUTE

 konq_plugin: KONQUEROR

%description -l pl
To jest zbiór wtyczek do lineakd. Wtyczki te pozwalają na dowiązywanie
akcji do specjalnych klawiszy.

Ten pakiet zawiera następujące wtyczki:
 amarok_plugin
 juk_plugin
 kdesktop_plugin
 kmail_plugin
 kmix_plugin
 konqueror_plugin

Te wtyczki obsługują następujące makra:
 amarok_plugin:	AMAROK_PLAY, AMAROK_PAUSE, AMAROK_STOP, AMAROK_PLAYPAUSE,
		AMAROK_BACK, AMAROK_FORWARD, AMAROK_SEEK, AMAROK_ADDMEDIA,
		AMAROK_VOLUMEUP, AMAROK_VOLUMEDOWN, AMAROK_VOLUMEMUTE,
		AMAROK_TOGGLEPLAYLIST, AMAROK_ENABLERANDOM

 juk_plugin:	JUK_PLAY, JUK_PAUSE, JUK_STOP, JUK_PLAYPAUSE, JUK_BACK,
		JUK_FORWARD, JUK_SEEKBACK, JUK_SEEKFORWARD, JUK_VOLUMEUP,
		JUK_VOLUMEDOWN, JUK_VOLUMEMUTE, JUK_STARTPLAYINGPLAYLIST,
		JUK_OPENFILE

 kdesktop_plugin:	KDE_LOCK_DESKTOP, KMENU, KDESKTOP_NEXT,
			KDESKTOP_PREVIOUS, KDESKTOP_EXECUTE, KDE_LOGOUT

 kmail_plugin:	KMAIL_COMPOSE

 kmix_plugin: KMIX_VOLUP, KMIX_VOLDOWN, KMIX_MUTE

 konq_plugin: KONQUEROR

%prep
%setup -q -n %{packagename}-%{version}

# kill plugin dir existence test
sed -i -e 's/test ! -d \$pdir/false/' admin/lineak.m4.in
cat admin/{acinclude.m4.in,lineak.m4.in} > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-lineak-plugindir=%{_libdir}/lineakd/plugins \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lineakd/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lineakd/plugins/*.so
%{_mandir}/man1/lineak_kdeplugins.1*
