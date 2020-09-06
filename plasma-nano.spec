%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma-nano
Version:	5.19.5
Release:	1
Summary:	Plasma interface for embedded devices
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
Patch0:		0001-StartupFeedback-calculate-background-color-from-icon.patch
Patch1:		0002-StartupFeedback-Add-optional-color-argument.patch
Patch2:		0003-Restore-property-binding.patch
Patch3:		0004-Make-window-background-transparent-again.patch
Patch4:		0005-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch5:		0006-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch6:		0007-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch7:		0008-Remove-timeout.patch
Patch8:		0009-Make-the-More-Wallpapers.-string-translatable.patch
Patch9:		0010-fix-explorer-layout.patch
Patch10:	0011-don-t-set-manually-all-those-flags.patch
Patch11:	0012-restore-previous-hacks.patch
Patch12:	0013-Revert-restore-previous-hacks.patch
Patch13:	0014-more-hacks-for-proper-display.patch
Patch14:	0015-prettier-startup-feedback.patch
Patch15:	0016-not-rounded-anymore.patch
Patch16:	0017-use-animators.patch
Patch17:	0018-Fix-QML-errors.patch
Patch18:	0019-rework-open-animation.patch
Patch19:	0020-give-a-margin-to-wallpapers.patch
Patch20:	0021-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
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
%{_datadir}/kservices5/*.desktop
%{_datadir}/metainfo/org.kde.plasma.nano.desktoptoolbox.appdata.xml
%{_datadir}/plasma/packages/org.kde.plasma.nano.desktoptoolbox
%{_datadir}/plasma/shells/org.kde.plasma.nano
