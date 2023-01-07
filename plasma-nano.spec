%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma-nano
Version:	5.26.5
Release:	1
Summary:	Plasma interface for embedded devices
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5I18n)

%description
Plasma interface for embedded devices.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang plasma-nano --all-name --with-html

%files -f plasma-nano.lang
%{_libdir}/qt5/qml/org/kde/plasma/private/nanoshell
%{_datadir}/metainfo/org.kde.plasma.nano.desktoptoolbox.appdata.xml
%{_datadir}/plasma/packages/org.kde.plasma.nano.desktoptoolbox
%{_datadir}/plasma/shells/org.kde.plasma.nano
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.nano.desktop
%{_datadir}/kservices5/plasma-package-org.kde.plasma.nano.desktoptoolbox.desktop
