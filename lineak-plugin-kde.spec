#
# TODO:
# - seperate each plugin
#
%define		packagename	lineak_kdeplugins

Summary:	These are KDE related plugins for the lineakd daemon.
Summary(pl):	To s± wtyczki do demona lineakd zwi±zane z KDE.
Name:		lineak-plugin-kde
Version:	0.8.4
Release:	0.9
License:	GPL
Url:		http://lineak.sourceforge.net
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
# Source0-md5:	4ddfc475e4df27f8822e0b08c0f701b5
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lineakd >= %{version}
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
To jest zbiór wtyczek do lineakd. Wtyczki te pozwalaj± na dowi±zywanie
akcji do specjalnych klawiszy.

Ta paczka zawiera nastêpuj±ce wtyczki:
 amarok_plugin
 juk_plugin
 kdesktop_plugin
 kmail_plugin
 kmix_plugin
 konqueror_plugin

Te wtyczki obs³uguj± nastêpuj±ce makra:
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/lineakd/plugins/*
%{_mandir}/*/*
