%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		plasma-nano
Version:	6.4.2
Release:	%{?git:0.%{git}.}1
Summary:	Plasma interface for embedded devices
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-nano/-/archive/%{gitbranch}/plasma-nano-%{gitbranchd}.tar.bz2#/plasma-nano-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/plasma-nano-%{version}.tar.xz
%endif
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Wayland)
BuildRequires:	cmake(KWayland) >= 5.90.0
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6ItemModels)
# Renamed after 6.0 2025-05-03
%rename plasma6-nano

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Plasma interface for embedded devices.

%files -f %{name}.lang
%{_qtdir}/qml/org/kde/plasma/private/nanoshell
%{_datadir}/plasma/shells/org.kde.plasma.nano
